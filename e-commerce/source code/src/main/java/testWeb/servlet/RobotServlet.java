package testWeb.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import testWeb.dao.RobotDAO;
import testWeb.dao.impl.RobotDAOImpl;
import testWeb.dao.UserDAO;
import testWeb.dao.impl.UserDAOImpl;
import testWeb.vo.Robotinfo;
import testWeb.vo.Userinfo;

public class RobotServlet extends HttpServlet {
	public void doGet(HttpServletRequest req,HttpServletResponse res) throws IOException,ServletException
	{

	}
	public void doPost(HttpServletRequest req,HttpServletResponse res)throws IOException,ServletException
	{
		Robotinfo rbinfo =new Robotinfo();
		rbinfo.setRbname(req.getParameter("Rbname"));
		rbinfo.setExploreavgtime(req.getParameter("Exploreavgtime"));
		rbinfo.setRbtype(req.getParameter("Rbtype"));
		rbinfo.setUserinfoid(Integer.parseInt(req.getParameter("userinfoid")));



		RobotDAO dao = new RobotDAOImpl();
		int flag =0;
		try
		{
			flag = dao.addByRobotinfo(rbinfo);
	    } catch(Exception e)
	    {
	    	e.printStackTrace();
	    }
	    if(flag==1)
	    {
	    	HttpSession session = req.getSession();
	    	session.setAttribute("Rbname",rbinfo.getRbname());
	    	session.setAttribute("Exploreavgtime",rbinfo.getExploreavgtime());
	    	session.setAttribute("Rbtype",rbinfo.getRbtype());
	    	session.setAttribute("userinfoid",rbinfo.getUserinfoid());
	    	if ("json".equals(req.getParameter("type"))){
				res.setContentType("application/json;charset=utf-8");
				res.getWriter().write("{\"code\":0,\"msg\":\"success\"}");
				return;
			}
	    	res.sendRedirect("./nextadd.jsp");
	    }else
	    {
	    	res.sendRedirect("./error.jsp");
	    }
}
}


