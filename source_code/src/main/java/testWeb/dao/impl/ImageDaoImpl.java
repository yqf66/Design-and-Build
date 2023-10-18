package testWeb.dao.impl;

import testWeb.dao.ImageDao;
import testWeb.db.DBConnect;
import testWeb.vo.Image;

import java.sql.Connection;
import java.sql.PreparedStatement;

public class ImageDaoImpl implements ImageDao {
    @Override
    public Image upload(Image image) {
        DBConnect dbConnect = new DBConnect();
        String sql = "insert into imagefile(filename, absolutepath, cdate,robotid,start_time,end_time,book,`key`,cubee) values(?, ?, ?,?,?,?,?,?,?)";
        try (Connection connection = dbConnect.getConnection();
             PreparedStatement preparedStatement =  connection.prepareStatement(sql)){
            preparedStatement.setString(1, image.getFilename());
            preparedStatement.setString(2, image.getAbsolutepath());
            preparedStatement.setObject(3, image.getCdate());
            preparedStatement.setInt(4,image.getRobotid());
            preparedStatement.setString(5,image.getStartTime());
            preparedStatement.setString(6,image.getEndTime());
            preparedStatement.setString(7,image.getBook());
            preparedStatement.setString(8,image.getKey());
            preparedStatement.setString(9,image.getCube());
            preparedStatement.execute();
            return image;
        }catch (Exception e){
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public void updateById(Image image) {
        DBConnect dbConnect = new DBConnect();
        String sql = "update  imagefile set success=?,start_time=?,end_time=?,book=?,`key`=?,cubee=? where id=?";
        try (Connection connection = dbConnect.getConnection();
             PreparedStatement preparedStatement =  connection.prepareStatement(sql)){
            preparedStatement.setString(1, image.getSuccess());
            preparedStatement.setString(2, image.getStartTime());
            preparedStatement.setString(3, image.getEndTime());
            preparedStatement.setString(4,image.getBook());
            preparedStatement.setString(5,image.getKey());
            preparedStatement.setString(6,image.getCube());
            preparedStatement.setInt(7,image.getId());
            preparedStatement.executeUpdate();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
