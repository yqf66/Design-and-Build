-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: javawebdb
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `imagefile`
--

DROP TABLE IF EXISTS `imagefile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imagefile` (
  `filename` varchar(200) DEFAULT NULL,
  `absolutepath` varchar(200) DEFAULT NULL COMMENT '绝对路径',
  `cdate` datetime DEFAULT NULL COMMENT '上传时间',
  `robotid` int DEFAULT NULL COMMENT '机器人id',
  `success` varchar(10) DEFAULT '否' COMMENT '是否发现宝藏',
  `start_time` varchar(30) DEFAULT NULL,
  `end_time` varchar(30) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `book` varchar(45) DEFAULT NULL,
  `key` varchar(45) DEFAULT NULL,
  `cubee` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagefile`
--

LOCK TABLES `imagefile` WRITE;
/*!40000 ALTER TABLE `imagefile` DISABLE KEYS */;
INSERT INTO `imagefile` VALUES ('1695987042670.png','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1695987042670.png','2023-09-29 19:30:43',1,'否',NULL,NULL,1,NULL,NULL,NULL),('1695987153298.png','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1695987153298.png','2023-09-29 19:32:33',1,'否',NULL,NULL,2,NULL,NULL,NULL),('1696246845350.png','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696246845350.png','2023-10-02 19:40:45',16,NULL,'2023-10-06 21:39:29','2023-10-11 02:10:20',3,'1','2','3'),('1696599598595.png','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696599598595.png','2023-10-06 21:39:59',1,'是','2023-10-06 21:39:29','2023-10-06 21:39:29',4,NULL,NULL,NULL),('1696607335418.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696607335418.jpg','2023-10-06 23:48:55',1,'否','2023-10-06 23:48:48','2023-10-06 23:48:48',5,NULL,NULL,NULL),('1696607439151.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696607439151.jpg','2023-10-06 23:50:39',1,'否','2023-10-06 23:50:31','2023-10-06 23:50:37',6,NULL,NULL,NULL),('1696607674337.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696607674337.jpg','2023-10-06 23:54:34',15,'否','2023-10-06 23:54:22','2023-10-06 23:54:33',7,NULL,NULL,NULL),('1696955609522.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696955609522.jpg','2023-10-11 00:33:30',1,'否','2023-10-11 00:33:23','2023-10-11 00:33:26',8,NULL,NULL,NULL),('1696955853610.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696955853610.jpg','2023-10-11 00:37:34',1,'否','2023-10-11 00:37:23','2023-10-11 00:37:28',9,NULL,NULL,NULL),('1696960625651.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696960625651.jpg','2023-10-11 01:57:06',1,'否','2023-10-11 01:57:01','2023-10-11 01:57:02',10,NULL,NULL,NULL),('1696960679246.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696960679246.jpg','2023-10-11 01:57:59',1,NULL,'2023-10-11 01:57:54','2023-10-11 01:57:56',11,'1','2','3'),('1696961437354.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696961437354.jpg','2023-10-11 02:10:37',1,NULL,'2023-10-11 02:10:09','2023-10-11 02:10:20',12,'325','333','262'),('1696992753087.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696992753087.jpg','2023-10-11 10:52:33',1,'否','2023-10-11 10:52:26','2023-10-11 10:52:27',13,NULL,NULL,NULL),('1696992762768.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1696992762768.jpg','2023-10-11 10:52:43',1,'否','2023-10-11 10:52:26','2023-10-11 10:52:27',14,NULL,NULL,NULL),('1697009736334.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1697009736334.jpg','2023-10-11 15:35:36',1,NULL,'2023-10-11 15:35:27','2023-10-11 15:35:35',15,'1','2','3'),('1697479976423.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1697479976423.jpg','2023-10-17 02:12:56',1,'否','2023-10-17 02:12:44','2023-10-17 02:12:55',16,NULL,NULL,NULL),('1697480064039.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1697480064039.jpg','2023-10-17 02:14:24',16,'否','2023-10-17 02:14:09','2023-10-17 02:14:22',17,NULL,NULL,NULL),('1697480135334.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1697480135334.jpg','2023-10-17 02:15:35',17,NULL,'2023-10-17 02:15:28','2023-10-17 02:15:34',18,'1','2','3'),('1697480247117.jpg','C:\\Users\\ASUS\\Desktop\\29-2021212985-林炫宇\\file\\1697480247117.jpg','2023-10-17 02:17:27',17,NULL,'2023-10-17 02:17:18','2023-10-17 02:17:26',19,'1','2','3');
/*!40000 ALTER TABLE `imagefile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `robotinfo`
--

DROP TABLE IF EXISTS `robotinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `robotinfo` (
  `robotid` int NOT NULL AUTO_INCREMENT,
  `rbname` varchar(45) DEFAULT NULL,
  `exploreavgtime` varchar(45) DEFAULT NULL,
  `rbtype` varchar(45) DEFAULT NULL,
  `userinfoid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`robotid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `robotinfo`
--

LOCK TABLES `robotinfo` WRITE;
/*!40000 ALTER TABLE `robotinfo` DISABLE KEYS */;
INSERT INTO `robotinfo` VALUES (1,'cs111222','1244','bbb','1'),(9,'zz12','13','zz','1'),(12,'1',NULL,'1','8'),(13,'1',NULL,'1','9'),(15,'1',NULL,'1','1'),(16,'testweb',NULL,'carbot','1'),(17,'testrobot',NULL,'car','12');
/*!40000 ALTER TABLE `robotinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userinfo` (
  `userinfoid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `haverb` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`userinfoid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES (1,'tom','123','flase'),(9,'admin','123456','false'),(10,'admin1','123456','false'),(11,'henry','123456','false'),(12,'linxuanyu','qwerty738738','false');
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'javawebdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-17  2:46:25
