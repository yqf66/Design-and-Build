package testWeb.dao;

import testWeb.vo.Image;
import testWeb.vo.Robotinfo;

import java.sql.SQLException;
import java.util.List;
import java.util.Map;

public interface RobotDAO {
		public int  addByRobotinfo(Robotinfo rbinfo) throws Exception;
		List<Robotinfo> queryAllByRobotinfo(Integer userId) throws SQLException;
		void deleteByRobotinfo(String s);
		void updateByRobotinfo(String rbname, String rbtype,Integer rid);
		List<Image> exploration(int rbid);
		Map<String, Object> queryAllByRobotinfoPage(int userId, int i, int parseInt) throws SQLException;
}
