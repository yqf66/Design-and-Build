package testWeb.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import testWeb.dao.*;
import testWeb.dao.impl.*;
import testWeb.vo.Userinfo;

public class UserLoginServlet extends HttpServlet {
	public void doGet(HttpServletRequest req,HttpServletResponse res) throws IOException,ServletException
	{
		doPost(req,res);
	}
	public void doPost(HttpServletRequest req,HttpServletResponse res)throws IOException,ServletException
	{
		req.setCharacterEncoding("utf-8");
		res.setContentType("text/html;charset=utf-8");
		Userinfo userinfo =new Userinfo();
		userinfo.setUsername(req.getParameter("username"));
		userinfo.setPassword(req.getParameter("password"));

		UserDAO dao = new UserDAOImpl();
		int flag =0;
		try
		{
//			flag = dao.queryByUserinfo(userinfo);

			userinfo = dao.queryByUserinfo(userinfo);
	    } catch(Exception e)
	    {
	    	e.printStackTrace();
	    }
	    if(userinfo!=null)
	    {
	    	HttpSession session = req.getSession();
	    	session.setAttribute("username",userinfo.getUsername());
			session.setAttribute("userId",userinfo.getUserinfoid());
			System.out.println(userinfo.getUserinfoid());
			if ("json".equals(req.getParameter("type"))) {
				res.setContentType("text/json;charset=utf-8");
				res.getWriter().write("{\"code\":0}");
				return;
			}
	    	res.sendRedirect("./welcome.jsp");
	    }else
	    {
			if ("json".equals(req.getParameter("type"))) {
				res.setContentType("text/json;charset=utf-8");
				res.getWriter().write("{\"code\":-1,\"msg\":\"incorrect username or password\"}");
				return;
			}
	    	res.sendRedirect("./error.jsp");
	    }
}
}
