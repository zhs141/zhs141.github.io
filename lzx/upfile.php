<?php
//设置文件执行的编码
header("Content-type:text/html;charset=utf-8");
$file=$_FILES["file"]["tmp_name"];
$filename=$_FILES["file"]["name"];
$path="~/";
$res=move_uploaded_file($file,$path.$filename);
?>
