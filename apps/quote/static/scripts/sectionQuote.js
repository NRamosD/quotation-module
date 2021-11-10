
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
function ProducerFilter(){
    producer = ProducerName.value
    if(producer==""){
        try{
            valueProducer.remove()
        }catch{
    
        }
        return
    }
    let content = `
        <span id="valueProducer" class="badge badge-warning" style="font-size: 1em;">${producer}</span>
    `
    labels.innerHTML += content
}
function SupplierFilter(){
    supplier = ProviderName.value
    if(supplier==""){
        try{
            valueSupplier.remove()
        }catch{
    
        }
        return
    }
    let content = ` 
        <span id="valueSupplier" class="badge badge-warning" style="font-size: 1em;">${supplier}</span>
    `
    labels.innerHTML += content
}

//guarda el array con los datos que se requieren 
let selectedId = []


$("#productsTable tr").click(function(){
    $(this).addClass('selected').siblings().removeClass('selected');    
    var nombre_articulo=$(this).find('td:nth-child(2)').html();
    var id=$(this).find('td:nth-child(1)').html();
    if(selectedId.indexOf(id)===-1){
        selectedId.push(id)
        console.log(`contenido actual del array ${selectedId}`)
        var ultimo= parseInt(0,10);
        var ultimo= parseInt(ultimo + ($("#tabla_cotizacion").find("th").last().html()),10);
        ultimo++;
        var fila= "<tr><th>"+ ultimo +"</th><td>"+ nombre_articulo +"</td><td>"+ '12.50' +"</td><td>"+ '12.50' +'</td><td><button id="bt_borrar" onclick="deleteRow()" value="' + id + '"><i class="fas fa-trash-alt"></i></button></td></tr>';
        /* alert(ultimo);
        alert(value);*/   
        var btn = document.createElement("TR");
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
    sessionStorage.setItem('etiquetas', labels.innerHTML )
    sessionStorage.setItem('selectedProducts', selectedItems.innerHTML )
 });

//Envío de datos
$(function () {
    $('#btnToQuoteDetail').on('click', function () {
        var Status = $(this).val();
        $.ajax({
            url: "http://127.0.0.1:8000/Listar1/",
            type:"post",
            dataType: 'json',
            data: {
                'getdata': JSON.stringify(selectedId)
            },
            success: function (res, status) {
                alert(res);
                alert(status);
            },
            error: function (res) {
                alert(res.status);                                                                                                                          
            }
        });
    });
});


function preloadFunc(){
    labels.innerHTML = sessionStorage.getItem('etiquetas')
    selectedItems.innerHTML = sessionStorage.getItem('selectedProducts')
}


if(typeof(Storage)!= 'undefined'){
    //otra forma
    //sessionStorage.clave = "loquevayadentrodelaclave"
    //localStorage.clear()*/
    window.onpaint = preloadFunc();
}else{
    console.log("No storage")
}


