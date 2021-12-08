

$(function () {
    $("#jej").click(function(e){
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
