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


const menuButton=document.querySelector('.menu');
const mobileDrawer=document.querySelector('.mobile-drawer');
const mobileBackdrop=document.querySelector('.mobile-menu-backdrop');
const closeMobileMenu=()=>{
  document.body.classList.remove('mobile-menu-open');
  if(menuButton) menuButton.setAttribute('aria-expanded','false');
  if(mobileDrawer) mobileDrawer.setAttribute('aria-hidden','true');
};
const openMobileMenu=()=>{
  document.body.classList.add('mobile-menu-open');
  if(menuButton) menuButton.setAttribute('aria-expanded','true');
  if(mobileDrawer) mobileDrawer.setAttribute('aria-hidden','false');
};
if(menuButton&&mobileDrawer){
  menuButton.addEventListener('click',()=>{
    document.body.classList.contains('mobile-menu-open') ? closeMobileMenu() : openMobileMenu();
  });
  mobileDrawer.querySelectorAll('a').forEach((link)=>link.addEventListener('click',closeMobileMenu));
}
if(mobileBackdrop) mobileBackdrop.addEventListener('click',closeMobileMenu);
window.addEventListener('keydown',(event)=>{if(event.key==='Escape') closeMobileMenu();});
window.addEventListener('resize',()=>{if(window.innerWidth>900) closeMobileMenu();});
