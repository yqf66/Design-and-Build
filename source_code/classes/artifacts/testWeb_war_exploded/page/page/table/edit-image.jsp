<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>layui</title>
    <meta name="renderer" content="webkit">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" href="../../lib/layui-v2.6.3/css/layui.css" media="all">
    <link rel="stylesheet" href="../../css/public.css" media="all">
    <style>
        body {
            background-color: #ffffff;
        }
    </style>
</head>
<body>
<div class="layui-form layuimini-form">
    <div class="layui-form-item">
        <label class="layui-form-label required">start-time</label>
        <div class="layui-input-block">
            <input type="hidden" id="id" name="id">
            <input type="text" id="startTime" name="startTime"
                   lay-verify="required" lay-reqtext="start time cannot be empty"
                   placeholder="please enter the start time" value="" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label required">end time</label>
        <div class="layui-input-block">
            <input type="text" id="endTime" name="endTime" lay-verify="required" lay-reqtext="end time cannot be empty"
                   placeholder="please enter the end time" value="" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label required">book</label>
        <div class="layui-input-block">
            <input type="text"  id="book" name="book" lay-verify="required"
                   lay-reqtext="cannot be empty" placeholder="please enter" value="" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label required">key</label>
        <div class="layui-input-block">
            <input type="text"  id="key" name="key" lay-verify="required"
                   lay-reqtext="cannot be empty" placeholder="please enter" value="" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label required">cube</label>
        <div class="layui-input-block">
            <input type="text"  id="cube" name="cube" lay-verify="required"
                   lay-reqtext="cannot be empty" placeholder="please enter" value="" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <div class="layui-input-block">
            <button class="layui-btn layui-btn-normal" lay-submit lay-filter="saveBtn">confirm save</button>
        </div>
    </div>
</div>
<script src="../../lib/layui-v2.6.3/layui.js" charset="utf-8"></script>
<script>
    layui.use(['form'], function () {
        var form = layui.form,
            layer = layui.layer,
            $ = layui.$;

        //监听提交
        form.on('submit(saveBtn)', function (data) {
            let loadIndex = layer.load(1);
            $.get("${pageContext.request.contextPath}/upload", data.field, function (res) {
                layer.close(loadIndex)
                layer.msg("successfully modified")
            })
            return false;
        });

    });
</script>
</body>
</html>
