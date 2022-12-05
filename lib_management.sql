-- MySQL dump 10.13  Distrib 5.7.32, for Win32 (AMD64)
--
-- Host: localhost    Database: lib_management
-- ------------------------------------------------------
-- Server version	5.7.32-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authorised_librarians`
--

DROP TABLE IF EXISTS `authorised_librarians`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authorised_librarians` (
  `name` varchar(30) DEFAULT NULL,
  `gender` varchar(8) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `emp_id` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authorised_librarians`
--

LOCK TABLES `authorised_librarians` WRITE;
/*!40000 ALTER TABLE `authorised_librarians` DISABLE KEYS */;
INSERT INTO `authorised_librarians` VALUES ('Tanmoy Bhuyan','Male','password','123654');
/*!40000 ALTER TABLE `authorised_librarians` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `name` varchar(100) DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `year_of_publish` varchar(30) DEFAULT NULL,
  `edition_number` varchar(30) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `book_id` varchar(30) DEFAULT NULL,
  `book_mrp` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('Harry Potter','Bloomsbury Publications','1995','1','J. K. Rowling','Not Issued','258963','750'),('Wings Of Fire','University Press','2001','1','APJ Abdul Kalam','Not Issued','125896','500'),('Harry Potter and the Goblet of Fire','Bloomsbury Productions','2004','1','J. K. Rowling','Not Issued','456322','800');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issued_books`
--

DROP TABLE IF EXISTS `issued_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issued_books` (
  `book_name` varchar(30) DEFAULT NULL,
  `book_id` varchar(30) DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `issued_to` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issued_books`
--

LOCK TABLES `issued_books` WRITE;
/*!40000 ALTER TABLE `issued_books` DISABLE KEYS */;
/*!40000 ALTER TABLE `issued_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lib_details`
--

DROP TABLE IF EXISTS `lib_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lib_details` (
  `rate` int(11) DEFAULT NULL,
  `max_days` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lib_details`
--

LOCK TABLES `lib_details` WRITE;
/*!40000 ALTER TABLE `lib_details` DISABLE KEYS */;
INSERT INTO `lib_details` VALUES (5,14);
/*!40000 ALTER TABLE `lib_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new_arrivals`
--

DROP TABLE IF EXISTS `new_arrivals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_arrivals` (
  `name` varchar(100) DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `year_of_publish` varchar(30) DEFAULT NULL,
  `edition_number` varchar(30) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `book_id` varchar(30) DEFAULT NULL,
  `book_mrp` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_arrivals`
--

LOCK TABLES `new_arrivals` WRITE;
/*!40000 ALTER TABLE `new_arrivals` DISABLE KEYS */;
/*!40000 ALTER TABLE `new_arrivals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patrons`
--

DROP TABLE IF EXISTS `patrons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patrons` (
  `name` varchar(30) DEFAULT NULL,
  `designation` varchar(20) DEFAULT NULL,
  `subscriptions` varchar(100) DEFAULT NULL,
  `gender` varchar(8) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `id` varchar(30) DEFAULT NULL,
  `edition_num` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patrons`
--

LOCK TABLES `patrons` WRITE;
/*!40000 ALTER TABLE `patrons` DISABLE KEYS */;
INSERT INTO `patrons` VALUES ('Indrajit Mandal','Student','wings of fire','Male','password','15990','1');
/*!40000 ALTER TABLE `patrons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-18 10:31:23
