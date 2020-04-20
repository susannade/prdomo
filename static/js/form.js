    $('form').on('submit', function() {
        $.ajax({
            data : {
                name : $('#kod').val(),
            },
            type: 'POST',
            url: '/check'
        })
        .done(function(data){

            if (data.error){
                $('#notok').text(data.error).show();
            }
            else{
                $('#ok').text(data.name).show();
            }
        });
    });
