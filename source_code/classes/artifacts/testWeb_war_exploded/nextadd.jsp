<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<% String rbname =(String)session.getAttribute("Rbname"); %>
<% String Exploreavgtime =(String)session.getAttribute("Exploreavgtime"); %>
<% String Rbtype =(String)session.getAttribute("Rbtype"); %>
<% Integer userinfoid =(Integer)session.getAttribute("userinfoid"); %>

<%= rbname %>
<%= Exploreavgtime %>
<%= Rbtype %>
<%= userinfoid %>
</body>
</html>