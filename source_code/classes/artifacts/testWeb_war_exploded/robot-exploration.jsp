<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Exploration Record</title>
    <style>
        .box{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }

        /** Table 表格样式 **/
        .table{
            border-collapse: collapse;
            width:800px;
            border:1px solid #c6c6c6 !important;
            margin-bottom:20px;
        }
        .table th{
            border-collapse: collapse;
            border-right:1px solid #c6c6c6 !important;
            border-bottom:1px solid #c6c6c6 !important;
            background-color:#ddeeff !important;
            padding:5px 9px;
            font-size:14px;
            font-weight:normal;
            text-align:center;
        }
        .table td{
            border-collapse: collapse;
            border-right:1px solid #c6c6c6 !important;
            border-bottom:1px solid #c6c6c6 !important;
            padding:5px 9px;
            font-size:12px;
            font-weight:normal;
            text-align:center;
            word-break: break-all;
        }
        .table tr:nth-child(odd){
            background-color:#fff !important;
        }
        .table tr:nth-child(even){
            background-color: #f8f8f8 !important;
        }

    </style>
</head>
<body>


<div class="box">
    <table border="1" class="table">
        <tr>
            <td>robotid</td>
            <td>image</td>
            <td>cdate</td>
            <td>success</td>
        </tr>
        <c:forEach items="${list}" var="roto">
            <tr>
                <td>${roto.robotid}</td>
                <td>
                   <img width="50" height="50"  src="${pageContext.request.contextPath}/ImageViewServlet?name=${roto.filename}">
                </td>
                <td>${roto.cdate}</td>
                <td>${roto.success}</td>
            </tr>
        </c:forEach>
    </table>
    <div>
        <button onclick="back()">back</button>
    </div>
</div>
<script>
    function back() {
        window.location.href = "http://localhost:8080/${pageContext.request.contextPath}/robotList?method=toRobotListView";
    }
</script>
</body>
</html>
