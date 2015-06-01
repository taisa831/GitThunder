<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>formsample</title>
    <link rel="stylesheet" type="text/css" href="/css/style_login.css" media="all" />
</head>
<body>
<div id="form">
    <p class="form-title">Login</p>
    <form action="/login" method="POST" name="login">
        <p>Login</p>
        <p class="mail"><input type="email" name="username" id="user" /></p>
        <p>Password</p>
        <p class="pass"><input type="password" name="password" id="pwd" /></p>
        <p class="submit"><input type="submit" name="Submit" value="Login" /></p>
    </form>
</div>
</body>
</html>
