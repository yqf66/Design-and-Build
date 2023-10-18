<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>robot-list</title>
    <meta name="renderer" content="webkit">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" href="../lib/layui-v2.6.3/css/layui.css" media="all">
    <link rel="stylesheet" href="../css/public.css" media="all">
</head>
<body>
<div class="layuimini-container">
    <div class="layuimini-main">
        <table class="layui-table">
            <thead>
            <tr>
                <th style="width: 150px" lay-data="{field:'robotid', width:150}">robotid</th>
                <th style="width: 200px" lay-data="{field:'image', width:200}">image</th>
                <th lay-data="{field:'cdate'}">cdate</th>
                <th lay-data="{field:'book'}">book</th>
                <th lay-data="{field:'key'}">key</th>
                <th lay-data="{field:'cube'}">cube</th>
                <th lay-data="{field:'startTime'}">start_time</th>
                <th lay-data="{field:'endTime'}">end_time</th>
                <th lay-data="{field:'action'}">action</th>
            </tr>
            </thead>
            <tbody>
            <c:forEach items="${list}" var="roto">
                <tr >
                    <td>${roto.robotid}</td>
                    <td >
                        <img class="img" height="150" width="150"
                             src="${pageContext.request.contextPath}/ImageViewServlet?name=${roto.filename}">
                    </td>
                    <td>${roto.cdate}</td>
                    <td>${roto.book}</td>
                    <td>${roto.key}</td>
                    <td>${roto.cube}</td>
                    <td>${roto.startTime}</td>
                    <td>${roto.endTime}</td>
                    <td><input type="button"
                               class="btn layui-btn"
                               value="edit"
                               roto-id="${roto.id}"
                               roto-book="${roto.book}"
                               roto-key="${roto.key}"
                               roto-cube="${roto.cube}"
                               roto-startTime="${roto.startTime}"
                               roto-endTime="${roto.endTime}"
                    ></td>
                </tr>
            </c:forEach>
            </tbody>
        </table>

    </div>
</div>
<script src="../lib/layui-v2.6.3/layui.js" charset="utf-8"></script>
<script>
    layui.use(function () {
        var table = layui.table;
        var util = layui.util;
        var $ = layui.jquery;

        //转换静态表格
        table.init('parse-table-demo', {});

        layer.photos({
            photos: '.img'
            , anim: 1
        });
        $(".btn").click(function () {
            const id = $(this).attr("roto-id");
            const book = $(this).attr("roto-book");
            const key = $(this).attr("roto-key");
            const cube = $(this).attr("roto-cube");
            const startTime = $(this).attr("roto-startTime");
            const endTime = $(this).attr("roto-endTime");

            var index = layer.open({
                title: 'edit',
                type: 2,
                shade: 0.2,
                maxmin:true,
                shadeClose: true,
                area: ['100%', '100%'],
                content: './table/edit-image.jsp',
                success(layero, index){
                    var body = layer.getChildFrame('body', index);
                   body.find("#id").val(id);
                   body.find("#book").val(book);
                   body.find("#key").val(key);
                   body.find("#cube").val(cube);
                   body.find("#startTime").val(startTime);
                   body.find("#endTime").val(endTime);
                }
            });
            $(window).on("resize", function () {
                layer.full(index);
            });
        })

        $(".img").click(function () {
            layer.photos({
                photos: {
                    "title": "",
                    "id": 123,
                    "start": 0,
                    "data": [
                        {
                            "alt": "picture name",
                            "pid": 666,
                            "src": $(this).attr("src"),
                            "thumb": $(this).attr("src")
                        }
                    ]
                }
                , anim: 5
            });
        })

    });
</script>

</body>
</html>
