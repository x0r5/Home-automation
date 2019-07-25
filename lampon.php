<?php

$command = escapeshellcmd('python3 scripts/lampon.py');
$output = shell_exec($command);
echo $output;


?>