<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>managemyrobot</title>
  <style>
    /*.table{*/
    /*  !*width: 100%;*!*/
    /*  border-collapse: collapse;*/
    /*}*/
    /*.table td{*/
    /*  border: 1px solid #000;*/
    /*  padding: 5px;*/
    /*}*/
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
      <td>rbid</td>
      <td>rbname</td>
      <td>exploreavgtime</td>
      <td>rbtype</td>
      <td>userinfoid</td>
      <td>action</td>
    </tr>
    <c:forEach items="${robotinfos}" var="roto">
      <tr>
        <td>${roto.rbid}</td>
        <td>${roto.rbname}</td>
        <td>${roto.exploreavgtime}</td>
        <td>${roto.rbtype}</td>
        <td>${roto.userinfoid}</td>
        <td>
          <button onclick="edit(${roto.rbid},'${roto.rbname}',${roto.exploreavgtime},'${roto.rbtype}',${roto.userinfoid})">edit</button>
          <button onclick="deleted(${JSON.stringify(roto)})">deleted</button>
          <a href="${pageContext.request.contextPath}/robotList?method=exploration&rbid=${roto.rbid}">Exploration Record</a>
        </td>
      </tr>
    </c:forEach>
  </table>
  <div>

  <button onclick="back()">back</button>
  </div>
</div>
<script>

  function back() {
    window.location.href = "http://localhost:8080/${pageContext.request.contextPath}/welcome.jsp";
  }
  function edit(rid,rbname,exploreavgtime,rbtype,userinfoid) {
    window.location.href = "http://localhost:8080/${pageContext.request.contextPath}/robotList?method=toUpdateRobotView&rid="
            +rid+"&rbname="+rbname+"&exploreavgtime="+exploreavgtime+"&rbtype="+rbtype+"&userinfoid="+userinfoid;
  }

  function deleted(roto) {

    window.location.href = "http://localhost:8080/${pageContext.request.contextPath}/robotList?method=deleteRobot&rbid="
            +roto.rbid+"&rbname="+roto.rbname+"&exploreavgtime="+roto.exploreavgtime+"&rbtype="+roto.rbtype+"&userinfoid="+roto.userinfoid;
  }

</script>
</body>
</html>
