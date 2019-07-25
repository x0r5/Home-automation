<?php

$command = escapeshellcmd('python3 scripts/lampoff.py');
$output = shell_exec($command);
echo $output;

?>