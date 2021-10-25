//Para mover al recargar página
let url = window.location.href
if(url == "http://127.0.0.1:8000/"){
    home.className += " active";
}
if(url == "http://127.0.0.1:8000/cotizar/"){
    quote.className += " active";
}
if(url == "http://127.0.0.1:8000/cargar_documento/"){
    documentLoad.className += " active";
}
if(url == "http://127.0.0.1:8000/informes/"){
    reports.className += " active";
}
if(url == "http://127.0.0.1:8000/info/"){
    info.className += " active";
}
