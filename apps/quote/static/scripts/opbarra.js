var URLactual = window.location;
const linkColor = document.querySelectorAll('.nav__link'); 
linkColor.forEach(l => l.classList.remove('active'));
let btn1=document.getElementById('home')
let btn2=document.getElementById('quote')
if(URLactual=='http://127.0.0.1:8000'){
    btn1.classList.add('active')
}else if(URLactual=='http://127.0.0.1:8000/cotizar'){
    btn2.classList.add('active')
}
    
//this.classList.add('active');