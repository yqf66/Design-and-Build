package testWeb.dao.impl;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import testWeb.dao.RobotDAO;
import testWeb.db.DBConnect;
import testWeb.vo.Image;
import testWeb.vo.Robotinfo;

public class RobotDAOImpl implements RobotDAO {
    public int addByRobotinfo(Robotinfo rbinfo) throws Exception {
        int flag1 = 0;
        int flag2 = 0;
        String sql = "select * from userinfo where userinfoid=?";
        String sqladd = "insert into robotinfo(rbname,exploreavgtime,rbtype,userinfoid) values(?,?,?,?)";
        PreparedStatement pstmt1 = null;
        PreparedStatement pstmt2 = null;
        DBConnect dbc = null;
        //数据库操作
        try {//连接数据库
            dbc = new DBConnect();
            dbc.setAutoCommit(false);
            pstmt1 = dbc.getConnection().prepareStatement(sql);
            pstmt1.setInt(1, rbinfo.getUserinfoid());
            //进行数据库查询
            ResultSet rs = pstmt1.executeQuery();
            while (rs.next()) {
                //查询出内容,与用户输入进行比较
                if (rs.getString("haverb").equals("true")) {
                    flag1 = 1;
                }
            }
            rs.close();
            pstmt1.close();
            //加入机器人
            pstmt2 = dbc.getConnection().prepareStatement(sqladd);
            pstmt2.setString(1, rbinfo.getRbname());
            pstmt2.setString(2, rbinfo.getExploreavgtime());
            pstmt2.setString(3, rbinfo.getRbtype());
            pstmt2.setInt(4, rbinfo.getUserinfoid());

            if (flag1 == 0) {
                if (pstmt2.executeUpdate() == 1) {
                    flag2 = 1;
                }
            }
            dbc.commit();
            pstmt2.close();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        } finally {
            //关闭数据库
            dbc.close();
        }
        return flag2;


    }

    @Override
    public List<Robotinfo> queryAllByRobotinfo(Integer userId) throws SQLException {
        ArrayList<Robotinfo> robotinfos = new ArrayList<>();
        DBConnect dbc = new DBConnect();
        Connection connection = dbc.getConnection();
        try (PreparedStatement preparedStatement = connection.prepareStatement("select * from robotinfo where userinfoid=?")) {
            preparedStatement.setInt(1, userId);
            ResultSet executeQuery = preparedStatement.executeQuery();
            while (executeQuery.next()) {
                int robotid = executeQuery.getInt("robotid");
                String rbname = executeQuery.getString("rbname");
                String exploreavgtime = executeQuery.getString("exploreavgtime");
                String rbtype = executeQuery.getString("rbtype");
                int userinfoid = executeQuery.getInt("userinfoid");
                Robotinfo robotinfo = new Robotinfo();
                robotinfo.setRbid(robotid);
                robotinfo.setRbname(rbname);
                robotinfo.setExploreavgtime(exploreavgtime);
                robotinfo.setRbtype(rbtype);
                robotinfo.setUserinfoid(userinfoid);
                robotinfos.add(robotinfo);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        queryExploreavgtime(robotinfos);
        return robotinfos;
    }

    private void queryExploreavgtime(ArrayList<Robotinfo> robotinfos) throws SQLException {

        DBConnect dbc = new DBConnect();
        Connection connection = dbc.getConnection();
        try (PreparedStatement preparedStatement = connection.prepareStatement("select ifnull((max(cdate)-min(cdate))/count(*),0) from imagefile where robotid =?")) {
            for (Robotinfo robotinfo1 : robotinfos) {
                preparedStatement.setInt(1, robotinfo1.getRbid());
                ResultSet executeQuery = preparedStatement.executeQuery();
                while (executeQuery.next()) {
                    String exploreavgtime = executeQuery.getString(1);
                    robotinfo1.setExploreavgtime(exploreavgtime);
                }
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            connection.close();
        }
    }

    @Override
    public void deleteByRobotinfo(String s) {
        DBConnect dbc = new DBConnect();
        Connection connection = dbc.getConnection();
        try (PreparedStatement preparedStatement = connection.prepareStatement("delete from robotinfo where robotid=?")) {
            preparedStatement.setString(1, s);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    @Override
    public void updateByRobotinfo(String rbname, String rbtype, Integer rid) {
        DBConnect dbc = new DBConnect();
        Connection connection = dbc.getConnection();
        try (PreparedStatement preparedStatement = connection.prepareStatement("update robotinfo set rbname=?,rbtype=? where robotid=?")) {
            preparedStatement.setString(1, rbname);
            preparedStatement.setString(2, rbtype);
            preparedStatement.setInt(3, rid);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<Image> exploration(int rbid) {
        DBConnect dbc = new DBConnect();
        Connection connection = dbc.getConnection();
        ArrayList<Image> images = new ArrayList<>();
        try (PreparedStatement preparedStatement = connection.prepareStatement("select * from imagefile where robotid=?")) {
            preparedStatement.setInt(1, rbid);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                Integer id = resultSet.getInt("id");
                String filename = resultSet.getString("filename");
                String absolutepath = resultSet.getString("absolutepath");
                String success = resultSet.getString("success");
                Timestamp cdate = resultSet.getTimestamp("cdate");
                String startTime = resultSet.getString("start_time");
                String endTime = resultSet.getString("end_time");
                int robotid = resultSet.getInt("robotid");
                String book = resultSet.getString("book");
                String key = resultSet.getString("key");
                String cube = resultSet.getString("cubee");
                Image image = new Image();
                image.setFilename(filename);
                image.setId(id);
                image.setAbsolutepath(absolutepath);
                image.setSuccess(success);
                image.setRobotid(robotid);
                image.setCdate(cdate.toLocalDateTime());
                image.setStartTime(startTime);
                image.setEndTime(endTime);
                image.setBook(book);
                image.setKey(key);
                image.setCube(cube);
                images.add(image);
            }
        } catch (SQLException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
        return images;
    }

    @Override
    public Map<String, Object> queryAllByRobotinfoPage(int userId, int page, int limit) throws SQLException {
        DBConnect dbc = new DBConnect();
        Connection connection = dbc.getConnection();
        HashMap<String, Object> map = new HashMap<>();

        int  start=(page-1)*limit;
        ArrayList<Robotinfo> robotinfos = new ArrayList<>();
        try {
            PreparedStatement preparedStatement = connection.prepareStatement("select count(*) from robotinfo where userinfoid=?");
            preparedStatement.setInt(1,userId);
            ResultSet executeQuery = preparedStatement.executeQuery();
            if (!executeQuery.next()) {
                return null;
            }
            int count = executeQuery.getInt(1);

            PreparedStatement query = connection.prepareStatement("select * from robotinfo where userinfoid=? limit ?,?");
            query.setInt(1,userId);
            query.setInt(2,start);
            query.setInt(3,limit);
            executeQuery = query.executeQuery();
            while (executeQuery.next()) {
                int robotid = executeQuery.getInt("robotid");
                String rbname = executeQuery.getString("rbname");
                String exploreavgtime = executeQuery.getString("exploreavgtime");
                String rbtype = executeQuery.getString("rbtype");
                int userinfoid = executeQuery.getInt("userinfoid");
                Robotinfo robotinfo = new Robotinfo();
                robotinfo.setRbid(robotid);
                robotinfo.setRbname(rbname);
                robotinfo.setExploreavgtime(exploreavgtime);
                robotinfo.setRbtype(rbtype);
                robotinfo.setUserinfoid(userinfoid);
                robotinfos.add(robotinfo);
            }
            queryExploreavgtime(robotinfos);
            map.put("data",robotinfos);
            map.put("count",count);

        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            connection.close();
        }
        return map;
    }


}
