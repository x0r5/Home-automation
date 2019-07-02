<?php

system("echo raspberry | sudo -S python /var/www/PiHome/scripts/lights/lampon.py");
header(Location: 'index.php' ) ;

?>