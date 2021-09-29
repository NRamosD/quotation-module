function PriceFilter(){
    if(parseFloat(SincePrice.value)>parseFloat(ToPrice.value)){
        return alert("El primer valor debe ser mayor al segundo.")
    }
    if (SincePrice.value!='' && ToPrice.value!=''){
        let content = `
        <span class="badge badge-warning" style="font-size: 1em;">Desde $${SincePrice.value} hasta $${ToPrice.value}</span>`
        labels.innerHTML += content
        return
    }
    if(SincePrice.value!=''){
        let content = `
        <span class="badge badge-warning" style="font-size: 1em;">Desde $${SincePrice.value}</span>`
        labels.innerHTML += content
    }
    if (ToPrice.value!=''){
        let content = `
        <span class="badge badge-warning" style="font-size: 1em;">Hasta $${ToPrice.value}</span>`
        labels.innerHTML += content
    }
}
function ProductTypeFilter(){
    let items = document.getElementById("ProductTypeOption");
    let selected = items.options[items.selectedIndex].text;
    let content = `
        <span class="badge badge-warning" style="font-size: 1em;">${selected}</span>
    `
    labels.innerHTML += content
}
function ProducerFilter(){
    let content = `
        <span class="badge badge-warning" style="font-size: 1em;">${ProducerName.value}</span>
    `
    labels.innerHTML += content
}
function SupplierFilter(){
    let content = ` 
        <span class="badge badge-warning" style="font-size: 1em;">${ProviderName.value}</span>
    `
    labels.innerHTML += content
}