# Mari Olivier - Flask + PostgreSQL + Railway

Landing page recriada a partir do protótipo Lovable, usando Python Flask, PostgreSQL e pasta persistente para imagens.

## Rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Abra `http://localhost:5000`.

## Railway

1. Suba este projeto para um repositório no GitHub.
2. No Railway, crie um novo projeto a partir do repositório.
3. Adicione um serviço PostgreSQL.
4. Garanta que a variável `DATABASE_URL` esteja disponível no serviço Flask.
5. Crie um volume e monte em `/app/app/static/uploads`.
6. Defina a variável `UPLOAD_DIR=/app/app/static/uploads`.
7. Deploy.

## Personalização rápida

- Trocar WhatsApp: edite o link nos botões dentro de `app/templates/index.html` ou use a variável do `.env` como referência.
- Trocar imagens fixas: substitua os arquivos em `app/static/img` mantendo os nomes.
- Imagens enviadas pelo endpoint `/upload` ficam em `app/static/uploads`, preparado para volume persistente.

## Estrutura

```txt
app.py
requirements.txt
Procfile
railway.json
app/
  templates/index.html
  static/css/style.css
  static/js/main.js
  static/img/
  static/uploads/
```
