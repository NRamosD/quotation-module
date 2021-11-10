//Para mover al recargar página
let url = window.location.href

if(url=="http://127.0.0.1:8000/"){
    sessionStorage.removeItem('etiquetas')
    home.className += " active";
}
if(url.includes("http://127.0.0.1:8000/cotizar/")){
    quote.className += " active";
}
if(url.includes("http://127.0.0.1:8000/cargar_documento/")){
    sessionStorage.removeItem('etiquetas')
    documentLoad.className += " active";
}
if(url.includes("http://127.0.0.1:8000/informes/")){
    sessionStorage.removeItem('etiquetas')
    reports.className += " active";
}
if(url.includes("http://127.0.0.1:8000/info/")){
    sessionStorage.removeItem('etiquetas')
    info.className += " active";
}
