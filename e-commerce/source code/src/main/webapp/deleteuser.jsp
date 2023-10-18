<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<form method="post" action="./deleteUser">
	username : <input type="text" name="username" placeholder="please input username" required />
	<input type="SUBMIT" name="deleteuser" value="deleteuser">
	<%String msg = (String)session.getAttribute("msg"); %>
	<%= msg == null ? "" : msg %>
</form>
</body>
</html>