//Para mover al recargar página
let url = window.location.href

if(url=="http://127.0.0.1:8000/"){
    sessionStorage.removeItem('selectedProductsValues')
    sessionStorage.removeItem('etiquetas')
    sessionStorage.removeItem('selectedProductsHtml')
    home.className += " active";
}
if(url.includes("http://127.0.0.1:8000/cotizar/")){
    quote.className += " active";
}
if(url.includes("http://127.0.0.1:8000/cargar_documento/")){
    sessionStorage.removeItem('selectedProductsValues')
    sessionStorage.removeItem('etiquetas')
    sessionStorage.removeItem('selectedProductsHtml')
    documentLoad.className += " active";
}
if(url.includes("http://127.0.0.1:8000/informes/")){
    sessionStorage.removeItem('selectedProductsValues')
    sessionStorage.removeItem('etiquetas')
    sessionStorage.removeItem('selectedProductsHtml')
    reports.className += " active";
}
if(url.includes("http://127.0.0.1:8000/info/")){
    sessionStorage.removeItem('etiquetas')
    sessionStorage.removeItem('selectedProducts')
    sessionStorage.removeItem('selectedProductsHtml')
    info.className += " active";
}