const nav=document.querySelector('.nav');
const onScroll=()=>nav.classList.toggle('scrolled',window.scrollY>20);
window.addEventListener('scroll',onScroll);onScroll();
const io=new IntersectionObserver((entries)=>{entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('show')})},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
document.querySelectorAll('details').forEach(d=>d.addEventListener('toggle',()=>{if(d.open){document.querySelectorAll('details').forEach(o=>{if(o!==d)o.open=false})}}));


document.querySelectorAll('.premium-button').forEach((button)=>{
  button.addEventListener('click',()=>{
    button.classList.remove('clicked');
    void button.offsetWidth;
    button.classList.add('clicked');
  });
});
