package testWeb.servlet;

import testWeb.dao.UserDAO;
import testWeb.dao.impl.UserDAOImpl;
import testWeb.vo.Userinfo;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

public class DeleteUserServlet extends HttpServlet {

    public void doGet(HttpServletRequest req, HttpServletResponse res)
            throws IOException, ServletException {
    }

    public void doPost(HttpServletRequest req, HttpServletResponse res)
            throws IOException, ServletException {
        Userinfo userinfo = new Userinfo();
        userinfo.setUsername(req.getParameter("username"));

        UserDAO dao = new UserDAOImpl();
        try {
            Userinfo userInfo = dao.queryByUser(userinfo);
            HttpSession session = req.getSession();
            if(userInfo == null){
                session.setAttribute("msg", "username not found");
                res.sendRedirect("./deleteuser.jsp");
            }else {
                dao.deleteUser(userinfo);
                session.setAttribute("msg", "delete success");
                res.sendRedirect("./deleteuser.jsp");
            }
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }

}
