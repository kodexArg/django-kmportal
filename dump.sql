-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: 172.18.0.2    Database: km1151
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$cJFIl5K8M3MUE1Gr6Ap8yd$aTXPCF5cZ0T3iiTCh5xKuEMqzm4dAWsClrkHP5zbyMI=','2023-05-31 02:23:07.169978',1,'admin','','','a@a.com',1,1,'2023-05-16 05:01:54.956913'),(5,'!wycLyxVlThUsWmfBvVOCsxAQKJkYXc7jSR3UbqxW','2023-05-17 01:56:45.673668',0,'andy','Andy','Cavedal','',0,1,'2023-05-17 01:56:45.631378'),(6,'!AcOj9rrp8jfrCje70T0nyViijbYp5Xif1hVP00Gc','2023-06-04 15:47:55.720726',0,'javier','Javier','Cavedal','',0,1,'2023-05-17 02:24:28.598052'),(10,'!awEET5Yf3h8h6PdiOfpjAUZdX8qg7IDXn2ERTFgr','2023-06-17 15:16:29.148143',0,'gabriel','Gabriel','','',0,1,'2023-05-25 23:56:03.225969'),(12,'!c4CiPr1iumN7krg2zPoYbzHWhq18sARMzzO4jbfH','2023-06-01 16:02:51.681246',0,'cintia','Cintia','Visaguirre','',0,1,'2023-06-01 16:02:51.640061'),(13,'!IDQFuaBoHrjMFAt8GeBJOEMBjRKdg4546Zfn5MnC','2023-06-01 16:12:57.934250',0,'gabi','Gabi','Manrique','',0,1,'2023-06-01 16:12:57.899677'),(14,'!CyfJLEZcREQmCTZt1F6YDhtBXRu91vZPstYrODos','2023-06-21 13:26:26.310161',0,'jere','Jere','Ezquerro','',0,1,'2023-06-01 16:13:15.254651'),(15,'!bNhxLIEalTOTazF5NQbQbvccfixB3v2QhnSxMOdQ','2023-06-21 02:20:48.384756',0,'luis','Luis','Astudillo','',0,1,'2023-06-01 16:24:13.880273'),(16,'!nMAfvnPVh7QND5gqC5SuLtis7sE8eR3JC9DVAfBa','2023-06-02 00:57:44.609582',0,'alcides_norman','Alcides Norman','Pessina','',0,1,'2023-06-02 00:57:44.573227'),(17,'!DGLJVYrLDv7UHRq6e2T7XzPgdFHVrkMX98mKWNlr','2023-06-02 17:12:31.204597',0,'natalia','Natalia','Cornejo','',0,1,'2023-06-02 12:16:08.473776'),(18,'pbkdf2_sha256$600000$yfAMsIWCxTztW5OZOVUR6a$5yFIhU5GE5NdVHgXxTl/e63G1RH2R6IYXKODTk/vPw4=','2023-06-23 13:45:00.732492',1,'administrator','','','gcavedal@gmail.com',1,1,'2023-06-02 23:54:00.288717'),(19,'!Juwnx6iaRukLe4hjCl6lWPjkIeNoSlX9BIqOvQBV','2023-06-14 04:14:07.420909',0,'emiliano','Emiliano','Costabile','',0,1,'2023-06-14 04:11:57.615507'),(20,'!of6yoeofPZIn3WU9wtufzvH6pEPnl3budd5kJDEg','2023-06-21 01:47:04.054850',0,'vanesa','Vanesa','Bourges','',0,1,'2023-06-16 02:28:36.076198'),(33,'!41ewUjRBuB9d8cm8oSc6Vl6WM986sgFwVrXLcFZt','2023-06-21 00:10:22.546355',0,'kodex','Kodex','Nigrae','',0,1,'2023-06-17 16:19:47.257856'),(34,'!2WO96yjn4SLliCIgUO3l79rtF9RDQDBhkOLWa9Mf','2023-06-19 03:00:14.553185',0,'pykodex','PyKodex','Br','',0,1,'2023-06-17 16:23:38.987708'),(35,'!EsKjnao046JXEQKbpiWofVDooubeoeCjVScxnfUx','2023-06-21 23:03:56.948080',0,'kodex5','Kodex','','',0,1,'2023-06-17 16:36:00.272514'),(36,'!6oGFWeokmkfnELSTF6HNdh7jtLhFE2RWR36lRrHN','2023-06-21 17:25:24.101411',0,'roger','Roger','Pustavrh','',0,1,'2023-06-21 17:25:24.060394');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialapp`
--

DROP TABLE IF EXISTS `socialaccount_socialapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialapp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp`
--

LOCK TABLES `socialaccount_socialapp` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp` DISABLE KEYS */;
INSERT INTO `socialaccount_socialapp` VALUES (1,'google','Google','271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com','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','');
/*!40000 ALTER TABLE `socialaccount_socialapp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialapp_sites`
--

DROP TABLE IF EXISTS `socialaccount_socialapp_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialapp_sites` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `socialapp_id` int NOT NULL,
  `site_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`),
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp_sites`
--

LOCK TABLES `socialaccount_socialapp_sites` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` DISABLE KEYS */;
INSERT INTO `socialaccount_socialapp_sites` VALUES (1,1,3);
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialaccount`
--

DROP TABLE IF EXISTS `socialaccount_socialaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialaccount` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialaccount`
--

LOCK TABLES `socialaccount_socialaccount` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialaccount` DISABLE KEYS */;
INSERT INTO `socialaccount_socialaccount` VALUES (3,'google','100051425376529298346','2023-05-17 01:56:45.646002','2023-05-17 01:56:45.646073','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"100051425376529298346\", \"at_hash\": \"eUGvZVZ1rMAJ-5kAXSGB3g\", \"name\": \"Andy Cavedal\", \"picture\": \"https://lh3.googleusercontent.com/a/AGNmyxbNT6_wYjE_CfwJcWzVOXTt3AzU80wz0W9A5cYI_w=s96-c\", \"given_name\": \"Andy\", \"family_name\": \"Cavedal\", \"locale\": \"es\", \"iat\": 1684288605, \"exp\": 1684292205}',5),(4,'google','118117857814537042606','2023-06-04 15:47:55.695762','2023-05-17 02:24:28.612478','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"118117857814537042606\", \"at_hash\": \"KEOjwvDCVqQHTW8P3EOejw\", \"name\": \"Javier Cavedal\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtdkV1A_6s19Z-Yu2ZvxS5mjtuewZov_JJlQdFc44C4=s96-c\", \"given_name\": \"Javier\", \"family_name\": \"Cavedal\", \"locale\": \"es\", \"iat\": 1685893675, \"exp\": 1685897275}',6),(10,'google','112970270967348067755','2023-06-01 16:02:51.656577','2023-06-01 16:02:51.656638','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"112970270967348067755\", \"at_hash\": \"hDgFOvW575YEDCTQHtEcEA\", \"name\": \"Cintia Visaguirre\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtfpvzoF5qfgqry7pjZQpat48sO_qbGX-hmky_ym=s96-c\", \"given_name\": \"Cintia\", \"family_name\": \"Visaguirre\", \"locale\": \"es\", \"iat\": 1685635371, \"exp\": 1685638971}',12),(11,'google','117475736497990189668','2023-06-01 16:12:57.913371','2023-06-01 16:12:57.913432','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"117475736497990189668\", \"at_hash\": \"Q4CshwiznZ1nrpBdJ3_mtg\", \"name\": \"Gabi Manrique\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtdxVDsuIHvE2j0ZOkSNvOsNF1ranYeYETdYf3eQz7M=s96-c\", \"given_name\": \"Gabi\", \"family_name\": \"Manrique\", \"locale\": \"en\", \"iat\": 1685635977, \"exp\": 1685639577}',13),(12,'google','100589945615449242165','2023-06-21 13:26:26.289521','2023-06-01 16:13:15.267432','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"100589945615449242165\", \"at_hash\": \"UtJQKhSJG4hbWfdcEIQSCQ\", \"name\": \"Jere Ezquerro\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtdJDZ9qhocsi8BoE9rU_Uw2JFtaU_viZ7tZIo6dQg=s96-c\", \"given_name\": \"Jere\", \"family_name\": \"Ezquerro\", \"locale\": \"es-419\", \"iat\": 1687353986, \"exp\": 1687357586}',14),(13,'google','111710906569173703801','2023-06-21 02:20:48.361997','2023-06-01 16:24:13.892824','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"111710906569173703801\", \"at_hash\": \"x4u3a35NfIrebKcJdcQdMg\", \"name\": \"Luis Astudillo\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtdG14kjbgB6Ow1uv5JqI7a8VMvQGCbUlrCVwtpohg=s96-c\", \"given_name\": \"Luis\", \"family_name\": \"Astudillo\", \"locale\": \"es-419\", \"iat\": 1687314048, \"exp\": 1687317648}',15),(14,'google','102208653364076385930','2023-06-02 00:57:44.587448','2023-06-02 00:57:44.587507','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"102208653364076385930\", \"at_hash\": \"hLyEVbP3aSk_iZ5TYepDuQ\", \"name\": \"Alcides Norman Pessina\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtctqxhvmzx9B4SVQdW5aYk8emOWE1NQT0K2bsBz6A=s96-c\", \"given_name\": \"Alcides Norman\", \"family_name\": \"Pessina\", \"locale\": \"es\", \"iat\": 1685667464, \"exp\": 1685671064}',16),(15,'google','113601820736523659066','2023-06-02 17:12:31.181382','2023-06-02 12:16:08.486852','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"113601820736523659066\", \"at_hash\": \"BUKTLvYtTPsPPEdG2-Ukew\", \"name\": \"Natalia Cornejo\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtdr2toOgyL7mdKhkvyNZTGNuVCf3WNv-hg3OcGG=s96-c\", \"given_name\": \"Natalia\", \"family_name\": \"Cornejo\", \"locale\": \"es-419\", \"iat\": 1685725951, \"exp\": 1685729551}',17),(16,'google','109271257718258776077','2023-06-14 04:14:07.399386','2023-06-14 04:11:57.629551','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"109271257718258776077\", \"at_hash\": \"sSyMLwIZiiNxx4yAh4OZlw\", \"name\": \"Emiliano Costabile\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtcvhuVpatG5K4WWENiGwSXKbFU_IAyfQ8YlNprb=s96-c\", \"given_name\": \"Emiliano\", \"family_name\": \"Costabile\", \"locale\": \"es\", \"iat\": 1686716047, \"exp\": 1686719647}',19),(17,'google','111908335234996923625','2023-06-21 01:47:04.031615','2023-06-16 02:28:36.092354','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"111908335234996923625\", \"at_hash\": \"qVUiE_tR7WMp5IgtaPicuw\", \"name\": \"Vanesa Bourges\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtfhTbFT6tg_9bvXYN47q4njrF5LXY8qa61PEI1H=s96-c\", \"given_name\": \"Vanesa\", \"family_name\": \"Bourges\", \"locale\": \"es\", \"iat\": 1687312023, \"exp\": 1687315623}',20),(30,'google','104408581613387722073','2023-06-21 00:10:22.530846','2023-06-17 16:19:47.268960','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"104408581613387722073\", \"at_hash\": \"-2Yz0Fjg_UIwit2tUqj1GQ\", \"name\": \"Kodex Nigrae\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtfNPEBoS0zIcSHlcfwHpgTesH7fydJjCmhOJhuA=s96-c\", \"given_name\": \"Kodex\", \"family_name\": \"Nigrae\", \"locale\": \"es\", \"iat\": 1687306222, \"exp\": 1687309822}',33),(31,'google','117349192888310886123','2023-06-19 03:00:14.531687','2023-06-17 16:23:39.001876','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"117349192888310886123\", \"at_hash\": \"5KT2_6SpeACy_q8zHH4xbg\", \"name\": \"PyKodex Br\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTteSjnYx0999pHo_GBahkePs_Qa1XiFDfGw8ltOe=s96-c\", \"given_name\": \"PyKodex\", \"family_name\": \"Br\", \"locale\": \"es\", \"iat\": 1687143614, \"exp\": 1687147214}',34),(32,'google','113412755194693288711','2023-06-21 23:03:56.920646','2023-06-17 16:36:00.285035','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"113412755194693288711\", \"at_hash\": \"OL7b7olWl_G-XcmUMJbpjA\", \"name\": \"Kodex\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtffva3OWXjz-bvmm8EzUktb02KlqpYihIkrY5jLmMI=s96-c\", \"given_name\": \"Kodex\", \"locale\": \"en\", \"iat\": 1687388636, \"exp\": 1687392236}',35),(33,'google','106133082179603285936','2023-06-21 17:25:24.073379','2023-06-21 17:25:24.073427','{\"iss\": \"https://accounts.google.com\", \"azp\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"aud\": \"271510756159-ltbbahio3id70ku1d90h7bb0pv3g0kqu.apps.googleusercontent.com\", \"sub\": \"106133082179603285936\", \"at_hash\": \"VPbqV2fi0qZK_9bFg2vwTQ\", \"name\": \"Roger Pustavrh\", \"picture\": \"https://lh3.googleusercontent.com/a/AAcHTtd-dD5GcMF9UkVhO4J4sRTn9Y9-4OgtqntNvCNZ=s96-c\", \"given_name\": \"Roger\", \"family_name\": \"Pustavrh\", \"locale\": \"es-419\", \"iat\": 1687368324, \"exp\": 1687371924}',36);
/*!40000 ALTER TABLE `socialaccount_socialaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialtoken`
--

DROP TABLE IF EXISTS `socialaccount_socialtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socialaccount_socialtoken` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int NOT NULL,
  `app_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialtoken`
--

LOCK TABLES `socialaccount_socialtoken` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialtoken` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-26 21:47:49
