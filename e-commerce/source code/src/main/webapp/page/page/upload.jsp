<%@ page contentType="text/html;charset=UTF-8" language="java" %>
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

<form class="layui-form" id="form" style="width: 500px" action="">
    <div class="layui-form-item">
        <label class="layui-form-label">robot id</label>
        <div class="layui-input-block">
            <input type="text" name="robotid" required lay-verify="required" placeholder="please enter the robot id"
                   autocomplete="off" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label"></label>
        <div class="layui-input-block">
            <input type="button" id="start" value="start exploring" autocomplete="off" class="layui-btn">
            <input type="button" id="end" value="end exploration" autocomplete="off" class="layui-btn">
        </div>
    </div>
    <div class="layui-form-item">
        <label class="layui-form-label">upload images</label>
        <div class="layui-input-inline">
            <button type="button" class="layui-btn" id="test1">
                <i class="layui-icon">&#xe67c;</i>
            </button>
            <span id="fileName"></span>
        </div>
    </div>
    <div class="layui-form-item">
        <div class="layui-input-block">
            <button class="layui-btn" lay-submit lay-filter="formDemo">submit</button>
            <button type="reset" class="layui-btn layui-btn-primary">reset</button>
        </div>
    </div>
</form>

<script src="../lib/layui-v2.6.3/layui.js" charset="utf-8"></script>
<script>
    layui.use(['form', 'jquery','layer','upload'], function () {
        let form = layui.form;
        let $ = layui.jquery;
        let layer = layui.layer;
        let upload = layui.upload;

        let startTime=null;
        let endTime =null;
        let fileVal = null;

        $("#start").click(function () {
            let date = new Date();
            startTime = date.getTime();
            layer.msg("start exploring");
        })
        $("#end").click(function () {
            if (startTime==null){
                layer.msg("please start exploring first");
                return;
            }
            let date = new Date();
            endTime = date.getTime();
            layer.msg("end exploration");
        })


        form.on('submit(formDemo)', function (data) {
            if (startTime==null || endTime==null){
                layer.msg("please complete the exploration");
                return false;
            }
            if (fileVal==null){
                layer.msg("please upload pictures");
                return false;
            }
            if (data.field.robotid==null || data.field.robotid==""){
                layer.msg("please enter the robot id");
                return false;
            }
            if (startTime>endTime){
                layer.msg("The start time cannot be greater than the end time, please explore again");
                startTime = null;
                endTime = null;
                return false;
            }
            let formData = new FormData();
            formData.append("startTime",startTime);
            formData.append("endTime",endTime);
            formData.append("file",fileVal);
            formData.append("robotid",data.field.robotid);
            layer.load(1);
            $.ajax({
                url: "${pageContext.request.contextPath}/upload",
                type: "post",
                data: formData,
                processData: false,
                // FormData时jq会自动改变类型，我们不允许
                contentType: false,
                success: function (res) {
                    layer.closeAll('loading');
                    layer.msg("successfully added",{time:1500,icon:1})
                },
                error: function (res) {
                    layer.closeAll('loading');
                    layer.msg("add failed",{time:1500,icon:2})
                }
            })
            return false;
        });



        //执行实例
        var uploadInst = upload.render({
            elem: '#test1', //上传接口
            auto: false,
            choose: function(obj){
                //上传完毕回调
                var files = obj.pushFile();
                let input = $("input[type='file']");
                $("#fileName").text(input.val());

                obj.preview(function(index, file, result){
                    console.log(index); //得到文件索引
                    console.log(file); //得到文件对象
                    console.log(result); //得到文件base64编码，比如图片
                    fileVal = file;
                });

            },error: function(){
                //请求异常回调
            }
        });
    });
</script>
</body>
</html>
