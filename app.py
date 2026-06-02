import os
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", BASE_DIR / "app" / "static" / "uploads"))
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

db = SQLAlchemy()

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    email = db.Column(db.String(180), nullable=True)
    phone = db.Column(db.String(60), nullable=True)
    interest = db.Column(db.String(120), nullable=True)
    message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class UploadedImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


def create_app():
    app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-me")
    database_url = os.getenv("DATABASE_URL", "sqlite:///instance/app.db")
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/contato")
    def contato():
        data = request.form if request.form else request.json or {}
        lead = Lead(
            name=data.get("name", "").strip() or "Sem nome",
            email=data.get("email", "").strip(),
            phone=data.get("phone", "").strip(),
            interest=data.get("interest", "").strip(),
            message=data.get("message", "").strip(),
        )
        db.session.add(lead)
        db.session.commit()
        if request.is_json:
            return jsonify({"ok": True, "message": "Contato registrado com sucesso."})
        return redirect(url_for("index") + "#contato")

    @app.post("/upload")
    def upload():
        # Endpoint simples para usar com volume persistente no Railway.
        file = request.files.get("image")
        if not file:
            return jsonify({"ok": False, "error": "Nenhuma imagem enviada."}), 400
        safe = secure_filename(file.filename)
        if not safe:
            return jsonify({"ok": False, "error": "Nome de arquivo inválido."}), 400
        ext = safe.rsplit(".", 1)[-1].lower() if "." in safe else ""
        if ext not in {"jpg", "jpeg", "png", "webp", "gif"}:
            return jsonify({"ok": False, "error": "Formato não permitido."}), 400
        filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{safe}"
        dest = UPLOAD_DIR / filename
        file.save(dest)
        row = UploadedImage(filename=filename, original_name=file.filename)
        db.session.add(row)
        db.session.commit()
        return jsonify({"ok": True, "url": f"/static/uploads/{filename}"})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
