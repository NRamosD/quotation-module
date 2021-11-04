if(typeof(Storage)!= 'undefined'){
    let valor = "jjkajs"
    sessionStorage.setItem('clave',valor)
    localStorage.setItem('clva',valor)
    localStorage.getItem('clva')
    localStorage.removeItem('clva')
    //otra forma
    sessionStorage.clave = "loquevayadentrodelaclave"

    localStorage.clear()
}else{
    alert("no sirve el storage")
}