<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
<style type="text/css">
div {
    background-color: lightgrey;
    width: 600px;
    border: 25px solid green;
    padding: 25px;
    margin-left: 350px;
    margin-top:100px;
}
h1,h2,h3,
{
	color:green;
}
</style>






</head>
<body><div>
<h1>Welcome to our website!</h1>
<h2>Please input your username and password!</h2>
<form method ="post" action="./login">
&nbsp;		username<input type="text" name="username"><br/>
&nbsp;		password<input type="text" name="password"><br/>
&nbsp;		<input type="SUBMIT" name="submit" value="submit"><br/>	
<h3>Not have a account?</h3>
&nbsp;	    <a href="register.jsp">  register </a>
		
</form>
</div>
</body>
</html>