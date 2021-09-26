const PRODUCT_URL = "http://127.0.0.1:8000/api/product/";

const HTMLResponse = document.querySelector("#productsTableELements")

//const tp = document.createDocumentFragment();

fetch(PRODUCT_URL)
    .then((response) => response.json())
    .then((products) => {
        products.forEach(product => {
            let fila = document.createElement('tr');
            let casilla1 = document.createElement('td');
            let casilla2 = document.createElement('td');
            let casilla3 = document.createElement('td');
            casilla1.innerText=product.id_product;
            casilla2.innerText=product.product_name;
            casilla3.innerText=product.price;
            fila.appendChild(casilla1);
            fila.appendChild(casilla2);
            fila.appendChild(casilla3);
            HTMLResponse.appendChild(fila);
        });
        //HTMLResponse.appendChild(fila);
        /* console.log(product)
        const tp = product.map((product) => `<tr> <td>${product.id_product }</td> <td>${ product.product_name }</td> <td>${ product.price }</td> </tr>`);
        HTMLResponse.innerHTML = tp; */
});





