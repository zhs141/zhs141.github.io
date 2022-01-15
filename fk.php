<?php
    $fp=fopen("访客.txt",'r');
    fbb=fread($fp,filesize("访客.txt"));
    fclose($fp);
    $fbb=string(number_format($fbb)+1);
    $fp=fopen("访客.txt",'w');
    fwrite($fp,$fbb);
    fclose($fp);
    echo "这个网页一共被访问了" . $fbb . '次';
?>
