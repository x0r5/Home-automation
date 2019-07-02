<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Home automation system</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script type="text/javascript">
    $(document).ready(function(){
        $("#lampon").click(function(){
             $.ajax({
                type: 'POST',
                url: 'lampon.php',
                success: function(data) {
                    alert(data);
                    $("p").text(data);

                }
            });
            $("#lampon").css("background-color", "green");
            $("#lampoff").css("background-color", "gray")
   });
   $("#lampoff").click(function(){
             $.ajax({
                type: 'POST',
                url: 'lampoff.php',
                success: function(data) {
                    alert(data);
                    $("p").text(data);

                }
            });
            $("#lampoff").css("background-color", "green");
            $("#lampon").css("background-color", "gray")
   });
});
    </script>
  </head>
  <body>
    
    <div class="container">
        <div class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-secondary" id="lampon" action="">ON</button>
            <button type="button" class="btn btn-secondary" id="lampoff">OFF</button>
        </div>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>