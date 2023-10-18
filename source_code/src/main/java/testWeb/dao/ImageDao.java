package testWeb.dao;

import testWeb.vo.Image;

    public interface ImageDao {
        Image upload(Image image);
        void updateById(Image image);
    }
