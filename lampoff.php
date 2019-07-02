<?php

system("echo raspberry | sudo -S python /var/www/PiHome/scripts/lights/lampoff.py");
header(Location: 'index.php' ) ;

?>