(function($){
    $('form').submit(function(event){
        event.preventDefault();

        let data = new FormData(this);

        var action = function(d){
            console.log(d);
        }

        $.ajax({
            url:'/api/productfiles/',
            data: data,
            type: POST,
            contentType: false,
            processData: false,
            succes: action,
            error: action
        })
    })
}(jQuery))