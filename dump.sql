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
-- Table structure for table `account_emailaddress`
--

DROP TABLE IF EXISTS `account_emailaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailaddress`
--

LOCK TABLES `account_emailaddress` WRITE;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_emailconfirmation`
--

DROP TABLE IF EXISTS `account_emailconfirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailconfirmation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailconfirmation`
--

LOCK TABLES `account_emailconfirmation` WRITE;
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_company`
--

DROP TABLE IF EXISTS `app_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_company` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `fantasy_name` varchar(255) NOT NULL,
  `cuit` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cuit` (`cuit`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_company`
--

LOCK TABLES `app_company` WRITE;
/*!40000 ALTER TABLE `app_company` DISABLE KEYS */;
INSERT INTO `app_company` VALUES (1,'Demo Company','My Demo Fantasy Name Company',1234567890),(2,'Second Company','ACME Demo Inc.',234234234);
/*!40000 ALTER TABLE `app_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_companysocialaccount`
--

DROP TABLE IF EXISTS `app_companysocialaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_companysocialaccount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `company_id` bigint DEFAULT NULL,
  `social_account_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_account_id` (`social_account_id`),
  KEY `app_companysocialaccount_company_id_d5cd92a7_fk_app_company_id` (`company_id`),
  CONSTRAINT `app_companysocialacc_social_account_id_459932d2_fk_socialacc` FOREIGN KEY (`social_account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `app_companysocialaccount_company_id_d5cd92a7_fk_app_company_id` FOREIGN KEY (`company_id`) REFERENCES `app_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_companysocialaccount`
--

LOCK TABLES `app_companysocialaccount` WRITE;
/*!40000 ALTER TABLE `app_companysocialaccount` DISABLE KEYS */;
INSERT INTO `app_companysocialaccount` VALUES (5,2,12),(6,2,30),(7,1,31),(8,2,32),(9,2,17),(10,2,3),(11,2,4),(12,2,10),(13,2,13),(14,2,16),(15,2,11),(16,2,14),(17,2,33);
/*!40000 ALTER TABLE `app_companysocialaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_drivers`
--

DROP TABLE IF EXISTS `app_drivers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_drivers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `identification_type` varchar(50) NOT NULL,
  `identification_number` varchar(50) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `company_id` bigint NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_drivers_company_id_e1385c45_fk_app_company_id` (`company_id`),
  CONSTRAINT `app_drivers_company_id_e1385c45_fk_app_company_id` FOREIGN KEY (`company_id`) REFERENCES `app_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_drivers`
--

LOCK TABLES `app_drivers` WRITE;
/*!40000 ALTER TABLE `app_drivers` DISABLE KEYS */;
INSERT INTO `app_drivers` VALUES (14,'Pablo','Burgos','DNI','34525345',1,2,0),(15,'Gonzalo','Maria Lo Perfido','DNI','25532530',1,2,0),(16,'Vanesa','Bourges','DNI','12445678',1,1,0),(17,'Javito','Selacome','DNI','87654321',1,1,0),(18,'Patricio','Reyes','DNI','24543679',1,2,0),(19,'Mariano','López','DNI','23465875',1,2,0),(20,'Gabriela','Moreira Perez','DNI','23512321',1,2,0),(21,'Jeremias','Ezquerro','DNI','36837951',1,2,0),(22,'Gabriel','Cavegol','DNI','12345678',1,2,0),(23,'Vanesa','Boriggia','DNI','26543212',1,2,0);
/*!40000 ALTER TABLE `app_drivers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_fuelorders`
--

DROP TABLE IF EXISTS `app_fuelorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_fuelorders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `modified_date` date NOT NULL,
  `requested_date` date NOT NULL,
  `operation_code` varchar(6) DEFAULT NULL,
  `expiration_date` date NOT NULL,
  `tractor_fuel_type` varchar(50) DEFAULT NULL,
  `backpack_fuel_type` varchar(50) DEFAULT NULL,
  `chamber_fuel_type` varchar(50) DEFAULT NULL,
  `tractor_liters` int unsigned DEFAULT NULL,
  `backpack_liters` int unsigned DEFAULT NULL,
  `chamber_liters` int unsigned DEFAULT NULL,
  `tractor_liters_to_load` int NOT NULL,
  `backpack_liters_to_load` int NOT NULL,
  `chamber_liters_to_load` int NOT NULL,
  `requires_odometer` tinyint(1) NOT NULL,
  `requires_kilometers` tinyint(1) NOT NULL,
  `is_blocked` tinyint(1) NOT NULL,
  `comments` longtext,
  `in_agreement` int NOT NULL,
  `company_id` bigint NOT NULL,
  `driver_id` bigint NOT NULL,
  `tractor_plate_id` bigint NOT NULL,
  `trailer_plate_id` bigint DEFAULT NULL,
  `cancel_reason` longtext,
  `is_canceled` tinyint(1) NOT NULL,
  `is_finished` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `operation_code` (`operation_code`),
  KEY `app_fuelorders_tractor_plate_id_0dd2e084_fk_app_tractors_id` (`tractor_plate_id`),
  KEY `app_fuelorders_company_id_4b961365_fk_app_company_id` (`company_id`),
  KEY `app_fuelorders_driver_id_2ebe4779_fk_app_drivers_id` (`driver_id`),
  KEY `app_fuelorders_trailer_plate_id_126be837_fk_app_trailers_id` (`trailer_plate_id`),
  CONSTRAINT `app_fuelorders_company_id_4b961365_fk_app_company_id` FOREIGN KEY (`company_id`) REFERENCES `app_company` (`id`),
  CONSTRAINT `app_fuelorders_driver_id_2ebe4779_fk_app_drivers_id` FOREIGN KEY (`driver_id`) REFERENCES `app_drivers` (`id`),
  CONSTRAINT `app_fuelorders_tractor_plate_id_0dd2e084_fk_app_tractors_id` FOREIGN KEY (`tractor_plate_id`) REFERENCES `app_tractors` (`id`),
  CONSTRAINT `app_fuelorders_trailer_plate_id_126be837_fk_app_trailers_id` FOREIGN KEY (`trailer_plate_id`) REFERENCES `app_trailers` (`id`),
  CONSTRAINT `app_fuelorders_chk_1` CHECK ((`tractor_liters` >= 0)),
  CONSTRAINT `app_fuelorders_chk_2` CHECK ((`backpack_liters` >= 0)),
  CONSTRAINT `app_fuelorders_chk_3` CHECK ((`chamber_liters` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_fuelorders`
--

LOCK TABLES `app_fuelorders` WRITE;
/*!40000 ALTER TABLE `app_fuelorders` DISABLE KEYS */;
INSERT INTO `app_fuelorders` VALUES (1,'2023-06-20','2023-06-20','2023-06-20','661350','2023-06-27','infinia_diesel','infinia_diesel','infinia_diesel',NULL,NULL,NULL,-1,-1,-1,0,0,0,'',0,2,14,1,1,NULL,0,0),(2,'2023-06-20','2023-06-21','2023-06-20','9c8e3e','2023-06-27','infinia_diesel','infinia_diesel',NULL,NULL,NULL,NULL,-1,-1,0,0,0,0,'',0,2,15,2,2,'',0,0),(3,'2023-06-20','2023-06-21','2023-06-20','80ab0a','2023-06-27','infinia_diesel',NULL,NULL,NULL,NULL,NULL,300,0,0,1,0,0,'',0,2,20,3,3,'',0,0),(4,'2023-06-20','2023-06-21','2023-06-20','895779','2023-06-27',NULL,'diesel_500',NULL,NULL,390,NULL,0,500,0,0,0,1,'',0,2,21,2,NULL,'',0,1),(5,'2023-06-20','2023-06-21','2023-06-20','278d46','2023-06-27','diesel_500','diesel_500','infinia_diesel',NULL,NULL,NULL,-1,-1,-1,0,1,0,'',0,2,19,1,NULL,'',0,0),(6,'2023-06-21','2023-06-21','2023-06-21','b61bfd','2023-06-28','infinia_diesel','diesel_500','super',NULL,NULL,NULL,-1,-1,-1,0,0,0,'',0,2,17,5,5,'',1,0),(7,'2023-06-21','2023-06-21','2023-06-21','12ba88','2023-06-28','diesel_500','diesel_500',NULL,NULL,NULL,NULL,-1,-1,-1,0,0,1,'',0,2,23,3,3,'',0,1),(8,'2023-06-21','2023-06-21','2023-06-21','1b0e33','2023-06-28','super',NULL,NULL,NULL,NULL,NULL,-1,0,0,0,0,1,'',0,2,20,3,NULL,'',0,0),(9,'2023-06-21','2023-06-21','2023-06-21','55c754','2023-06-28','diesel_500','diesel_500',NULL,NULL,NULL,NULL,-1,-1,0,1,1,0,'',0,2,22,4,4,'',0,1),(10,'2023-06-21','2023-06-21','2023-06-21','dd857e','2023-06-28','diesel_500','diesel_500','diesel_500',NULL,NULL,NULL,400,200,-1,0,0,0,'',0,2,16,4,5,'',0,0);
/*!40000 ALTER TABLE `app_fuelorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_pumpoperators`
--

DROP TABLE IF EXISTS `app_pumpoperators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_pumpoperators` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `short_name` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `short_name` (`short_name`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `app_pumpoperators_user_id_3367457f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_pumpoperators`
--

LOCK TABLES `app_pumpoperators` WRITE;
/*!40000 ALTER TABLE `app_pumpoperators` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_pumpoperators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_refuelings`
--

DROP TABLE IF EXISTS `app_refuelings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_refuelings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `acceptance_date` date NOT NULL,
  `edited_date` date NOT NULL,
  `status` int NOT NULL,
  `tractor_pic` varchar(100) NOT NULL,
  `backpack_pic` varchar(100) NOT NULL,
  `chamber_pic` varchar(100) NOT NULL,
  `tractor_liters` int unsigned NOT NULL,
  `backpack_liters` int unsigned NOT NULL,
  `chamber_liters` int unsigned NOT NULL,
  `tractor_fuel_type` varchar(50) NOT NULL,
  `backpack_fuel_type` varchar(50) NOT NULL,
  `chamber_fuel_type` varchar(50) NOT NULL,
  `odometer` int unsigned DEFAULT NULL,
  `kilometers` int unsigned DEFAULT NULL,
  `dispatch_note_pic` varchar(100) NOT NULL,
  `observation_pic` varchar(100) DEFAULT NULL,
  `observation` varchar(512) DEFAULT NULL,
  `fuel_order_id` bigint NOT NULL,
  `pump_operator_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_refuelings_fuel_order_id_c6fa4dcc_fk_app_fuelorders_id` (`fuel_order_id`),
  KEY `app_refuelings_pump_operator_id_a857967b_fk_app_pumpoperators_id` (`pump_operator_id`),
  CONSTRAINT `app_refuelings_fuel_order_id_c6fa4dcc_fk_app_fuelorders_id` FOREIGN KEY (`fuel_order_id`) REFERENCES `app_fuelorders` (`id`),
  CONSTRAINT `app_refuelings_pump_operator_id_a857967b_fk_app_pumpoperators_id` FOREIGN KEY (`pump_operator_id`) REFERENCES `app_pumpoperators` (`id`),
  CONSTRAINT `app_refuelings_chk_1` CHECK ((`tractor_liters` >= 0)),
  CONSTRAINT `app_refuelings_chk_2` CHECK ((`backpack_liters` >= 0)),
  CONSTRAINT `app_refuelings_chk_3` CHECK ((`chamber_liters` >= 0)),
  CONSTRAINT `app_refuelings_chk_4` CHECK ((`odometer` >= 0)),
  CONSTRAINT `app_refuelings_chk_5` CHECK ((`kilometers` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_refuelings`
--

LOCK TABLES `app_refuelings` WRITE;
/*!40000 ALTER TABLE `app_refuelings` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_refuelings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_setting`
--

DROP TABLE IF EXISTS `app_setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_setting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_setting`
--

LOCK TABLES `app_setting` WRITE;
/*!40000 ALTER TABLE `app_setting` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_tractors`
--

DROP TABLE IF EXISTS `app_tractors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_tractors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `domain` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_tractors_company_id_9cbe5718_fk_app_company_id` (`company_id`),
  CONSTRAINT `app_tractors_company_id_9cbe5718_fk_app_company_id` FOREIGN KEY (`company_id`) REFERENCES `app_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_tractors`
--

LOCK TABLES `app_tractors` WRITE;
/*!40000 ALTER TABLE `app_tractors` DISABLE KEYS */;
INSERT INTO `app_tractors` VALUES (1,'ASD-342',1,2),(2,'HDK-662',1,2),(3,'34-ACMX-11',1,2),(4,'99-AS3-21',1,2),(5,'75 ZMX 54',1,2);
/*!40000 ALTER TABLE `app_tractors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_trailers`
--

DROP TABLE IF EXISTS `app_trailers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_trailers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `domain` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_trailers_company_id_06884567_fk_app_company_id` (`company_id`),
  CONSTRAINT `app_trailers_company_id_06884567_fk_app_company_id` FOREIGN KEY (`company_id`) REFERENCES `app_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_trailers`
--

LOCK TABLES `app_trailers` WRITE;
/*!40000 ALTER TABLE `app_trailers` DISABLE KEYS */;
INSERT INTO `app_trailers` VALUES (1,'DD3-234',1,2),(2,'ACM-112',1,2),(3,'35-MMO-12',1,2),(4,'253 BBVE 52',1,2),(5,'234 ASB 321',1,2);
/*!40000 ALTER TABLE `app_trailers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add association',7,'add_association'),(26,'Can change association',7,'change_association'),(27,'Can delete association',7,'delete_association'),(28,'Can view association',7,'view_association'),(29,'Can add code',8,'add_code'),(30,'Can change code',8,'change_code'),(31,'Can delete code',8,'delete_code'),(32,'Can view code',8,'view_code'),(33,'Can add nonce',9,'add_nonce'),(34,'Can change nonce',9,'change_nonce'),(35,'Can delete nonce',9,'delete_nonce'),(36,'Can view nonce',9,'view_nonce'),(37,'Can add user social auth',10,'add_usersocialauth'),(38,'Can change user social auth',10,'change_usersocialauth'),(39,'Can delete user social auth',10,'delete_usersocialauth'),(40,'Can view user social auth',10,'view_usersocialauth'),(41,'Can add partial',11,'add_partial'),(42,'Can change partial',11,'change_partial'),(43,'Can delete partial',11,'delete_partial'),(44,'Can view partial',11,'view_partial'),(45,'Can add site',12,'add_site'),(46,'Can change site',12,'change_site'),(47,'Can delete site',12,'delete_site'),(48,'Can view site',12,'view_site'),(49,'Can add email address',13,'add_emailaddress'),(50,'Can change email address',13,'change_emailaddress'),(51,'Can delete email address',13,'delete_emailaddress'),(52,'Can view email address',13,'view_emailaddress'),(53,'Can add email confirmation',14,'add_emailconfirmation'),(54,'Can change email confirmation',14,'change_emailconfirmation'),(55,'Can delete email confirmation',14,'delete_emailconfirmation'),(56,'Can view email confirmation',14,'view_emailconfirmation'),(57,'Can add social account',15,'add_socialaccount'),(58,'Can change social account',15,'change_socialaccount'),(59,'Can delete social account',15,'delete_socialaccount'),(60,'Can view social account',15,'view_socialaccount'),(61,'Can add social application',16,'add_socialapp'),(62,'Can change social application',16,'change_socialapp'),(63,'Can delete social application',16,'delete_socialapp'),(64,'Can view social application',16,'view_socialapp'),(65,'Can add social application token',17,'add_socialtoken'),(66,'Can change social application token',17,'change_socialtoken'),(67,'Can delete social application token',17,'delete_socialtoken'),(68,'Can view social application token',17,'view_socialtoken'),(69,'Can add pump operators',18,'add_pumpoperators'),(70,'Can change pump operators',18,'change_pumpoperators'),(71,'Can delete pump operators',18,'delete_pumpoperators'),(72,'Can view pump operators',18,'view_pumpoperators'),(73,'Can add company',19,'add_company'),(74,'Can change company',19,'change_company'),(75,'Can delete company',19,'delete_company'),(76,'Can view company',19,'view_company'),(77,'Can add drivers',20,'add_drivers'),(78,'Can change drivers',20,'change_drivers'),(79,'Can delete drivers',20,'delete_drivers'),(80,'Can view drivers',20,'view_drivers'),(81,'Can add tractors',21,'add_tractors'),(82,'Can change tractors',21,'change_tractors'),(83,'Can delete tractors',21,'delete_tractors'),(84,'Can view tractors',21,'view_tractors'),(85,'Can add trailers',22,'add_trailers'),(86,'Can change trailers',22,'change_trailers'),(87,'Can delete trailers',22,'delete_trailers'),(88,'Can view trailers',22,'view_trailers'),(89,'Can add fuel orders',23,'add_fuelorders'),(90,'Can change fuel orders',23,'change_fuelorders'),(91,'Can delete fuel orders',23,'delete_fuelorders'),(92,'Can view fuel orders',23,'view_fuelorders'),(93,'Can add refuelings',24,'add_refuelings'),(94,'Can change refuelings',24,'change_refuelings'),(95,'Can delete refuelings',24,'delete_refuelings'),(96,'Can view refuelings',24,'view_refuelings'),(97,'Can add setting',25,'add_setting'),(98,'Can change setting',25,'change_setting'),(99,'Can delete setting',25,'delete_setting'),(100,'Can view setting',25,'view_setting'),(101,'Can add company social account',26,'add_companysocialaccount'),(102,'Can change company social account',26,'change_companysocialaccount'),(103,'Can delete company social account',26,'delete_companysocialaccount'),(104,'Can view company social account',26,'view_companysocialaccount');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-05-16 22:02:57.417068','1','example.com',3,'',12,1),(2,'2023-05-16 22:03:15.970970','2','http://127.0.0.1:8000',1,'[{\"added\": {}}]',12,1),(3,'2023-05-16 22:09:46.552706','2','http://127.0.0.1:8000',3,'',12,1),(4,'2023-05-16 22:10:27.808791','3','http://127.0.0.1:8000/',1,'[{\"added\": {}}]',12,1),(5,'2023-05-16 22:13:12.813472','1','Google',1,'[{\"added\": {}}]',16,1),(6,'2023-05-16 22:42:19.117922','3','http://127.0.0.1:8000',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',12,1),(7,'2023-05-17 01:31:11.931364','3','gabriel4',3,'',4,1),(8,'2023-05-25 23:39:22.764987','2','Gabriel',3,'',4,1),(9,'2023-05-25 23:39:22.770295','4','gabriel5',3,'',4,1),(10,'2023-05-25 23:39:22.776498','8','kodex',3,'',4,1),(11,'2023-05-25 23:39:22.782321','7','pykodex',3,'',4,1),(12,'2023-06-04 23:44:11.831711','1','My Demo Fantasy Name Company',1,'[{\"added\": {}}]',19,18),(13,'2023-06-04 23:44:26.444539','1','CompanySocialAccount object (1)',1,'[{\"added\": {}}]',26,18),(14,'2023-06-04 23:45:53.562576','2','ACME Demo Inc.',1,'[{\"added\": {}}]',19,18),(15,'2023-06-04 23:46:08.744424','2','CompanySocialAccount object (2)',1,'[{\"added\": {}}]',26,18),(16,'2023-06-04 23:56:00.160859','1','Kodex Nigrae -> My Demo Fantasy Name Company',3,'',26,18),(17,'2023-06-04 23:56:10.677635','3','Gabriel -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(18,'2023-06-04 23:58:25.163983','4','Kodex Nigrae -> My Demo Fantasy Name Company',1,'[{\"added\": {}}]',26,18),(19,'2023-06-14 13:18:55.896287','5','Jere Ezquerro -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(20,'2023-06-17 16:19:17.326969','9','kodex',3,'',4,18),(21,'2023-06-17 16:19:17.331543','25','kodex0',3,'',4,18),(22,'2023-06-17 16:19:17.335961','30','kodex09',3,'',4,18),(23,'2023-06-17 16:19:17.341988','26','kodex1',3,'',4,18),(24,'2023-06-17 16:19:17.347190','21','kodex2',3,'',4,18),(25,'2023-06-17 16:19:17.353049','27','kodex3',3,'',4,18),(26,'2023-06-17 16:19:17.357457','31','kodex33',3,'',4,18),(27,'2023-06-17 16:19:17.361750','28','kodex4',3,'',4,18),(28,'2023-06-17 16:19:17.366064','29','kodex6',3,'',4,18),(29,'2023-06-17 16:19:17.371095','24','kodex7',3,'',4,18),(30,'2023-06-17 16:19:17.375640','32','kodex94',3,'',4,18),(31,'2023-06-17 16:19:17.380082','11','pykodex',3,'',4,18),(32,'2023-06-17 16:19:17.385081','23','pykodex6',3,'',4,18),(33,'2023-06-17 16:19:17.391632','22','pykodex9',3,'',4,18),(34,'2023-06-17 16:20:22.698524','6','Kodex Nigrae -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(35,'2023-06-17 17:43:09.529970','7','PyKodex Br -> My Demo Fantasy Name Company',1,'[{\"added\": {}}]',26,18),(36,'2023-06-17 18:19:31.619595','8','Kodex -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(37,'2023-06-18 20:58:39.131855','13','Pablo Burgos',3,'',20,18),(38,'2023-06-18 20:58:39.137803','12','Pablo Burgos',3,'',20,18),(39,'2023-06-18 20:58:39.144058','11','Pablo Burgos',3,'',20,18),(40,'2023-06-18 20:58:39.150580','10','Pablo Burgos',3,'',20,18),(41,'2023-06-18 20:58:39.155456','9','Pablo Burgos',3,'',20,18),(42,'2023-06-19 19:41:34.268943','9','Vanesa Bourges -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(43,'2023-06-19 19:41:40.104228','10','Andy Cavedal -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(44,'2023-06-19 19:41:48.093780','11','Javier Cavedal -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(45,'2023-06-20 17:58:20.941763','1','661350',1,'[{\"added\": {}}]',23,18),(46,'2023-06-20 17:59:07.986460','2','9c8e3e',1,'[{\"added\": {}}]',23,18),(47,'2023-06-20 19:55:00.028856','2','9c8e3e',2,'[{\"changed\": {\"fields\": [\"Chamber liters to load\"]}}]',23,18),(48,'2023-06-20 19:56:00.331647','3','80ab0a',1,'[{\"added\": {}}]',23,18),(49,'2023-06-20 22:11:17.887123','4','895779',1,'[{\"added\": {}}]',23,18),(50,'2023-06-20 22:57:46.796148','3','80ab0a',2,'[{\"changed\": {\"fields\": [\"Requires odometer\"]}}]',23,18),(51,'2023-06-20 22:59:56.623498','5','278d46',1,'[{\"added\": {}}]',23,18),(52,'2023-06-21 00:52:50.844030','6','b61bfd',1,'[{\"added\": {}}]',23,18),(53,'2023-06-21 01:50:48.346825','5','278d46',2,'[{\"changed\": {\"fields\": [\"Trailer plate\"]}}]',23,18),(54,'2023-06-21 01:51:15.977446','4','895779',2,'[{\"changed\": {\"fields\": [\"Chamber liters to load\"]}}]',23,18),(55,'2023-06-21 01:54:07.141882','3','80ab0a',2,'[{\"changed\": {\"fields\": [\"Tractor fuel type\", \"Backpack fuel type\", \"Chamber fuel type\"]}}]',23,18),(56,'2023-06-21 01:54:16.087984','2','9c8e3e',2,'[{\"changed\": {\"fields\": [\"Chamber fuel type\"]}}]',23,18),(57,'2023-06-21 01:54:48.267450','4','895779',2,'[{\"changed\": {\"fields\": [\"Tractor fuel type\"]}}]',23,18),(58,'2023-06-21 01:55:10.033175','3','80ab0a',2,'[{\"changed\": {\"fields\": [\"Tractor fuel type\"]}}]',23,18),(59,'2023-06-21 01:57:04.051952','5','278d46',2,'[{\"changed\": {\"fields\": [\"Chamber fuel type\"]}}]',23,18),(60,'2023-06-21 02:05:49.038047','7','12ba88',1,'[{\"added\": {}}]',23,18),(61,'2023-06-21 02:06:27.705233','8','1b0e33',1,'[{\"added\": {}}]',23,18),(62,'2023-06-21 02:11:45.341006','12','Cintia Visaguirre -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(63,'2023-06-21 02:11:52.879852','13','Luis Astudillo -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(64,'2023-06-21 02:12:02.013283','14','Emiliano Costabile -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(65,'2023-06-21 02:12:13.098089','15','Gabi Manrique -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(66,'2023-06-21 02:12:30.112899','16','Alcides Norman Pessina -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(67,'2023-06-21 12:25:57.938294','9','55c754',1,'[{\"added\": {}}]',23,18),(68,'2023-06-21 14:28:57.052891','10','dd857e',1,'[{\"added\": {}}]',23,18),(69,'2023-06-21 18:18:13.217584','17','Roger Pustavrh -> ACME Demo Inc.',1,'[{\"added\": {}}]',26,18),(70,'2023-06-26 01:07:56.967905','3','http://kodex.duckdns.org',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',12,18);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (13,'account','emailaddress'),(14,'account','emailconfirmation'),(1,'admin','logentry'),(19,'app','company'),(26,'app','companysocialaccount'),(20,'app','drivers'),(23,'app','fuelorders'),(18,'app','pumpoperators'),(24,'app','refuelings'),(25,'app','setting'),(21,'app','tractors'),(22,'app','trailers'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(12,'sites','site'),(7,'social_django','association'),(8,'social_django','code'),(9,'social_django','nonce'),(11,'social_django','partial'),(10,'social_django','usersocialauth'),(15,'socialaccount','socialaccount'),(16,'socialaccount','socialapp'),(17,'socialaccount','socialtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-05-16 05:00:32.478060'),(2,'auth','0001_initial','2023-05-16 05:00:33.551917'),(3,'admin','0001_initial','2023-05-16 05:00:33.770744'),(4,'admin','0002_logentry_remove_auto_add','2023-05-16 05:00:33.784649'),(5,'admin','0003_logentry_add_action_flag_choices','2023-05-16 05:00:33.803435'),(6,'contenttypes','0002_remove_content_type_name','2023-05-16 05:00:33.914366'),(7,'auth','0002_alter_permission_name_max_length','2023-05-16 05:00:34.017836'),(8,'auth','0003_alter_user_email_max_length','2023-05-16 05:00:34.056051'),(9,'auth','0004_alter_user_username_opts','2023-05-16 05:00:34.071548'),(10,'auth','0005_alter_user_last_login_null','2023-05-16 05:00:34.162690'),(11,'auth','0006_require_contenttypes_0002','2023-05-16 05:00:34.168894'),(12,'auth','0007_alter_validators_add_error_messages','2023-05-16 05:00:34.183800'),(13,'auth','0008_alter_user_username_max_length','2023-05-16 05:00:34.276562'),(14,'auth','0009_alter_user_last_name_max_length','2023-05-16 05:00:34.383807'),(15,'auth','0010_alter_group_name_max_length','2023-05-16 05:00:34.421487'),(16,'auth','0011_update_proxy_permissions','2023-05-16 05:00:34.441383'),(17,'auth','0012_alter_user_first_name_max_length','2023-05-16 05:00:34.533702'),(18,'sessions','0001_initial','2023-05-16 05:00:34.610696'),(19,'default','0001_initial','2023-05-16 20:26:58.873283'),(20,'social_auth','0001_initial','2023-05-16 20:26:58.882608'),(21,'default','0002_add_related_name','2023-05-16 20:26:58.902681'),(22,'social_auth','0002_add_related_name','2023-05-16 20:26:58.911612'),(23,'default','0003_alter_email_max_length','2023-05-16 20:26:58.938945'),(24,'social_auth','0003_alter_email_max_length','2023-05-16 20:26:58.946709'),(25,'default','0004_auto_20160423_0400','2023-05-16 20:26:58.968142'),(26,'social_auth','0004_auto_20160423_0400','2023-05-16 20:26:58.977094'),(27,'social_auth','0005_auto_20160727_2333','2023-05-16 20:26:59.016471'),(28,'social_django','0006_partial','2023-05-16 20:26:59.089092'),(29,'social_django','0007_code_timestamp','2023-05-16 20:26:59.174004'),(30,'social_django','0008_partial_timestamp','2023-05-16 20:26:59.262925'),(31,'social_django','0009_auto_20191118_0520','2023-05-16 20:26:59.375861'),(32,'social_django','0010_uid_db_index','2023-05-16 20:26:59.424486'),(33,'social_django','0011_alter_id_fields','2023-05-16 20:26:59.886659'),(34,'social_django','0003_alter_email_max_length','2023-05-16 20:26:59.898531'),(35,'social_django','0002_add_related_name','2023-05-16 20:26:59.906563'),(36,'social_django','0004_auto_20160423_0400','2023-05-16 20:26:59.914054'),(37,'social_django','0005_auto_20160727_2333','2023-05-16 20:26:59.920933'),(38,'social_django','0001_initial','2023-05-16 20:26:59.926528'),(39,'account','0001_initial','2023-05-16 21:57:34.368498'),(40,'account','0002_email_max_length','2023-05-16 21:57:34.421509'),(41,'sites','0001_initial','2023-05-16 21:57:34.468131'),(42,'sites','0002_alter_domain_unique','2023-05-16 21:57:34.509992'),(43,'socialaccount','0001_initial','2023-05-16 21:57:35.227883'),(44,'socialaccount','0002_token_max_lengths','2023-05-16 21:57:35.336390'),(45,'socialaccount','0003_extra_data_default_dict','2023-05-16 21:57:35.360531'),(46,'app','0001_initial','2023-06-03 16:10:29.306619'),(47,'app','0002_companysocialaccount','2023-06-04 23:43:39.839072'),(48,'app','0003_alter_company_options_remove_drivers_language','2023-06-18 16:55:11.172606'),(49,'app','0004_drivers_is_deleted','2023-06-18 20:35:39.223992'),(50,'app','0005_alter_drivers_identification_type','2023-06-18 20:40:51.135561'),(51,'app','0006_alter_fuelorders_backpack_liters_and_more','2023-06-20 16:16:21.359952'),(52,'app','0007_alter_fuelorders_backpack_liters_and_more','2023-06-20 16:17:03.555589'),(53,'app','0008_fuelorders_cancel_reason_fuelorders_is_canceled_and_more','2023-06-20 20:27:28.292944'),(54,'app','0009_alter_fuelorders_expiration_date','2023-06-21 00:11:12.383106'),(55,'app','0010_alter_fuelorders_backpack_fuel_type_and_more','2023-06-21 01:53:52.402764'),(56,'app','0011_alter_fuelorders_options_and_more','2023-06-21 22:24:46.220910');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('063afyyuciq64q0uq9ohuhz7uq5cv0k3','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoiTnhNb3IiLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIkR2TXJiYUNremxCaSJdfQ:1q3S64:luS_KVfXRgL4YG1VSwnaFMOObXf8WpDy8Y4QPmHJnXU','2023-06-12 01:54:56.906875'),('0wsxubk3njw0umcfja9skecqsoyqjjsa','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIldOZVE4MjZIUnM5RyJdfQ:1q4ELB:W2N96y3P2j3hDjt5dLndrREJnyqQXVAr-vfOk3hwF2o','2023-06-14 05:25:45.281630'),('1gwwrii747yks4bp39qxzxobsgh6z30b','.eJxVjMEOwiAQRP-FsyFAW1i86Y-QZbukxIYmAifjv9uaHvQ2M29mXiJgb0volZ8hz-IqvLj8ZhHpweUAuK5HLJFo66XJb-fEVd52x6Vlwpa3cj9Xf1cL1mX_sTESgDUzMDmcgMzE4CMMySYLJimTvNWs1aQU7Vob78boeJgdjNqQeH8Av8Y72A:1q696H:CPmF5Ls7w1p0QQGx04rRycyxSDXBs63FmvFTBOixCnk','2023-06-19 12:14:17.100384'),('1jsff4jrvng2fry6tlbkjfkgjmm6c29v','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sInZreUlWYXNEWGZQZCJdfQ:1q3S4x:mX-NSCcFD768v5aNnUWLdolFfb1cs83_WM5EonuXUFs','2023-06-12 01:53:47.341303'),('2vq0ecrgez1f9hdtswp1wj5j6sd55atv','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIkY2aTRnOWFDN3VSMyJdfQ:1q3S5M:_Wyk69E3Ba-y-hnatk9ibOzX53ModmsLOsazxheYq1M','2023-06-12 01:54:12.755608'),('33ed0jtknqw3tooeie9lomplkasytro8','.eJxVjEsOAiEQRO_C2hAQ-bnTi5DuBgJxwiQCK-PdnTGz0GW9qnovFmCOEmZPz1AjuzKp2ekXItAjtb2BZdkxB6J1tsG_m6Pu_Lal1EYlGHVt9-P1pyrQy-YRymRACzILq504p-ydVF7KFJV3qIQiARckAhE1WZfJoCIDFtFoSo69P9-HPP0:1qBnSi:r6Z1aZOLhxA-eYnzWAeX-i3fW0RBseLuvw_yC7su0o0','2023-07-05 02:20:48.393380'),('44e2h5tz3f2i31l0cc421def8her0zkg','.eJxVjM0OwiAQhN-Fs2mA7S7Um75Is-UnEBuaCJyM725retDjfDPzvcTMvaW51_CcsxdXASguv3Bh9wjlaHhdDzywc1svbfhuzroOtz2F0rLjlrdyP19_qsQ17R4dCHUATaiiAlJhlGR8jCjNRHphAkAAy9MYaYkSrUYy7BUzkHdWifcHtS07jA:1qBgrR:ZzBNidxXJRn5ANABRqOKO9UtTlYjInIWq5ilT_qtwl8','2023-07-04 19:17:53.275095'),('4foar4wq1xryebh6y3ii3c6srfftnzz7','.eJxVjMEOwiAYg9-FsyGwkQHe9EVI-X_MFheWCJwW311mdtDe2q_tLgJanUMr6RUWFlehlbj8hhH0TPkgWNcjliDaWq7y2zlxkbfuUq4LoS5bvp-rv6sZZe4_foCfHopJK8Ps9Bidmii50QzkyCZt2LPyykZGlyETYQnRY4DxmMT7A-qBPVE:1q5skQ:zcDGg3-dwIquIKeT_M3uSeZfhm5tyd69NE7lAwWnLcA','2023-06-18 18:46:38.470357'),('4muvm2lyr5rs1rv0nufczi6e3lwu3w9q','.eJxVjMsOwiAURP-FtWl43PJwpz9CLnAJxIYmQlfGf7c1XehyzsycF_O4jeK3Tk9fE7sy4djlFwaMD2pHg8ty4AljXLc2pu_mrPt02xO1USOOurb7-fpTFexl9xhlLHKtCCQ32ToJQFlloQIlmIXjYgYBqILm5EzUSVsZVIrJEmhrDHt_ALq0O6A:1q9HtX:ZnneVNsYRElnwXB5JJ-axzf27aJFDav1qlEFGQZ8UhY','2023-06-28 04:14:07.428868'),('4pp8mw8jn8v9qb8xmn98pczj95mp5d6c','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sInlNRnlQMDhmRXB3UCJdfQ:1qAY3n:DORrEld49gQGru_F4uasp7BYwEAnz_sMEVA7UKEa4Sk','2023-07-01 15:41:55.830530'),('57qj9c6vfb5ogn4ugghgcsnxerbk03n4','.eJxVjMEOwiAYg9-FsyGwkQHe9EVI-X_MFheWCJwW311mdtDe2q_tLgJanUMr6RUWFlehlbj8hhH0TPkgWNcjliDaWq7y2zlxkbfuUq4LoS5bvp-rv6sZZe4_foCfHopJK8Ps9Bidmii50QzkyCZt2LPyykZGlyETYQnRY4DxmMT7A-qBPVE:1q5s6r:tZXEI2LsK22GaYrtgp4VVmt_44sZqTl5DqI9Ys9xYcc','2023-06-18 18:05:45.897160'),('5gnt2dbsbzaz8gqfhrjsmf8dqcmf27el','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIkdGSHJpT1RmcE9JTSJdfQ:1q4kvH:xWQEXuBPKK0UdasVBhuGHKmgLhTNKKSje8UH9me1kg8','2023-06-15 16:13:11.738550'),('6yyrt8juntlfnu19ktyw6v53dnuuiamr','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sImhYSGxTTjR3Q1Z4TCJdfQ:1q4aT1:et2cdQaIYk_muyx7D_1-3YeKJW32ID0nUmsIwHL-GEc','2023-06-15 05:03:19.372186'),('86496wta2volo6a81b0b2wnbtxvfuuq1','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIjhwbEV6Y0N0ZXByVSJdfQ:1pz68Z:v2tyCLjZy0ggKO0diS4WGwhV1OXqKpu7qkL-ixOw6DI','2023-05-31 01:39:31.269308'),('8fhl9mlzl8s97i5vf56w4761zwa6oq15','.eJxVjMsOwiAURP-FtSE8r-DO_giBCwRiQxOBlfHfbU0XupwzM-dFnJ-juNnT09VIboQrcvmFweMjtaPx63pg6hG32Qb9bs660_ueUhsV_ahbW87Xn6r4XnaPsZFxkwIDkNzyrMBmDUlIERQAZ1YaxZgArVChMVxrG1DELK5RRikMeX8AoX861g:1q9PQM:sPKwijcFPLjI-bIC5SCogQ5KNcozGtRYrZLTOL_UPNI','2023-06-28 12:16:30.013777'),('97yqptxp1tv5spg216tpd6ldpq8n0g4g','.eJxVjMsOgjAQRf-la9OUocDg0r3fQOaFoKZNKKyM_64kLHR7zzn35Qba1mnYii3DrO7sKnSn35FJHpZ2ondKt-wlp3WZ2e-KP2jx16z2vBzu38FEZfrWhDFAE8wocM8AIxpU2o2gsQFBQqgFObQ1kbRVH2PHipGFoENTAvf-AAt1OFU:1qBwvg:cvPeBaKGXquzrUbv-bQWNAT73kQ3C9Kc1RD_0_kLk70','2023-07-05 12:27:20.565662'),('ajs5foa7jfyuqp2ahy4m1ktnfxtoyvy9','.eJxVjM0OwiAQhN-Fs2mA7S7Um75Is-UnEBuaCJyM725retDjfDPzvcTMvaW51_CcsxdXASguv3Bh9wjlaHhdDzywc1svbfhuzroOtz2F0rLjlrdyP19_qsQ17R4dCHUATaiiAlJhlGR8jCjNRHphAkAAy9MYaYkSrUYy7BUzkHdWifcHtS07jA:1qC6rk:L_4o1kTmHOalf1EuYGx_2_zeXqLHIFHp2x4uRfGLo38','2023-07-05 23:03:56.957170'),('aqot2eqrjc3r3rop9grhb6n4v8d3j9va','.eJxVjM0OwiAQhN-Fs2mA7S7Um75Is-UnEBuaCJyM725retDjfDPzvcTMvaW51_CcsxdXASguv3Bh9wjlaHhdDzywc1svbfhuzroOtz2F0rLjlrdyP19_qsQ17R4dCHUATaiiAlJhlGR8jCjNRHphAkAAy9MYaYkSrUYy7BUzkHdWifcHtS07jA:1qB5NX:apHN9RGl7LZYEpKkWwTtQBCngIZ934X0_uawXSqnveQ','2023-07-03 03:16:31.439933'),('axothtm7gjctm1i820h5858kqbhw3ym9','.eJxVjMEOgyAQRP9lz40RiGvx1v4IWRY2klJMKvTS9N-rjReP82bmfYCYl1aqe8dXkhSDi09KGabScr6Ao1Zn19b4cinABAOcmCd-xLIXlPOOu0PX_TdHvXa3LcVSE1NNS7kfr5NqpnXePNgr1GzG3mpGsoKodRzZ42CJjQoqiLJaxKAVH1Cs1t6z9cFcRQ00wvcHcypH6w:1pz6PF:s_8WjVjczXLDJ2D0TxfuJaXVJkhgSNM-wLrExkhC01g','2023-05-31 01:56:45.682687'),('c43jvw7zer50fgf0hqnlt0plyz3w0dtf','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sImtwRzBUMEhZbVRkeSJdfQ:1q4rGX:5AeB_BX12luKx8HiGTvHieZ270vSZu7RCxtov6tUHpM','2023-06-15 22:59:33.569295'),('cd0fq3dt9dle0p4sao82mzm2j9x1kin4','.eJxVjM0OwiAQhN-Fs2mA7S7Um75Is-UnEBuaCJyM725retDjfDPzvcTMvaW51_CcsxdXASguv3Bh9wjlaHhdDzywc1svbfhuzroOtz2F0rLjlrdyP19_qsQ17R4dCHUATaiiAlJhlGR8jCjNRHphAkAAy9MYaYkSrUYy7BUzkHdWifcHtS07jA:1qBwuj:XKjoT-7n7lhWvuCFXbH0LvpHBYqki40roPHxhtCil6I','2023-07-05 12:26:21.720025'),('ciwwd5uqwccgwnlgmdtxr8clv6rxqvc8','.eJxVjU0OwiAQhe_C2pCBBizu9CJkhpmmjQ1NBFaNd5eaLnT53vd-dhWx1Tm2Iq-4sLopc1WXX5MwPSUfBNf1sDWmtLVc9Tdz4qLvXUmuS8K6bPlxtv6mZixz30keRUIAg8HwZDmMNIBznsBSGAfuyls7QWBxnvsBwQTARkCAaRT1_gDvGj0k:1q58KF:bvpSPZaJS5ljpOs1gbqzBdyKKfx1-tpp_7LAjKBDA8E','2023-06-16 17:12:31.211974'),('dw4456qp9gczbvpqgwjfjkvc1v5kh8ha','.eJxVjEsOAiEQRO_C2hAQ-bnTi5DuBgJxwiQCK-PdnTGz0GW9qnovFmCOEmZPz1AjuzKp2ekXItAjtb2BZdkxB6J1tsG_m6Pu_Lal1EYlGHVt9-P1pyrQy-YRymRACzILq504p-ydVF7KFJV3qIQiARckAhE1WZfJoCIDFtFoSo69P9-HPP0:1q4l6E:2-bQ_z-Jm8HZB5XCRQnGj-3BDFDh2uxtOfxt2uBnvAM','2023-06-15 16:24:30.109800'),('ehqztzvy3l6ngwfmao4wmou7v37s2gsw','.eJxVjMEOgyAQRP9lz40RUEFv7Y-QhV0iKcVEoZem_15tvHicNzPvA-j9UnOxb15jiEyWXxgTTLmmdAOLtcy2brzaSDCBEnCBDv2T89FgSgduTl_z35z11tz3xLlEjyUu-XG-LqoZt3n3aJJilB1r6aQTA7YKPY1Ka4OdR-OQpKEwGommYw6tCUym70m3Qg3sGb4_t_ZIdw:1qAYGl:WBiypZ0MZHnWpfLnFhjKfr6oEm82x15BUEGb3jt7xfU','2023-07-01 15:55:19.915112'),('h8m410ynol7jgjdzdh8xrsc4d4j7hkeh','.eJxVjEEOwiAURO_C2hCw_ALu7EXI5wOB2NBEYGW8u63pQpfzZua9mMPRsxstPl0J7MYmdvllHukR61Hguh6YI9E2auffzVk3ft9TrL0Q9rLV5Xz9qTK2vHsggASUNhL6hCEJTEIoCwoIgSIFtFoKOWk7UwIIV4DZR0ukjBEGNHt_ANz5PKs:1pz3pX:6d0mBHW4a5qyHxq9DVXgoN_XvxtHNmOHXL7nSoabb1I','2023-05-30 23:11:43.047685'),('htwphld3jdb9suqdkctylivsg7scytrp','.eJxVjMsOwiAURP-FtSE8r-DO_giBCwRiQxOBlfHfbU0XupwzM-dFnJ-juNnT09VIboQrcvmFweMjtaPx63pg6hG32Qb9bs660_ueUhsV_ahbW87Xn6r4XnaPsZFxkwIDkNzyrMBmDUlIERQAZ1YaxZgArVChMVxrG1DELK5RRikMeX8AoX861g:1qBxqs:WVzFlK_kCiz035c50CRpZ-sDdSkzM-uq7nArcZKDuc0','2023-07-05 13:26:26.316020'),('jnmidn9iyfpbhees2powsz5a6vwp45jq','.eJxVjMsOgyAURP-FdWN4irprf4RcL5dISjER6Kbpv1cbNy7nzMz5MEBcW67uTVsMkbyjF8TEptxSujEHrS6uFdpc9GxiqmcXOAM-KR8NpHTg7vR1_81Zl-6-J8o1ItS45sf5uqgWKMvu4UZQ6EmhB6uQ4yCHcZQgQ-AUcLa8F0YHbrW0FuVsxIgktTaegxWWK_b9AbnmR3c:1qC1a8:ns6OGHYjkEU1-eHyW1-H-bxDeD6i2HLpJhX0bIKzXNg','2023-07-05 17:25:24.108898'),('jz446f99ojem6ed8kuwfdcd88hm5ozw7','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIklLRHp5N3VwcGh6WiJdfQ:1q3s97:2RCXajmyl11rxcLww9C71nuHHZMWlP0YCnZayrymzho','2023-06-13 05:43:49.676293'),('kc05x3e67q2eo84pd433vr3cbonprnoh','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIk1lWU5VVDRzQXhYcCJdfQ:1qBypf:d7hayoP4PVjAJtJRuqx8rffbt407R_1MJ6rUd7FkU40','2023-07-05 14:29:15.107402'),('kjphanwluc1wm3l6q8g7zt0a8u4lbplk','.eJxVjMEOgjAQRP-lZ0Os22XRm_4ImW63gUhqIuVk_HfBcNDjvJl5L9djqUO_zPbsx-QujsgdfmGE3q1sDaZpww1UH0upzXez13NzXZOVOirq-Ci3_fWnGjAPqyexhe4cRSLYZw_P5CkZdcosXiwfAxRoQcZZLaTYtsSSUhacghf3_gDwpT0H:1qBlQU:Eo6zYJ_Y9p7sPy2y43Ac-9mwFSGlEHG6yq_Kq79bh7k','2023-07-05 00:10:22.553822'),('kktdlu42z8tq8l3x6kc4c2111vosafvj','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIkh0ZFdrbGNWNXFGMSJdfQ:1q2KZD:SkEdQU7-IulyYlbfI7OH0z3s1axKOuK15HgxZwu8uQ4','2023-06-08 23:40:23.901046'),('km16i7ydfnm73dll2naba6ltcx8z0shz','.eJxVjMEOwiAYg9-FsyGwkQHe9EVI-X_MFheWCJwW311mdtDe2q_tLgJanUMr6RUWFlehlbj8hhH0TPkgWNcjliDaWq7y2zlxkbfuUq4LoS5bvp-rv6sZZe4_foCfHopJK8Ps9Bidmii50QzkyCZt2LPyykZGlyETYQnRY4DxmMT7A-qBPVE:1q2MlQ:khAU6G7leSlnfaHBS5C6f0Ekrd0YX_7CqfDK9mBALzg','2023-06-09 02:01:08.468630'),('kr6lyutj9tubulpa8sftc7pnk6zm964i','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sImxISjFuMUtxVndmVyJdfQ:1q3nn4:v1b_nTJt5hpV1UuLoMAuZYr2hTA-csc1Dctzj941lFI','2023-06-13 01:04:46.726566'),('leah1evsuhzhimmo1sr4gdw97dg0n9vl','.eJxVjMsOwiAURP-FtSFAeVzc6Y-Qyy0EYkMTCyvjv9uaLnQ5Z2bOiwUcvYSxpWeoM7syJdjlF0akR2pHg8tyYI5E62idfzdnvfHbnlLrlbDXtd3P15-q4FZ2j0UAkb2TlK0gbcBq54313ieSJkoNU1RezagpZ4UOI4HORkqEyTqZ2PsDxPc8Ag:1qBmw4:4zylebBlBIQBGPnkKvd5oaO-OxD93B70wcnTyaSo5wk','2023-07-05 01:47:04.063443'),('lo5a3iqdbenv3705f9n4vbgsox0e3vh6','.eJxVjM0OwiAQhN-Fs2mA7S7Um75Is-UnEBuaCJyM725retDjfDPzvcTMvaW51_CcsxdXASguv3Bh9wjlaHhdDzywc1svbfhuzroOtz2F0rLjlrdyP19_qsQ17R4dCHUATaiiAlJhlGR8jCjNRHphAkAAy9MYaYkSrUYy7BUzkHdWifcHtS07jA:1qBLzA:Bg_abezIolKzQuw9kuOGIZG0FQAlZvyHtyDhkFZrfHU','2023-07-03 21:00:28.707654'),('lsmegh80lm062jk2ik5hhbpszyl1tvng','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIlZ4WllUcXNuekRzViJdfQ:1q4aSy:XJqNncJ5_Vx-hO85flQoj77YZevQpjFzZAYh-yJGpcY','2023-06-15 05:03:16.122303'),('ndvuvgj52p9s7e3idu703vai2v1d6g84','.eJxVjMsOgyAURP-FdWNAkIe79kfIBS6RlGIi0E3Tf682blzOmZnzIeD92kuzb9xSTBgsviBlMpee841Y6G2xveJmUyAzYYZcoAP_xHI0kPOBh9M3_DdnXYf7nrC05KGltTzO10W1QF12j-JKA5UcxUhV1GYUAiOPjDsMYmKGskkwAdxJikZ5GaQeHQ8-aBRSK0W-P4yARwY:1q9HrR:lSX7q9yIg33waTIfQYVJ6CeTnDVFjRu1JKEIemMVMTM','2023-06-28 04:11:57.660785'),('odkiknlqyocveqfgwbh91r4pktpqp1ch','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIjhDR3hpR0hCZmFEaCJdfQ:1q5Xk2:Rg9FQ56GcMjv7VLIoPaSsZzm2lrq6JV7_0-RsZt9sP8','2023-06-17 20:20:50.892815'),('qnvm13o1r9dodal6h6r1lwu9sjgny6mv','.eJxVjDsOwyAQBe9CHSHby_JJmd5nQAsLsZMIJGNXUe4eIblI2jcz7y08Hfvij5Y2v7K4ilFcfrdA8ZlKB_ygcq8y1rJva5BdkSdtcq6cXrfT_TtYqC291mQcOmJltTPDaCkqEzAoZ3HIoMA6ywlAuQk1RADMo8LMmSPmMKH4fAHBsTc2:1pz6qU:VU3h8Fa6w9Zgddo6bleOPy1UqDlX84ccBgYGzZsjTbg','2023-05-31 02:24:54.106325'),('qrnzf31e673co78p5lc9tpxq5bh89rl0','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIkhTQkZiVENBWWNxSSJdfQ:1q3zUi:BpwDLuCOxw68jbID1fM608s9UmHS08UO52CVFIC4yKg','2023-06-13 13:34:36.223527'),('qsniv6inoz0h6owexri8amn4z2a35dyi','.eJxVjMsOgjAQRf-la9OUocDg0r3fQOaFoKZNKKyM_64kLHR7zzn35Qba1mnYii3DrO7sKnSn35FJHpZ2ondKt-wlp3WZ2e-KP2jx16z2vBzu38FEZfrWhDFAE8wocM8AIxpU2o2gsQFBQqgFObQ1kbRVH2PHipGFoENTAvf-AAt1OFU:1qCh5w:iit3LuOfRGMj8aHJjhY3DG-PfPP8I_KhTGPd4VSPHyM','2023-07-07 13:45:00.739984'),('rid7u1s6c54n0pcwxfyy5tszu693t4lp','.eJxVjMEOwiAYg9-FsyGwkQHe9EVI-X_MFheWCJwW311mdtDe2q_tLgJanUMr6RUWFlehlbj8hhH0TPkgWNcjliDaWq7y2zlxkbfuUq4LoS5bvp-rv6sZZe4_foCfHopJK8Ps9Bidmii50QzkyCZt2LPyykZGlyETYQnRY4DxmMT7A-qBPVE:1q8A2d:TQpatp0Y3RBATZLVBrnyFD8f-GAVblDC6hmZ068Za2E','2023-06-25 01:38:51.094695'),('rk94sktfp6xby610i9pv3dcoz3xxzf12','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIkhKWHRZb0txbVowdSJdfQ:1q3zfF:eyfUFDRIVusNEqEWmADxQC6Y4g1_DOHdPGAAnwoRL1g','2023-06-13 13:45:29.763381'),('ubr9bq7jdzlh9td3z1pqlrubsaqivd0t','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIkM0S2Q3UFh2ZVZ3QSJdfQ:1qBJ6x:Sy1l0uq6j6zXTiujW9x0CW5_-nLhIMdI5r6BBSwj8dM','2023-07-03 17:56:19.624933'),('usemtj9yhii2108vsa6okutzs17p0vog','.eJxVjMsOgyAURP-FdWN43oK7-iOExyWSUkwUumn679XGjcs5M3M-xIWw9NrsG9ecMkaLL5cLGWsv5Uas6222fcPV5khGwiS5QO_CE-vRuFIOPJy-4b8562147Alry8G1vNTpfF1Us9vm3aNNpEyjpwCCGZYkmKQAueBeAjBqhJaUclAyyKA1U8r4wGPi9yii4Jp8f3NLRjw:1q4kvL:wvpuEn9o8yo6kL5y3_CFsguO4HSTvXbiepq-6bYalQk','2023-06-15 16:13:15.297683'),('v9o1w6t5y3bpzem5g8o4zyougr0oh9c8','.eJxVjEEOwiAURO_C2hCw_ALu7EXI5wOB2NBEYGW8u63pQpfzZua9mMPRsxstPl0J7MYmdvllHukR61Hguh6YI9E2auffzVk3ft9TrL0Q9rLV5Xz9qTK2vHsggASUNhL6hCEJTEIoCwoIgSIFtFoKOWk7UwIIV4DZR0ukjBEGNHt_ANz5PKs:1pz3pG:PANP51X9AtgMjS6Ga74fUeE5S0hnYrVOIe2NfbOds68','2023-05-30 23:11:26.191858'),('wdwgr3l83gomssa4c5ml87rxknq1a10q','.eJxVjMsOgjAQRf-la9OUocDg0r3fQOaFoKZNKKyM_64kLHR7zzn35Qba1mnYii3DrO7sKnSn35FJHpZ2ondKt-wlp3WZ2e-KP2jx16z2vBzu38FEZfrWhDFAE8wocM8AIxpU2o2gsQFBQqgFObQ1kbRVH2PHipGFoENTAvf-AAt1OFU:1qBzBM:FepkN0L_hDIe-1DvNvjCkfUjUA66wfPgAs8tmzw-MZU','2023-07-05 14:51:40.113167'),('wsskmi9i9jh9s2qod61ltx9nil6lcnrx','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIjh0UmJxaTN5TUF1dyJdfQ:1q0WVp:tBkN646K_EODLuflP8KyAAd9P_DEK1NTTuAffs7642A','2023-06-04 00:01:25.002233'),('xhmvrnvq0fvadn8rseyimiwc4pp4xo22','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sInRYcThZd2NjR2hXQyJdfQ:1qBJ6V:6V_yq93lAAon1VSwnlo8AML-WfoMAIed5I7wv4QqCdQ','2023-07-03 17:55:51.846471'),('xpt02me8malx1sgu2sls6bgysewztctj','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIlNaajdRZzJaWnF6ZiJdfQ:1q4aSz:6W-qz0eduFZnqWWLsjq4TGJMmrrmX4uEAvlClV_R_7g','2023-06-15 05:03:17.871216'),('xye1skq120a239nkpzgdn1vq4z3yp2jt','eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sImRvU0duWm9Kb0JlbCJdfQ:1q0Ugu:_mp_KgauPyeyouAMutQZvZ0sHhLqLbVEbGA7gvQLTpU','2023-06-03 22:04:44.885753'),('y7xlb3csmo8yj98z0kdccqbbtcpds839','.eJxVjEEOwiAURO_C2hCw_ALu7EXI5wOB2NBEYGW8u63pQpfzZua9mMPRsxstPl0J7MYmdvllHukR61Hguh6YI9E2auffzVk3ft9TrL0Q9rLV5Xz9qTK2vHsggASUNhL6hCEJTEIoCwoIgSIFtFoKOWk7UwIIV4DZR0ukjBEGNHt_ANz5PKs:1pz3pM:qJGfMe7vwtv3l4z1iO_XJ8M-rjvK7-kkr94y-XTDxVY','2023-05-30 23:11:32.039374'),('ylduweqjxzvefovees818cpb1o8qim69','.eJxVjEEOwiAURO_C2hCw_ALu7EXI5wOB2NBEYGW8u63pQpfzZua9mMPRsxstPl0J7MYmdvllHukR61Hguh6YI9E2auffzVk3ft9TrL0Q9rLV5Xz9qTK2vHsggASUNhL6hCEJTEIoCwoIgSIFtFoKOWk7UwIIV4DZR0ukjBEGNHt_ANz5PKs:1pz3pL:EfPePcZjOtHQAurRv4t_yPZ2RCWabEbxz3Tmdd56qt0','2023-05-30 23:11:31.211431');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_site` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (3,'http://kodex.duckdns.org','http://kodex.duckdns.org');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_association` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int NOT NULL,
  `lifetime` int NOT NULL,
  `assoc_type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_code`
--

DROP TABLE IF EXISTS `social_auth_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_code` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  KEY `social_auth_code_code_a2393167` (`code`),
  KEY `social_auth_code_timestamp_176b341f` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_code`
--

LOCK TABLES `social_auth_code` WRITE;
/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_nonce` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int NOT NULL,
  `salt` varchar(65) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_partial`
--

DROP TABLE IF EXISTS `social_auth_partial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_partial` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(32) NOT NULL,
  `next_step` smallint unsigned NOT NULL,
  `backend` varchar(32) NOT NULL,
  `data` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `social_auth_partial_token_3017fea3` (`token`),
  KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`),
  CONSTRAINT `social_auth_partial_chk_1` CHECK ((`next_step` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_partial`
--

LOCK TABLES `social_auth_partial` WRITE;
/*!40000 ALTER TABLE `social_auth_partial` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_partial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_auth_usersocialauth` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int NOT NULL,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  KEY `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` (`user_id`),
  KEY `social_auth_usersocialauth_uid_796e51dc` (`uid`),
  CONSTRAINT `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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

-- Dump completed on 2023-06-26 22:13:16
