//button functionality

$(document).on('click', '#lampon', function () {
    console.log("lampon");
    $(this).css("background-color", "green");
    $('#lampoff').css("background-color", "gray");

    //ajax
    $.ajax({
        type: 'POST',
        url: 'lampon.php',
        success: function (data) {
            alert(data);
        }
    });
});

$(document).on('click', '#lampoff', function () {
    console.log("lampoff");
    $(this).css("background-color", "green");
    $('#lampon').css("background-color", "gray");

    $.ajax({
        type: 'POST',
        url: 'lampon.php',
        success: function (data) {
            alert(data);
        }
    });
});

/*

$(document).ready(function() {

    $("#lamoff").click(function(){
        $("#lampoff").css("background-color", "green");
        $("#lampon").css("background-color", "gray");
        console.log('lampoff pressed');
    });

});
$(document).ready(function(){
    $("#lampon").click(function () {
        $("#lampon").css("background-color", "green");
        $("#lampoff").css("background-color", "gray");
        console.log('lampon pressed');

    });
});



    ///ajax comes here
    $.ajax({
        type: 'POST', //hidden from the url
        url: 'ajax/login.php',
        data: _data,  //sent to the server
        dataType: 'json',
        async: true
    })
        .done(function ajaxDone(data){
            //console.log('ajax done');
            console.log(data);
            if(data.redirect != undefined){
                window.location = data.redirect;
            }else if(data.error != undefined){
                _error.text(data.error).show();
            }
        })
        .fail(function ajaxFailed(e){
            console.log('ajax fail');
            console.log(e);


        })
        .always(function ajaxAlwaysDoThis(data){
            console.log("Always");
        })

    return false;

    $(document).ready(function(){
        $("#lampon").click(function(){
             $.ajax({
                 type: 'POST',
                 url: 'lampon.php',
                 async: true
                success: function(data) {
                    alert(data);
                    $("p").text(data);

                }
            });
            $("#lampon").css("background-color", "green");
            $("#lampoff").css("background-color", "gray")
   });


*/