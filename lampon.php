<?php

//system("echo raspberry | sudo -S python /var/www/PiHome/scripts/lights/lampon.py");
//header(Location: 'index.php' ) ;

$command = escapeshellcmd('python3 test.py');
$output = shell_exec($command);
echo $output;


?>