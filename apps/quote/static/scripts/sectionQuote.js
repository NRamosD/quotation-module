
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

/*
$("#productsTable tr").click(function(){
    $(this).addClass('selected').siblings().removeClass('selected');    
    let nombre_articulo=$(this).find('td:nth-child(1)').html();
    let price=$(this).find('td:nth-child(4)').html();
    let id=$(this).find('td:nth-child(1)').html();
    if(selectedId.indexOf(id)===-1){
        selectedId.push(id)
        console.log(`contenido actual del array ${selectedId}`)
        ultimo= parseInt(0,10);
        ultimo= parseInt(ultimo + ($("#tabla_cotizacion").find("th").last().html()),10);
        ultimo++;
        let fila= "<tr><th>"+ ultimo +"</th><td>"+ nombre_articulo +"</td><td>"+ price +'</td><td><button id="bt_borrar" onclick="deleteRow()" value="' + id + '"><i class="fas fa-trash-alt"></i></button></td></tr>';
        //alert(ultimo);
        //alert(value);
        let btn = document.createElement("TR");
        btn.innerHTML=fila;
        document.getElementById("selectedItems").appendChild(btn);
    }
    
});
*/

//PARA CARGA CON AJAX EN LAS TABLAS SIGUIENTES
$("#productsTable tr").click(function(){
    $(this).addClass('selected').siblings().removeClass('selected');
    let nombre_articulo=$(this).find('td:nth-child(1)').html();
    $.ajax({
        //url : 'http://127.0.0.1:8000/api/product/',
        url : 'http://127.0.0.1:8000/api/productSupplierJoin/',
    
        type : 'GET',
    
        dataType : 'json',
    
        success : function(json) {
            $("#selectedItemsLower").empty();
            $("#selectedItemsHigher").empty();

            //Obtengo solo los que llevan el nombre del seleccionado
            let dataFiltered = json.filter(function(element){
                return element.product_name == nombre_articulo ;
            });

            let limite;
            if( dataFiltered.length > 5 ){
                limite = 5
            }else{ limite = dataFiltered.length }
            //copia del dataFiltered
            let arraySegundo = dataFiltered.slice();

            let lowToHigh = arraySegundo.sort(function(a, b){
                if (a.price < b.price) {
                    return -1;
                }
            });
            let HighToLow = dataFiltered.sort(function(a, b){
                if (a.price > b.price) {
                    return -1;
                }
            });

            console.log("menor a mayor ",lowToHigh)
            console.log("mayor a menor",HighToLow)

            for (let index = 0; index < limite; index++) {
                let num = index + 1
                let fila= `
                    <tr>
                        <td>${num}</td>
                        <td>${lowToHigh[index].supplier_name}</td>
                        <td>${lowToHigh[index].price}</td>
                        ${(parseInt(lowToHigh[index].availability)==0)?'<td>Mismo día</td>':`<td>${lowToHigh[index].availability}</td>`}
                        <td>${lowToHigh[index].brand}</td>
                        <td><input type="checkbox" class="chBox" value="${lowToHigh[index].id_product}"></td>
                    </tr>
                `
                let elementTR = document.createElement("tr");
                elementTR.innerHTML=fila;
                document.getElementById("selectedItemsLower").appendChild(elementTR);
            }
            /*
            for (let index = 0; index < limite; index++) {
                let num = index + 1
                
                let fila= `
                    <tr>
                        <td>${num}</td>
                        <td>${HighToLow[index].price}</td>
                        <td>${HighToLow[index].id_supplier}</td>
                        <td>${HighToLow[index].brand}</td>
                        <td><input type="checkbox" value="first_checkbox"></td>
                    </tr>
                `
                let elementTR = document.createElement("tr");
                elementTR.innerHTML=fila;
                document.getElementById("selectedItemsHigher").appendChild(elementTR);
            }*/
            


            /*
            let pricesArray = dataFiltered.map(function(x){
                return x.price
            })
            let pricesFloat = []
            for (let index = 0; index < pricesArray.length; index++) {
                pricesFloat.push(pricesArray[index])
            }

            console.log(pricesFloat)
            let lessPrice = []
            for (let index = 0; index < 3; index++) {
                let x = Math.min(pricesFloat)
                lessPrice.push(x)
                let indexToEliminate = pricesFloat.indexOf(x)
                console.log(index+" aqui array "+ lessPrice +" aqui indice a eliminar"+ indexToEliminate)
                pricesArray.splice(indexToEliminate, 1);
            }
            console.log("Aqui van los precios menores "+lessPrice)
            console.log(dataFiltered)*/
        },

        error : function(xhr, status) {
            alert('Disculpe, existió un problema');
        },
    
        // código a ejecutar sin importar si la petición falló o no
        complete : function(xhr, status) {
            //alert('Petición realizada');
        }
    });
    
});


//Elementos en vista previa
$("#btn_vistaprevia").click(function(){
    $("#selectedPreviewItems").empty();
    $.ajax({
        url : 'http://127.0.0.1:8000/api/product/',
        dataType : 'json',
    
        success : function(json) {
            
            //$("#selectedItemsHigher").empty();

            //Obtengo solo los que llevan el nombre del seleccionado
            //selectedId
            let dataPreview;
            selectedId.forEach(id => {
                dataPreview = json.filter(function(obj){
                    return obj.id_product == id ;
                });
            });
            limite = selectedId.length
            for (let index = 0; index < limite; index++) {
                let fila= `
                    <tr>
                        <td>${dataPreview[index].product_name}</td>
                        <td>${dataPreview[index].price}</td>
                        <td>${dataPreview[index].id_supplier}</td>
                        <td>${dataPreview[index].brand}</td>
                        <td>${dataPreview[index].brand_vehicle}</td>
                        <td>${dataPreview[index].model_vehicle}</td>
                        <td>${dataPreview[index].year_vehicle}</td>
                    </tr>
                `
                let elementTR = document.createElement("tr");
                elementTR.innerHTML=fila;
                document.getElementById("tabla_preview").appendChild(elementTR);
            }
        },

        error : function(xhr, status) {
            alert('Disculpe, existió un problema');
        },
    
        // código a ejecutar sin importar si la petición falló o no
        complete : function(xhr, status) {
            //alert('Petición realizada');
        }
    });
    
});



/*
if( $('.chBox').prop('checked') ) {
    alert('Seleccionado');
}
$( '.chBox' ).on( 'click', function() {
    if( $(this).is(':checked') ){
        // Hacer algo si el checkbox ha sido seleccionado
        alert("El checkbox con valor " + $(this).val() + " ha sido seleccionado");
    } else {
        // Hacer algo si el checkbox ha sido deseleccionado
        alert("El checkbox con valor " + $(this).val() + " ha sido deseleccionado");
    }
});*/
//$(".chBox").click(function(){
//$('input:checkbox.chBox').on('click',function() {
$(document).on('change','input[type="checkbox"]' ,function(e) {
    //if(this.id=="fiscal") {
        let id = this.value
        if(this.checked){
            if(selectedId.indexOf(id)===-1){
                selectedId.push(id)
                console.log(`contenido actual del array ${selectedId}`)
            }
            //alert("HOLA "+ this.value)
        }else {
            //alert("El checkbox con valor " + this.value + " ha sido deseleccionado");
            let i = selectedId.indexOf(id);
            if ( i !== -1 ) {
                selectedId.splice( i, 1 );
                console.log(`contenido actual del array ${selectedId}`)
            }
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
        let dataQuote={
            "id_quote": 1,
            "description": eleDataQuote.value,
            "date": "2021-11-29T02:06:51.161934Z",
            "total": "245.35"
        }
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        $.ajax({
            //url : 'http://127.0.0.1:8000/api/product/',
            url : 'http://127.0.0.1:8000/api/quotes/',
            
            data : dataQuote,
            headers : {
                "X-CSRFToken" : getCookie('csrftoken') 
            },
            type : 'POST',
        
            dataType : 'json',
        
            success : function(json) {
                alert("Cotización guardada con éxito!")
                setTimeout( function() { window.location.href = "http://127.0.0.1:8000/"; }, 1000 );
            },
            error : function(xhr, status) {
                alert('Disculpe, existió un problema');
            },
        
            // código a ejecutar sin importar si la petición falló o no
            complete : function(xhr, status) {
                //alert('Petición realizada');
            }
        });
    });
});


$(function () {
    $("#saveDataQuote").click(function(e){
        sessionStorage.setItem('selectedProductsValues', selectedId.toString())
        $('#vS').val(selectedId.toString())
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




