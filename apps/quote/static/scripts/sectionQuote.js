
//ETIQUETA DE PRECIO
function PriceFilter(){
    if(parseFloat(SincePrice.value)>parseFloat(ToPrice.value)){
        return alert("El primer valor debe ser mayor al segundo.")
    }
    if (SincePrice.value=='' && ToPrice.value==''){
        try{
            valuesPrice.remove()
        }catch{

        }
    }
    if (SincePrice.value!='' && ToPrice.value!=''){
        try{
            valuesPrice.remove()
        }catch{

        }
        let content = `
        <span id="valuesPrice" class="badge badge-warning" style="font-size: 1em;">Desde $${SincePrice.value} hasta $${ToPrice.value}</span>`
        labels.innerHTML += content
        return
    }
    if(SincePrice.value!=''){
        try{
            valuesPrice.remove()
        }catch{

        }
        let content = `
        <span id="valuesPrice" class="badge badge-warning" style="font-size: 1em;">Desde $${SincePrice.value}</span>`
        labels.innerHTML += content
    }
    if (ToPrice.value!=''){
        try{
            valuesPrice.remove()
        }catch{

        }
        let content = `
        <span id="valuesPrice" class="badge badge-warning" style="font-size: 1em;">Hasta $${ToPrice.value}</span>`
        labels.innerHTML += content
    }
}
//ETIQUETA DE TIPO DE PRODUCTO
function ProductTypeFilter(){
    try{
        valueType.remove()
    }catch{

    }
    let items = document.getElementById("ProductTypeOption");
    let selected = items.options[items.selectedIndex].text;
    if(selected==""){
        try{
            valueType.remove()
        }catch{
    
        }
        return
    }
    let content = `
        <span id="valueType" class="badge badge-warning" style="font-size: 1em;">${selected}</span>
    `
    labels.innerHTML += content
}
//ETIQUETA DE LA MARCA
function ProducerFilter(){
    try{
        valueType.remove()
    }catch{

    }
    let items = document.getElementById("ProductBrandOption");
    let selected = items.options[items.selectedIndex].text;
    if(selected==""){
        try{
            valueType.remove()
        }catch{
    
        }
        return
    }
    let content = `
        <span class="badge badge-warning" style="font-size: 1em;">${selected}</span>
    `
    labels.innerHTML += content
}
function SupplierFilter(){
    try{
        valueType.remove()
    }catch{

    }
    let items = document.getElementById("ProductProviderOption");
    let selected = items.options[items.selectedIndex].text;
    if(selected==""){
        try{
            valueType.remove()
        }catch{
    
        }
        return
    }
    let content = `
        <span class="badge badge-warning" style="font-size: 1em;">${selected}</span>
    `
    labels.innerHTML += content
}

//guarda el array con los datos que se requieren 
let selectedId;


$("#productsTable tr").click(function(){
    $(this).addClass('selected').siblings().removeClass('selected');    
    let nombre_articulo=$(this).find('td:nth-child(2)').html();
    let price=$(this).find('td:nth-child(4)').html();
    let id=$(this).find('td:nth-child(1)').html();
    if(selectedId.indexOf(id)===-1){
        selectedId.push(id)
        console.log(`contenido actual del array ${selectedId}`)
        ultimo= parseInt(0,10);
        ultimo= parseInt(ultimo + ($("#tabla_cotizacion").find("th").last().html()),10);
        ultimo++;
        let fila= "<tr><th>"+ ultimo +"</th><td>"+ nombre_articulo +"</td><td>"+ price +'</td><td><button id="bt_borrar" onclick="deleteRow()" value="' + id + '"><i class="fas fa-trash-alt"></i></button></td></tr>';
        /* alert(ultimo);
        alert(value);*/   
        let btn = document.createElement("TR");
        btn.innerHTML=fila;
        document.getElementById("selectedItems").appendChild(btn);
    }
    
});
function deleteRow(){
    let i = selectedId.indexOf( bt_borrar.value );
    if ( i !== -1 ) {
        selectedId.splice( i, 1 );
    }
    let row = bt_borrar.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

$(".changeInPage").click(function(){
    sessionStorage.setItem('selectedProductsValues', selectedId.toString())
    sessionStorage.setItem('etiquetas', labels.innerHTML )
    sessionStorage.setItem('selectedProductsHtml', selectedItems.innerHTML )
});

//Envío de datos
$(function () {
    $("#saveDataQuote").click(function(e){
        let data = sessionStorage.getItem('selectedProductsValues')
        $('#eleDataQuote').val(data)
        alert(data)
    });
});

$(function () {
    $("#btnToQuoteDetail").click(function(e){
        sessionStorage.setItem('selectedProductsValues', selectedId.toString())
        $('#vS').val(selectedId.toString())
    });
});


function preloadFunc(){
    if(sessionStorage.getItem('selectedProductsValues')==null){
        selectedId = [];
        labels.innerHTML = sessionStorage.getItem('etiquetas')
        selectedItems.innerHTML = sessionStorage.getItem('selectedProductsHtml')
    }else{
        datos = sessionStorage.getItem('selectedProductsValues')
        idsArray = datos.split(',')
        selectedId = idsArray
        labels.innerHTML = sessionStorage.getItem('etiquetas')
        selectedItems.innerHTML = sessionStorage.getItem('selectedProductsHtml')
    }
}

function isNumberKey(evt){
    let charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

$(document).ready(function(){

    // code to read selected table row cell data (values).
    /*$("#table").on('keypress','.quantity',function(){
        // get the current row
        let currentRow=$(this).closest("tr"); 
        let col1=currentRow.find("td:eq(4)"); // get current row 1st TD value
        console.log(col1.text())
        let data=parseFloat(col1.text())*parseInt(this.value);
        col1.html(data)
        console.log(col1.text())
        //alert(data)
    });*/
});

/*
$(".quantity").change(function () {
    alert(this.value)
    $('#table tr').eq(1).find('td').val('HELLOO');
});
*/


if(typeof(Storage)!= 'undefined'){
    //otra forma
    //sessionStorage.clave = "loquevayadentrodelaclave"
    //localStorage.clear()*/
    window.onpaint = preloadFunc();
}else{
    console.log("No storage")
}


