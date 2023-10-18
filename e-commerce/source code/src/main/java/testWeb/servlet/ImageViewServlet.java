package testWeb.servlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ImageViewServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String name = req.getParameter("name");
        resp.setContentType("image/jpeg");
        resp.setHeader("Content-Disposition", "attachment; filename=" + name);
        String path = "C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\" + name;
        byte[] bytes = Files.readAllBytes(Paths.get(path));
        resp.getOutputStream().write(bytes);
    }
}
