package testWeb.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import testWeb.dao.UserDAO;
import testWeb.dao.impl.UserDAOImpl;
import testWeb.vo.Userinfo;

public class UserRegisterServlet extends HttpServlet
{

		public void doGet(HttpServletRequest req,HttpServletResponse res) throws IOException,ServletException
		{
			doPost(req,res);
		}
		public void doPost(HttpServletRequest req,HttpServletResponse res)throws IOException,ServletException
		{
			Userinfo userinfo =new Userinfo();
			userinfo.setUsername(req.getParameter("username"));
			userinfo.setPassword(req.getParameter("password"));

			UserDAO dao = new UserDAOImpl();
			int flag =0;
			try
			{
				flag = dao.registerByUserinfo(userinfo);
		    } catch(Exception e)
		    {
		    	e.printStackTrace();
		    }
		    if(flag==1)
		    {
		    	HttpSession session = req.getSession();
		    	session.setAttribute("username",userinfo.getUsername());
				session.setAttribute("userId",userinfo.getUserinfoid());
				if ("json".equals(req.getParameter("type"))) {
					res.setContentType("text/json;charset=utf-8");
					res.getWriter().write("{\"code\":0}");
					return;
				}
		    	res.sendRedirect("./welcome1.jsp");
		    }else
		    {
				if ("json".equals(req.getParameter("type"))) {
					res.setContentType("text/json;charset=utf-8");
					res.getWriter().write("{\"code\":-1,\"msg\":\"login has failed\"}");
					return;
				}
		    	res.sendRedirect("./error1.jsp");
		    }
	}
}

