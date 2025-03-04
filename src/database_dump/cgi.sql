-- MySQL dump 10.13  Distrib 9.2.0, for macos15.2 (arm64)
--
-- Host: localhost    Database: cgi
-- ------------------------------------------------------
-- Server version	8.0.41

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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add history',8,'add_history'),(30,'Can change history',8,'change_history'),(31,'Can delete history',8,'delete_history'),(32,'Can view history',8,'view_history');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'api','user'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'readApi','history'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-12 14:43:08.706143'),(2,'auth','0001_initial','2025-02-12 14:43:09.744829'),(3,'admin','0001_initial','2025-02-12 14:43:09.968333'),(4,'admin','0002_logentry_remove_auto_add','2025-02-12 14:43:09.982695'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-12 14:43:10.000353'),(6,'contenttypes','0002_remove_content_type_name','2025-02-12 14:43:10.171555'),(7,'auth','0002_alter_permission_name_max_length','2025-02-12 14:43:10.270744'),(8,'auth','0003_alter_user_email_max_length','2025-02-12 14:43:10.312408'),(9,'auth','0004_alter_user_username_opts','2025-02-12 14:43:10.319833'),(10,'auth','0005_alter_user_last_login_null','2025-02-12 14:43:10.395389'),(11,'auth','0006_require_contenttypes_0002','2025-02-12 14:43:10.400927'),(12,'auth','0007_alter_validators_add_error_messages','2025-02-12 14:43:10.412621'),(13,'auth','0008_alter_user_username_max_length','2025-02-12 14:43:10.503145'),(14,'auth','0009_alter_user_last_name_max_length','2025-02-12 14:43:10.625293'),(15,'auth','0010_alter_group_name_max_length','2025-02-12 14:43:10.668975'),(16,'auth','0011_update_proxy_permissions','2025-02-12 14:43:10.674485'),(17,'auth','0012_alter_user_first_name_max_length','2025-02-12 14:43:10.785405'),(18,'sessions','0001_initial','2025-02-12 14:43:10.844416'),(19,'api','0001_initial','2025-02-12 14:44:34.480743'),(20,'api','0002_delete_user','2025-02-12 14:58:49.363432'),(21,'readApi','0001_initial','2025-02-12 15:41:57.417638');
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
INSERT INTO `django_session` VALUES ('0cyq83vhmpat15nbm64rexpvl2gov2j0','eyJ1c2VyX2lkIjoyfQ:1toQgt:KpKCsXFvJjMPcMSSy2ylc2ZzaghYYbDNhmYbzRd5YsU','2025-03-02 17:31:55.608402'),('0tloh2cgqk69cuip7319obw57jqblzwl','eyJ1c2VyX2lkIjoxfQ:1toPW3:VRQ8ipXHLtk4lDbyz8EMOmuRpe_p2EyySKjbNn7fK_I','2025-03-15 16:16:39.520673'),('0z5ap3fnxz1h9aef3gi6bbyma09411j8','eyJ1c2VyX2lkIjoxfQ:1tojSU:RzFHvBm5y3HxA42wCNnw77FtzRF5fSf5R9LoMY57Q2U','2025-03-03 13:34:18.236106'),('12mi8cp3o9bih4tiv5fevawh0mr8rda0','eyJ1c2VyX2lkIjoyfQ:1toQYy:NXcCvvNgNNzz2a_u2qkgEVQelVsEKJQQmcGm9L7frTQ','2025-03-02 17:23:44.268094'),('1tbka3wtf661y1myzs8f60k07hff5bkx','eyJ1c2VyX2lkIjoxfQ:1toQB2:0PQJ6xGymMY_wj-Gy5OS6llRgG0MmprDOzH_1GpHX6Q','2025-03-02 16:59:00.084710'),('6gof5yuyhm8kbae4f14hnsqgbqpnqubp','eyJ1c2VyX2lkIjoxfQ:1toOiw:EtUDz2TpBzjwk9iw7gZcG7VY8xll2h-kju3EuKhUYJk','2025-03-15 15:25:54.412697'),('734n8fctfft5i02hcp4r3fpyi03gl1uj','eyJ1c2VyX2lkIjoxfQ:1toQy6:4_vh0XWjWw4kBFF9FAdUkoYk-lCK-10kdw0QPHNaufI','2025-03-02 17:49:42.195239'),('7a2ov7dwl8cqadhi3h9a3ih2fiwxjhil','eyJ1c2VyX2lkIjoxfQ:1tp8TY:KzJsr7iYmBE5V26GKjqYln406iD_OS-oiuvV15FM28w','2025-03-04 16:17:04.752462'),('8bzp8d8aigkqjmyij1qn8tvjvvb5qmd5','eyJ1c2VyX2lkIjoxfQ:1toPQQ:QGxlf7bzO27gpH_VG37UlSC09Uivf7sGpncSW_kuUQE','2025-03-15 16:10:50.604579'),('8cytently85ye84r8gktmaxkaub1ep6b','eyJ1c2VyX2lkIjoyfQ:1toisO:lZywbSMNYhthXSGEC3ie8jcmupL7auW2Ee4wWZCrSYo','2025-03-03 12:57:00.104566'),('8j02q4wff7wdjrojl5qucktj49d0ana1','eyJ1c2VyX2lkIjoxfQ:1toiXo:KgMmntVahEfPbvIZmjGfq3QlZU00q6dlyJ2E3IAcguA','2025-03-03 12:35:44.323182'),('8oyy47lv9u9i5bsdgpv7cxpmxau6utef','eyJ1c2VyX2lkIjoxfQ:1toiTN:2edxYTjONtAB-xmhOIJS3AD82MQfLA0XcLdordmFwls','2025-03-03 12:31:09.827453'),('90zq478ozsbple8u1by4nd6ue8eas01x','eyJ1c2VyX2lkIjoxfQ:1tpHET:ctPbERozodRyV3Ip_1T5bcgvRFMPRP8BW8R2kMkEvrw','2025-03-05 01:38:05.545855'),('91as5kioa8dukw0q4hc1z018ymzo3524','eyJ1c2VyX2lkIjoxfQ:1toPzM:o81PREa7nAPIsUbGkYS14Ox7lnvqIqPIEl8-ba_s8EE','2025-03-02 16:46:56.663681'),('a05tywzpg20mqklrmq89phcnpm4d5ll2','eyJ1c2VyX2lkIjoyfQ:1toQxv:3s9bFVonluEkuZRIWNmYv9SMThvHcgJy1fbndlOIxRQ','2025-03-02 17:49:31.723270'),('ahowl8xm4lmderpsp4xys4dmupfdownv','eyJ1c2VyX2lkIjoxfQ:1toQxU:rNzxX5lu_vBRM5LbKg1s-5NpszEsz8Q4FfqQtxHcTCk','2025-03-02 17:49:04.898107'),('akehohl7fz4rz831jju54y4idoc0lo3i','eyJ1c2VyX2lkIjoxfQ:1toiQX:nGU6fdV6klNzPQ6S91zG4XI7WryLRDvSt6AjKQlvDPg','2025-03-03 12:28:13.191998'),('anxuvkr6rx94hew6yt596axgs8pvc6n2','eyJ1c2VyX2lkIjoxfQ:1tpKLQ:CSYmZiGGXy4_QL4Gy88M_vVmtsGgzQlvtQRL7QOGspU','2025-03-05 04:57:28.271056'),('cpdxl6eqcqk5r7mrein0piw983rfc05q','eyJ1c2VyX2lkIjoxfQ:1toPmT:s_ZdBF0sPQwv2SQJ6KjIe2iRkruUMggSuvXM_MNEPVg','2025-03-15 16:33:37.463627'),('cwp6i1d6cj8quib243g358co9ri9rxos','eyJ1c2VyX2lkIjoyfQ:1toQ7R:Oxe18pISmBef9bhUjxow_FvWYcBvxgpSY1DIVHq8CaI','2025-03-02 16:55:17.497306'),('elv81ln1dpwvndkc33ro4we71efg8fk3','eyJ1c2VyX2lkIjoxfQ:1tpH7O:anviCXRPTVJhXVGtoRJ3XkikeM6zjz1LLHX3xrRVXI4','2025-03-05 01:30:46.355892'),('f14yttf5h6z6ho47h4d22aplnznp040r','eyJ1c2VyX2lkIjoxfQ:1tpHA1:h-3zXDfO3kym_rKAKLG7-8hNPDXxTJpSji5YPPWltic','2025-03-05 01:33:29.767568'),('f8zaroys3o6wts7kydbrnukds1r40wiq','eyJ1c2VyX2lkIjoxfQ:1toQuK:gGKWRmqMfdla8enaG_zqeaQmjFBmvaufChdcWjb8lO0','2025-03-02 17:45:48.072257'),('gi0oxldeb6iih4qgyck7y9nlu5aczqma','eyJ1c2VyX2lkIjoxfQ:1toQmh:bljllB4II9Tk1OBq-p0A6Lmj1uBLTcSiPfAX_W8HpeM','2025-03-02 17:37:55.427000'),('gidgyo4720fiisq722m7n6o45nljngee','eyJ1c2VyX2lkIjoxfQ:1tp472:P3LxwlHqYBUKFVMq5xcGAg_1cYVdlTHOh_2apksqtSE','2025-03-04 11:37:32.417148'),('guabchb4thmjfzunlcd211oatco1kjd4','eyJ1c2VyX2lkIjoxfQ:1toQKm:DZh0H8XxkqsgD30H_8KJAOmGN822xRBVIF_aQZnhkbU','2025-03-02 17:09:04.296554'),('gyhn69b4h1oin9wxefizzksw7hihsxjw','eyJ1c2VyX2lkIjoxfQ:1tois0:TQHN6pMIhRF6qfrwM3UwMuSGoRXhqcqbFDDrg8DmwPo','2025-03-03 12:56:36.278548'),('h9kxysk92vg5bxg7u2ojsw1j74mzpqiy','eyJ1c2VyX2lkIjoxfQ:1tpIQ0:8sI3gg7B9_Hj_iMW-DZ0P-tKybVEU2iAby6f3IchkIw','2025-03-05 02:54:04.137259'),('hbvgp16k6ej8tokh980qxsmlx977sazu','eyJ1c2VyX2lkIjoyfQ:1toQx0:CBlxm-axB7DSwefRXm10y_NPkljVq2cUCdGez5ucrUM','2025-03-02 17:48:34.792417'),('iqz9k2i3jd6ad3rs18sweishmcl5htgr','eyJ1c2VyX2lkIjoxfQ:1toPkW:W_xpHWZ6k7axet5AKQwJ27rICNAS29AYdiw4to3JVqE','2025-03-15 16:31:36.662923'),('jw4b3m59mpdqlmal5u6tzalswkg1xnsu','eyJ1c2VyX2lkIjoxfQ:1toPP8:zIoKdDH2gvbRg_qyinoKhrr1l1_x96zgJKk_3GBA6Zs','2025-03-15 16:09:30.811486'),('ld7xptnunrq7f1vdkk3e17sqh83uwg7l','eyJ1c2VyX2lkIjoxfQ:1tpHHo:e_gm8qVBKcdJqgnL_4PqxxHhaJBbqsxwSj5cqJ7Wt6k','2025-03-05 01:41:32.452187'),('lq9nlj55am470b4jnnfsaydhchg6nmpb','eyJ1c2VyX2lkIjoxfQ:1toQ5x:ujaaNeaJ6Wegbj7ZqTom8_l0KucawvqoaH5fvKnMaZI','2025-03-02 16:53:45.734448'),('r8oo837lssyj0x79pnyze7u1gy3no6m8','eyJ1c2VyX2lkIjoxfQ:1tpHCA:BGQi0fp8JBJ9r8aX6WratuuuVmBBDsgvP9v-cqdcj20','2025-03-05 01:35:42.686211'),('t67ubdgr287jspu7nvbawtilut6fib6t','eyJ1c2VyX2lkIjoyfQ:1toQSF:P0xpB8C6THQuYIVSbp2lQXo1AeSm4xoNhDpbGLMvzJ8','2025-03-02 17:16:47.210842'),('t83dlwn3ybx0r67ofja4qfkt5yj9jiv4','eyJ1c2VyX2lkIjoxfQ:1toQG6:aBZsEmoFeNNibxqs7wDQzfKVabaXQBG6nuHN1txXgsc','2025-03-02 17:04:14.302805'),('th4dvmn2ivn7v3kiv8z0qlmgrxi55qr8','eyJ1c2VyX2lkIjoxfQ:1toQwA:bpbhzCS1jzYx_hcdPRnPoe2Dl1s1e7huZPcUpHT59rc','2025-03-02 17:47:42.761775'),('ucfiln8685a0upd1h1s83kv3a6bnif4n','eyJ1c2VyX2lkIjoxfQ:1toikn:5PkncRfz84fjDsOoSHtGUViJVrQI2rsLbDowYSqQROE','2025-03-03 12:49:09.936499'),('udfll78unu6e0cwfvh3ey5yq0ysy2fy8','eyJ1c2VyX2lkIjoxfQ:1tp5hW:K9uTjwaDkQ5bX1igzJum34KMYVQUrBDZt3Wu3wVXymM','2025-03-04 13:19:18.680473'),('vc4k7b8txvcj2su32f5ifzt68w77o6rh','eyJ1c2VyX2lkIjoxfQ:1toPJY:o1uuHtBkKoFGGfA5D_JUguyYqMVLWEjLOUFes8L5_WY','2025-03-15 16:03:44.406337'),('w46lzo9yqunjnockrizfkyv56466ytos','eyJ1c2VyX2lkIjoxfQ:1tp2GF:HTJGK5Yu49EtrsLz7esVvC-lD9z43pN5lP0IQ_O-a54','2025-03-04 09:38:55.399752'),('wwn9z3s7xpl67oe6fzqw73wofxc36048','eyJ1c2VyX2lkIjoyfQ:1toQUP:jrt9FWdteV9WC3yzO5ib8Yy24aJO7usj9mXdyZkBfE0','2025-03-02 17:19:01.732257'),('x4p80ieckhzvl4xy2anltoy68cdh2k1j','eyJ1c2VyX2lkIjoxfQ:1toOpd:xlEFPO8Dug7W5LgDiR5nc1CbajysxyYUpONRKuViNYg','2025-03-15 15:32:49.446678'),('x912zykbn7cenl27vw7ldjjewt1ufq0o','eyJ1c2VyX2lkIjoyfQ:1tpH9J:XZvlAaOoa47qC4L8Z0dfOv2p7kDvYw5qm3euDXW9zvE','2025-03-05 01:32:45.582602'),('y6wwfeix62wi83my68m6q91w5fm46cns','eyJ1c2VyX2lkIjoyfQ:1tp5co:jmWdZNuE-KC8YZR1crBKRhchgDy1Xgz1ksJHSUpsiLQ','2025-03-04 13:14:26.732382'),('ylrfy6zpoisc1le8pyfrvmocus7ue24n','eyJ1c2VyX2lkIjoxfQ:1toQsl:dUrODSSMGn8Thb-b5M27UjZDIyA6SrLDFtSxCwNyR9c','2025-03-02 17:44:11.717646');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `photo` varchar(255) NOT NULL,
  `result` json NOT NULL,
  `summary` text NOT NULL,
  `target` json NOT NULL,
  `fullAnalysis` json NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,'2025-03-03 19:10:14','http://localhost:8000/media/uploads/461277069_961375746033879_5393122898144942911_n.jpg','{\"Relational\": 7, \"Informative\": 5, \"Remunerative\": 10, \"Entertainment\": 10}','To enhance the advertisement’s effectiveness, the primary focus should be on improving the informative and relational aspects while slightly toning down the remunerative and entertainment aspects. We recommend incorporating key details about the food, such as ingredients and benefits, and including messaging that fosters emotional connections with the target audience. Consider showing the food being enjoyed in a social setting or using language that resonates with customer values to increase the relational score. Simultaneously, ensure that the entertainment elements do not overshadow the informative content and that the remunerative appeal doesn\'t overshadow the product\'s inherent quality and benefits. These adjustments will lead to a more balanced and effective advertisement.','{\"relational\": 6, \"remunerative\": 7, \"entertainment\": 9, \"informational\": 4}','\"---\\n## **Detailed Optimization Plan**\\n### **1. Remunerative (Profit-Driven Appeal)**\\n**Target Score:** `7`\\n**Current Score:** `10`\\n**Assessment:** Exceeds Target!\\n**Recommended Improvements:** While a strong remunerative appeal is positive, consider subtly reducing its emphasis to allow for enhancements in other areas. This could involve slightly downplaying explicit price promotions or guarantees, and instead focusing on product benefits and customer experience. For example, if the poster has a large, bold price, consider reducing the font size slightly or replacing some of the emphasis with benefits.\\n\\n### **2. Informative (Conveying Essential Product Information)**\\n**Target Score:** `6`\\n**Current Score:** `5`\\n**Assessment:** Falls Short of Target!\\n**Recommended Improvements:** To enhance the informative aspect, the poster needs to clearly communicate key details about the food item. This could involve highlighting specific ingredients, preparation methods, nutritional information, or the food\'s origin. Adding a short, concise description of the food\'s unique selling points, benefits or preparation methods can improve the \'Informative\' score. Ensuring that important certifications (e.g., organic, gluten-free) are clearly displayed will also contribute to a higher score. If the advertisement features an image of the food, consider adding visual cues to show the textures and ingredients more clearly.\\n\\n### **3. Relational (Emotional and Social Connection)**\\n**Target Score:** `9`\\n**Current Score:** `7`\\n**Assessment:** Falls Short of Target!\\n**Recommended Improvements:** To improve the relational aspect, focus on fostering a stronger emotional and social connection with the audience. This can be achieved by incorporating imagery or messaging that evokes positive emotions, such as joy, nostalgia, or comfort. Showcasing the food being enjoyed in a social setting (e.g., a family meal, a gathering of friends) can create a sense of community and belonging. Alternatively, use language that speaks to the customer\'s values and aspirations. Use real people instead of overly-stylized stock photos can make the ad feel more genuine. Storytelling around the food item could also strengthen the emotional connection.\\n\\n### **4. Entertainment (Engagement and Attention-Grabbing Appeal)**\\n**Target Score:** `4`\\n**Current Score:** `10`\\n**Assessment:** Exceeds Target!\\n**Recommended Improvements:** While high entertainment value is desirable, it\'s currently overshadowing other aspects. To balance this, consider simplifying the overall design or reducing the intensity of the visual or verbal elements that contribute to entertainment. If the poster contains a humorous element, ensure that it doesn\'t distract from the core message. One approach is to use a more restrained color palette or layout.\\n\\n---\\n### **Summary**\\n\\nTo enhance the advertisement’s effectiveness, the primary focus should be on improving the informative and relational aspects while slightly toning down the remunerative and entertainment aspects. We recommend incorporating key details about the food, such as ingredients and benefits, and including messaging that fosters emotional connections with the target audience. Consider showing the food being enjoyed in a social setting or using language that resonates with customer values to increase the relational score. Simultaneously, ensure that the entertainment elements do not overshadow the informative content and that the remunerative appeal doesn\'t overshadow the product\'s inherent quality and benefits. These adjustments will lead to a more balanced and effective advertisement.\"',1),(2,'2025-03-03 19:11:11','http://localhost:8000/media/uploads/CDC937E1-B55C-4F2D-B3C4-DF92D8B5C836.jpeg','{\"Message\": \"Not a food picture\"}','To significantly enhance the advertisement’s effectiveness, the core problem, the image not being recognized as food, needs immediate correction. Beyond that, the advertisement needs to be more direct and enticing. Focus on clearly showcasing the food item with a high-quality image and conveying compelling information such as price promotions and key ingredients to quickly draw the viewer\'s attention and provide a reason to purchase. Incorporate elements that elicit emotional responses, such as depicting happy customers enjoying the food, and introduce engaging visual elements and copy to make the advertisement more memorable and impactful. The ad needs to both inform and invite the viewer to take action.','{\"relational\": 9, \"remunerative\": 4, \"entertainment\": 9, \"informational\": 9}','\"---\\n## **Detailed Optimization Plan**\\n### **1. Remunerative (Profit-Driven Appeal)**\\n**Target Score:** `4`  \\n**Current Score:** `0`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** Since the AI believes it\'s not a food picture, this is likely the core issue. Assuming it *is* a food picture and is simply being misinterpreted, ensure the imagery prominently features the product (the food) and is easily identifiable as food. Then, clearly state the price, special offers (e.g., discounts, bundle deals), or value proposition (e.g., \\\"best price in town,\\\" \\\"free delivery\\\") to create a sense of urgency and incentivize purchase. If the food item is associated with savings (e.g., a family meal deal), explicitly mention the savings amount or benefit of buying it now. A call to action like \\\"Order Now & Save!\\\" is crucial.\\n\\n### **2. Informative (Conveying Essential Product Information)**\\n**Target Score:** `9`  \\n**Current Score:** `0`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** Clearly identify the food item being advertised. Provide essential details like ingredients (if it\'s a selling point, e.g., \\\"made with fresh, local ingredients\\\"), nutritional information (e.g., \\\"low fat,\\\" \\\"high protein\\\"), portion size, or serving suggestions. Also, include details about where and how to purchase the food: the restaurant name, location (address, website), hours of operation, delivery options, and ordering methods (phone, online). If applicable, highlight any special preparations or cooking methods that make the food unique.\\n\\n### **3. Relational (Emotional and Social Connection)**\\n**Target Score:** `9`  \\n**Current Score:** `0`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** Invoke positive emotions through imagery and text. Use visuals that depict happy people enjoying the food, creating a sense of community and connection. Consider including testimonials or customer reviews to build trust and social proof. The copy should use evocative language that appeals to the senses, describing the taste, smell, and texture of the food in a mouthwatering way. Frame the food as something that brings people together or provides comfort.\\n\\n### **4. Entertainment (Engagement and Attention-Grabbing Appeal)**\\n**Target Score:** `9`  \\n**Current Score:** `0`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** Use high-quality, visually appealing imagery. A captivating photo or illustration is key to grabbing attention. If appropriate for the brand, use humor or puns related to the food item. Consider incorporating a playful design element or an interactive element (e.g., a QR code leading to a fun filter or a game). Make sure the advertisement is easily digestible and doesn\'t overload the viewer with too much information. The design should be visually striking and memorable.\\n---\\n### **Summary**\\nTo significantly enhance the advertisement’s effectiveness, the core problem, the image not being recognized as food, needs immediate correction. Beyond that, the advertisement needs to be more direct and enticing. Focus on clearly showcasing the food item with a high-quality image and conveying compelling information such as price promotions and key ingredients to quickly draw the viewer\'s attention and provide a reason to purchase. Incorporate elements that elicit emotional responses, such as depicting happy customers enjoying the food, and introduce engaging visual elements and copy to make the advertisement more memorable and impactful. The ad needs to both inform and invite the viewer to take action.\\n---\"',1),(3,'2025-03-03 20:58:54','http://localhost:8000/media/uploads/461277069_961375746033879_5393122898144942911_n.jpg','{\"Relational\": 0, \"Informative\": 4, \"Remunerative\": 6, \"Entertainment\": 6}','The advertisement requires significant enhancements across all four areas to meet its target values. Prioritizing the relational aspect, the ad needs to establish an emotional connection through relevant imagery and messaging that speaks to the target audience\'s social values. Secondly, a strong emphasis on conveying essential product information, including ingredients and benefits, is critical to address the informative shortfall. Alongside, the remunerative aspect needs bolstering by clearly highlighting pricing, discounts, or value propositions like bundle deals, to drive profit-driven appeal. Finally, inject a touch of humor or dynamic visuals for minor entertainment enhancement to boost the overall engagement. Implementing these recommendations will substantially improve the advertisement\'s effectiveness.','{\"relational\": 8, \"remunerative\": 9, \"entertainment\": 7, \"informational\": 7}','\"---\\n## **Detailed Optimization Plan**\\n### **1. Remunerative (Profit-Driven Appeal)**\\n**Target Score:** `9`  \\n**Current Score:** `6`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** To increase the remunerative appeal, the advertisement should clearly highlight the value proposition and potential cost savings or benefits for the customer. Specifically, include a more prominent display of pricing or discounts, such as a \\\"Limited Time Offer\\\" or \\\"Bundle Deal.\\\" Also, consider adding social proof, such as customer testimonials or reviews, emphasizing positive experiences with the product or service\'s value. Quantifiable benefits, like \\\"Save 20% on your first order\\\" or \\\"Enjoy a free drink with every meal,\\\" should be prominently displayed.\\n\\n### **2. Informative (Conveying Essential Product Information)**\\n**Target Score:** `8`  \\n**Current Score:** `4`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** The advertisement needs more essential product information. Incorporate key details about the food item, such as ingredients, nutritional value (e.g., \\\"Made with fresh, organic ingredients\\\"), preparation methods (e.g., \\\"Slow-cooked for ultimate flavor\\\"), or size/portion information. If there are any unique selling points (USPs), highlight them. For instance, if it\'s a healthy option, emphasize low calorie count or high protein content. Visual cues, like close-up shots of the product\'s texture or presentation, can also convey information effectively. Include allergen information clearly if applicable.\\n\\n### **3. Relational (Emotional and Social Connection)**\\n**Target Score:** `7`  \\n**Current Score:** `0`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** Currently, the advertisement lacks any emotional or social connection. To improve this, consider using imagery that evokes positive emotions, such as people enjoying the food together in a social setting (family, friends). Use inclusive language that makes the viewer feel welcomed and part of a community. Showcasing the food as part of a celebration or special occasion can also foster a relational connection. Include a tagline or message that resonates with the target audience\'s values and aspirations.\\n\\n### **4. Entertainment (Engagement and Attention-Grabbing Appeal)**\\n**Target Score:** `7`  \\n**Current Score:** `6`  \\n**Assessment:** Falls short of the target.\\n**Recommended Improvements:** While the entertainment score is relatively close to the target, minor adjustments can improve it. Use a more captivating headline or tagline that immediately grabs the viewer\'s attention. Consider incorporating a sense of humor or playfulness into the advertisement\'s design or messaging. Dynamic visuals, such as animated elements or a striking image, can also enhance engagement. If possible, integrate a call to action that encourages interaction, such as a QR code leading to a fun interactive experience or a social media contest related to the food item.\\n\\n---\\n### **Summary**\\nThe advertisement requires significant enhancements across all four areas to meet its target values. Prioritizing the relational aspect, the ad needs to establish an emotional connection through relevant imagery and messaging that speaks to the target audience\'s social values. Secondly, a strong emphasis on conveying essential product information, including ingredients and benefits, is critical to address the informative shortfall. Alongside, the remunerative aspect needs bolstering by clearly highlighting pricing, discounts, or value propositions like bundle deals, to drive profit-driven appeal. Finally, inject a touch of humor or dynamic visuals for minor entertainment enhancement to boost the overall engagement. Implementing these recommendations will substantially improve the advertisement\'s effectiveness.\"',1);
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `readapi_history`
--

DROP TABLE IF EXISTS `readapi_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `readapi_history` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `event_name` varchar(255) NOT NULL,
  `event_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `readapi_history`
--

LOCK TABLES `readapi_history` WRITE;
/*!40000 ALTER TABLE `readapi_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `readapi_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `photo_url` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Timz','Timz@gmail.com','pbkdf2_sha256$870000$UfaxwUvOR4fDbGHp4XPMNz$4pkbxSqSMo2wQbGZC2o4Zkn57G44jOpgfLLdFgEEkw8=',''),(2,'Bonz','Bonz@gmail.com','pbkdf2_sha256$870000$tNZaRiuDw6ShHwZvh2EmuJ$zyAlTyE26eJW9PKTMgaQneP1bJPC9X2D96SA4wBMUC0=','');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-04 14:35:30
