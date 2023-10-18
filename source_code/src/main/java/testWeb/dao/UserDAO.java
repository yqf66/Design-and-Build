package testWeb.dao;

import testWeb.vo.Userinfo;

public interface UserDAO {
		public Userinfo queryByUserinfo(Userinfo userinfo) throws Exception;
		public int registerByUserinfo(Userinfo userinfo)throws Exception;
		Userinfo queryByUser(Userinfo userinfo) throws Exception;
    	int deleteUser(Userinfo userinfo) throws Exception;
}
