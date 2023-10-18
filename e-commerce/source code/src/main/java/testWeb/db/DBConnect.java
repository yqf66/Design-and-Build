package testWeb.db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnect {
		private final String DBDRIVER ="com.mysql.cj.jdbc.Driver";
		private final String DBURL    =	"jdbc:mysql://localhost:3306/javawebdb?useSSL=false&useUnicode=true&characterEncoding=UTF-8&allowPublicKeyRetrieval=true";
		private final String DBUSER   ="root";
		private final String DBPASSWORD = "root";
		private Connection conn = null;

		public DBConnect()
		{
			try
			{
				Class.forName(DBDRIVER);
				this.conn = DriverManager.getConnection(DBURL, DBUSER, DBPASSWORD);
				System.out.println(this.conn);
			}catch(Exception e)
			{
				System.out.println(e.getMessage());
			}
		}


		//提交
		public void commit() throws Exception
		{
			conn.commit();
		}
		//取得数据库链接
		public Connection getConnection()
		{
			return this.conn;
		}
		//关闭数据库链接
		public void close()
		{
			try
			{
				this.conn.close();
			}catch(Exception e) {}
		}
		//取消自动提交
		public void setAutoCommit(boolean a) throws SQLException {
			// TODO Auto-generated method stub
			conn.setAutoCommit(a);
		}
}
