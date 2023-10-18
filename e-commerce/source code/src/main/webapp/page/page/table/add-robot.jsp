<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>add</title>
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
        <label class="layui-form-label required">rbname</label>
        <div class="layui-input-block">
            <input type="text" name="Rbname" lay-verify="required" lay-reqtext="rbname cannot be empty" placeholder="please enter rbname" value="" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label required">rbtype</label>
        <div class="layui-input-block">
            <input type="text" name="Rbtype" lay-verify="required" lay-reqtext="rbtype cannot be empty" placeholder="please enter rbtype" value="" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label required">userinfoid</label>
        <div class="layui-input-block">
            <input type="number" name="userinfoid" lay-verify="required" lay-reqtext="userinfoid cannot be empty" placeholder="please enter userinfoid" value="" class="layui-input">
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
    layui.use(['form',"jquery"], function () {
        var form = layui.form,
            layer = layui.layer,
            $ = layui.jquery;

        //监听提交
        form.on('submit(saveBtn)', function (data) {

            layer.load(1);
            $.post("${pageContext.request.contextPath}/robot?type=json",data.field,function (res) {
                layer.closeAll('loading');
                if (res.code===0){
                    layer.msg("successfully added",{time:1000,icon:1},function () {
                        var iframeIndex = parent.layer.getFrameIndex(window.name);
                        parent.layui.table.reload('currentTableId', {
                            page: {
                                curr: 1
                            },
                        }, 'data');
                        parent.layer.close(iframeIndex);
                    })
                }
            },"json")
            return false;
        });

    });
</script>
</body>
</html>
