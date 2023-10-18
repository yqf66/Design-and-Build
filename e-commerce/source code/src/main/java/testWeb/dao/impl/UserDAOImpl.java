package testWeb.dao.impl;


import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import testWeb.dao.UserDAO;
import testWeb.db.DBConnect;
import testWeb.vo.Userinfo;

public class UserDAOImpl implements UserDAO {

	@Override
	public Userinfo queryByUserinfo(Userinfo userinfo) throws Exception {

		int flag =0;
		Userinfo user = null;
		String sql ="select * from userinfo where username=?";
		PreparedStatement pstmt = null;
		DBConnect dbc =null;
		//下面是数据库具体操作
		try
		{
			//连接数据库
			dbc =new DBConnect();
			pstmt = dbc.getConnection().prepareStatement(sql);
			pstmt.setString(1, userinfo.getUsername());
			//进行数据库查询
			ResultSet rs =pstmt.executeQuery();
			while(rs.next())
			{
				//查询出内容,与用户输入进行比较
				if(rs.getString("password").equals(userinfo.getPassword()))
				{
					user = new Userinfo();
					user.setUserinfoid(rs.getInt("userinfoid"));
					user.setUsername(rs.getString("username"));
					flag =1;
				}
			}
			rs.close();
			pstmt.close();
		}catch(SQLException e)
		{
			System.out.println(e.getMessage());
		}finally
		{
			//关闭数据库
			dbc.close();
		}
		return user;
	}

	public int registerByUserinfo(Userinfo userinfo)throws Exception
	{
		int flag1 =1;
		int flag2 =0;
		//查询
		String sqlcheck ="select * from userinfo ";
		String sql ="insert into userinfo(username,password,haverb) values(?,?,?)";
		PreparedStatement pstmt1 = null;
		PreparedStatement pstmt2 = null;
		DBConnect dbc =null;
		//下面是数据库具体操作
		try
		{
			//连接数据库
			dbc =new DBConnect();
			dbc.setAutoCommit(false);
			pstmt1 = dbc.getConnection().prepareStatement(sqlcheck);
			ResultSet rs =pstmt1.executeQuery();
			while(rs.next())
			{
				//查询出内容,与用户输入进行比较
				if(rs.getString("username").equals(userinfo.getUsername()))
				{
					flag1 =0;
				}
			}
			rs.close();
			pstmt1.close();

			pstmt2 = dbc.getConnection().prepareStatement(sql);
			pstmt2.setString(1, userinfo.getUsername());
			pstmt2.setString(2, userinfo.getPassword());
			pstmt2.setString(3,"false");


			if(flag1==1&&!userinfo.getPassword().equals(null)&&!userinfo.getUsername().equals(null))
			{
				if(pstmt2.executeUpdate()==1)
				{
					flag2 =1;
				}
			}
			dbc.commit();
			pstmt2.close();
		}catch(SQLException e)
		{
			System.out.println(e.getMessage());
		}finally
		{
			//关闭数据库
			dbc.close();
		}
		return flag2;

	}

	@Override
	public int deleteUser(Userinfo userinfo) throws Exception {
		String sql = "delete from userinfo where username=?";
		PreparedStatement pstmt = null ;
		DBConnect dbc = null;
		try{
			//连接数据库
			dbc = new DBConnect() ;
			pstmt = dbc.getConnection().prepareStatement(sql) ;
			pstmt.setString(1,userinfo.getUsername()) ;
			//进行数据库更新操作
			return pstmt.executeUpdate();
		}catch (SQLException e){
			System.out.println(e.getMessage());
		}finally{
			// 关闭数据库连接
			if(dbc != null){
				dbc.close();
			}
			if(pstmt != null){
				pstmt.close();
			}
		}
		return 0;
	}

	@Override
	public Userinfo queryByUser(Userinfo userinfo) throws Exception {

		String sql = "select * from userinfo where username=?";
		PreparedStatement pstmt = null ;
		DBConnect dbc = null;
		ResultSet rs = null;
		try{
			//连接数据库
			dbc = new DBConnect() ;
			pstmt = dbc.getConnection().prepareStatement(sql) ;
			pstmt.setString(1,userinfo.getUsername()) ;
			// 进行数据库查询操作
			rs = pstmt.executeQuery();
			while(rs.next()){
				Userinfo user = new Userinfo();
				user.setUsername(rs.getString("username"));
				return user;
			}
		}catch (SQLException e){
			System.out.println(e.getMessage());
		}finally{
			// 关闭数据库连接
			if(dbc != null){
				dbc.close();
			}
			if(rs != null){
				rs.close();
			}
			if(pstmt != null){
				pstmt.close();
			}
		}
		return null;
	}
}
