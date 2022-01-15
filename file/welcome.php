<html>
<head>
<meta charset="utf-8">
<title>选择</title>
</head>
<body>

<?php
<form action="welcome.php" method="post">
验证码: <input type="text" name="age">
<input type="submit" value="提交">
</form>
 
switch ($age)
{
case "张三":
    Header("https://zhs141.github.io/file");
    break;
default:
    echo "你输入的验证码是错误哒～";
}
/?>
</body>
</html>
