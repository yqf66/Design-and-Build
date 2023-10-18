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
<% String username =(String)session.getAttribute("username"); %>
welcome <%= username %>

<h1>Click this to creat your robot</h1>
<a href="robot.jsp">  creatmyrobot </a> <br>
<a href="robotList?method=toRobotListView"> managemyrobot </a>  <br>
<a href="page/index.jsp"> index </a><br>
<a href="page/page/upload.jsp"> upload robot </a><br>
<h2>^^_</h2>
<h3>^^_</h3>

</div>
</body>
</html>
