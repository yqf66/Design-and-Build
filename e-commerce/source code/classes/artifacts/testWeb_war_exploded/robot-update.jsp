<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>update</title>
</head>
<body>

<form action="robotList" method="get">
    <div>
        <label>robot id</label>
        <input type="text"  disabled  value="${robo.rbid}" />
        <input type="hidden" name="rid"  value="${robo.rbid}" />
        <input type="hidden" name="method"  value="updateRobot" />
    </div>
    <div>
        <label>robot name</label>
        <input type="text" name="rbname" value="${robo.rbname}" />
    </div>
    <div>
        <label>exploration average time</label>
        <input type="text" disabled   value="${robo.exploreavgtime}" />
    </div>

    <div>
        <label>robot type</label>
        <input type="text" name="rbtype" value="${robo.rbtype}" />
    </div>
    <div>
        <label>user id</label>
        <input type="text" disabled name="userinfoid"  value="${robo.userinfoid}" />
    </div>
    <input type="submit" value="submit">
</form>
</body>
</html>
