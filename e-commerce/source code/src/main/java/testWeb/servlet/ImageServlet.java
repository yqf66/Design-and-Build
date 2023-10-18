package testWeb.servlet;

import testWeb.dao.ImageDao;
import testWeb.dao.impl.ImageDaoImpl;
import testWeb.vo.Image;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.util.Date;


@WebServlet("/UploadServlet")
@MultipartConfig
public class ImageServlet  extends HttpServlet {
    SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取上传的文件
        Part filePart = request.getPart("file");// 文件 name 名称为file
        String fileName = filePart.getSubmittedFileName();
        String robotid = request.getParameter("robotid"); //机器人id
        String success = request.getParameter("success"); // 是否探索到
        String startTime = request.getParameter("startTime");// 开始时间 格式  2023-10-06 21:39:29
        String endTime = request.getParameter("endTime");//结束时间  格式 2023-10-06 21:39:29
        String key = request.getParameter("key");
        String book = request.getParameter("book");
        String cube = request.getParameter("cube");


        // 毫秒转日期
        if (startTime !=null && endTime!=null){
            Date dateS = new Date(Long.parseLong(startTime));
            Date dateE = new Date(Long.parseLong(endTime));
            startTime =simpleDateFormat.format(dateS);
            endTime =simpleDateFormat.format(dateE);
        }



        // 指定上传的目录
        String uploadDir = "C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file";
        File uploadDirFile = new File(uploadDir);
        if (!uploadDirFile.exists()) {
            uploadDirFile.mkdirs();
        }

        // 将文件保存到服务器
        String name= System.currentTimeMillis() + fileName.substring(fileName.lastIndexOf("."));
        String filePath = uploadDir + File.separator +  name;
        filePart.write(filePath);

        // 将文件信息保存到数据库
        ImageDaoImpl imageDao = new ImageDaoImpl();
        Image image = new Image();
        image.setAbsolutepath(filePath);
        image.setFilename(name);
        image.setRobotid(Integer.parseInt(robotid));
        image.setCdate(LocalDateTime.now());
        image.setSuccess(success);
        image.setStartTime(startTime);
        image.setEndTime(endTime);
        image.setKey(key);
        image.setBook(book);
        image.setCube(cube);
        imageDao.upload(image);

        // 返回上传成功的信息给客户端
        response.getWriter().println("upload success！");
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String id = req.getParameter("id");
        String startTime = req.getParameter("startTime");
        String endTime = req.getParameter("endTime");
        String success = req.getParameter("success");
        String book = req.getParameter("book");
        String key = req.getParameter("key");
        String cube = req.getParameter("cube");


        ImageDao imageDao = new ImageDaoImpl();
        Image image = new Image();
        image.setId(Integer.parseInt(id));
        image.setStartTime(startTime);
        image.setEndTime(endTime);
        image.setSuccess(success);
        image.setKey(key);
        image.setBook(book);
        image.setCube(cube);
        imageDao.updateById(image);
        resp.getWriter().println(200);
    }
}
