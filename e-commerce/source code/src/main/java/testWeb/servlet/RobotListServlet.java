package testWeb.servlet;

import com.alibaba.fastjson.JSON;
import testWeb.dao.RobotDAO;
import testWeb.dao.impl.RobotDAOImpl;
import testWeb.vo.Image;
import testWeb.vo.Robotinfo;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

public class RobotListServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String method = req.getParameter("method");
        HttpSession session = req.getSession();
        Object userId = session.getAttribute("userId");
        RobotDAO dao = new RobotDAOImpl();
        if (method.equals("toRobotListView")) {
            List<Robotinfo> robotinfos = null;
            try {
                robotinfos = dao.queryAllByRobotinfo((int) userId);
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
            req.setAttribute("robotinfos", robotinfos);
            req.getRequestDispatcher("robot-list.jsp").forward(req, resp);
        } else if (method.equals("toAddRobotView")) {
            resp.sendRedirect(req.getContextPath() + "/robot.jsp");
        } else if (method.equals("toUpdateRobotView")) {
            String rid = req.getParameter("rid");
            String rbname = req.getParameter("rbname");
            String exploreavgtime = req.getParameter("exploreavgtime");
            String rbtype = req.getParameter("rbtype");
            String userinfoid = req.getParameter("userinfoid");
            Robotinfo robotinfo = new Robotinfo();
            robotinfo.setRbid(Integer.parseInt(rid));
            robotinfo.setRbname(rbname);
            robotinfo.setExploreavgtime(exploreavgtime);
            robotinfo.setRbtype(rbtype);
            robotinfo.setUserinfoid(Integer.parseInt(userinfoid));
            session.setAttribute("robo", robotinfo);
            resp.sendRedirect(req.getContextPath() + "/robot-update.jsp");
        } else if (method.equals("updateRobot")) {
            dao.updateByRobotinfo(req.getParameter("rbname"),
                    req.getParameter("rbtype"),
                    Integer.parseInt(req.getParameter("rid")));
            if (!"json".equals(req.getParameter("type"))){
                resp.sendRedirect(req.getContextPath() + "/robotList?method=toRobotListView");
            }else {
                resp.getWriter().write("success");
            }
        } else if (method.equals("deleteRobot")) {
            String rid = req.getParameter("rid");
            dao.deleteByRobotinfo(rid);
            resp.sendRedirect(req.getContextPath() + "/robotList?method=toRobotListView");
        }else if (method.equals("exploration")){
            List<Image> list  =  dao.exploration(Integer.parseInt(req.getParameter("rbid")));
            session.setAttribute("list",list);
//            req.getRequestDispatcher("robot-exploration.jsp").forward(req, resp);
            resp.sendRedirect(req.getContextPath() + "/page/page/exploration.jsp");
        }else if (method.equals("robtListJson")){
            resp.setContentType("application/json;charset=utf-8");
            String page = req.getParameter("page");
            String limit = req.getParameter("limit");
            Map<String,Object> robotinfos = null;
            try {
                robotinfos = dao.queryAllByRobotinfoPage((int) userId,Integer.parseInt(page),Integer.parseInt(limit));
                robotinfos.put("code",0);
                robotinfos.put("msg","success");
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
            JSON.writeJSONString(resp.getWriter(),robotinfos);
        }
    }
}
