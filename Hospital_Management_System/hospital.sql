-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2022 at 05:08 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `Appointment_Id` varchar(15) NOT NULL,
  `patient_id` varchar(10) NOT NULL,
  `doctor_id` varchar(10) NOT NULL,
  `Appointment_Date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`Appointment_Id`, `patient_id`, `doctor_id`, `Appointment_Date`) VALUES
('145', '312', '34', '2021-04-03 00:00:00'),
('A116', '110', '112', '2019-08-13 10:07:02'),
('A119', '300', '500', '2017-10-24 12:27:06'),
('A202', '400', '112', '2015-12-06 15:04:02'),
('A210', '212', '319', '2018-05-30 12:30:10'),
('A215', '115', '210', '2019-07-15 14:48:02'),
('A216', '123', '215', '2015-08-15 17:38:38'),
('A236', '111', '800', '2012-11-15 12:50:48'),
('A326', '456', '555', '2017-12-20 18:10:59');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add appointment', 7, 'add_appointment'),
(26, 'Can change appointment', 7, 'change_appointment'),
(27, 'Can delete appointment', 7, 'delete_appointment'),
(28, 'Can view appointment', 7, 'view_appointment'),
(29, 'Can add bed', 8, 'add_bed'),
(30, 'Can change bed', 8, 'change_bed'),
(31, 'Can delete bed', 8, 'delete_bed'),
(32, 'Can view bed', 8, 'view_bed'),
(33, 'Can add blood donate', 9, 'add_blooddonate'),
(34, 'Can change blood donate', 9, 'change_blooddonate'),
(35, 'Can delete blood donate', 9, 'delete_blooddonate'),
(36, 'Can view blood donate', 9, 'view_blooddonate'),
(37, 'Can add doctor', 10, 'add_doctor'),
(38, 'Can change doctor', 10, 'change_doctor'),
(39, 'Can delete doctor', 10, 'delete_doctor'),
(40, 'Can view doctor', 10, 'view_doctor'),
(41, 'Can add medicine', 11, 'add_medicine'),
(42, 'Can change medicine', 11, 'change_medicine'),
(43, 'Can delete medicine', 11, 'delete_medicine'),
(44, 'Can view medicine', 11, 'view_medicine'),
(45, 'Can add nurse', 12, 'add_nurse'),
(46, 'Can change nurse', 12, 'change_nurse'),
(47, 'Can delete nurse', 12, 'delete_nurse'),
(48, 'Can view nurse', 12, 'view_nurse'),
(49, 'Can add organ donate', 13, 'add_organdonate'),
(50, 'Can change organ donate', 13, 'change_organdonate'),
(51, 'Can delete organ donate', 13, 'delete_organdonate'),
(52, 'Can view organ donate', 13, 'view_organdonate'),
(53, 'Can add patient', 14, 'add_patient'),
(54, 'Can change patient', 14, 'change_patient'),
(55, 'Can delete patient', 14, 'delete_patient'),
(56, 'Can view patient', 14, 'view_patient'),
(57, 'Can add story', 15, 'add_story'),
(58, 'Can change story', 15, 'change_story'),
(59, 'Can delete story', 15, 'delete_story'),
(60, 'Can view story', 15, 'view_story'),
(61, 'Can add test', 16, 'add_test'),
(62, 'Can change test', 16, 'change_test'),
(63, 'Can delete test', 16, 'delete_test'),
(64, 'Can view test', 16, 'view_test'),
(65, 'Can add user1', 17, 'add_user1'),
(66, 'Can change user1', 17, 'change_user1'),
(67, 'Can delete user1', 17, 'delete_user1'),
(68, 'Can view user1', 17, 'view_user1'),
(69, 'Can add user', 18, 'add_user'),
(70, 'Can change user', 18, 'change_user'),
(71, 'Can delete user', 18, 'delete_user'),
(72, 'Can view user', 18, 'view_user');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `bed`
--

CREATE TABLE `bed` (
  `bed_id` varchar(30) NOT NULL,
  `Bed_Type` varchar(15) NOT NULL,
  `Vacancy` enum('Y','N') NOT NULL,
  `Bed_Charge` mediumint(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bed`
--

INSERT INTO `bed` (`bed_id`, `Bed_Type`, `Vacancy`, `Bed_Charge`) VALUES
('1150', 'Ward', 'N', 2300),
('1236', 'ICU', 'N', 7000),
('134', 'ICU', 'N', 15000),
('1504', 'WARD', 'N', 2000),
('2500', 'ICU', 'N', 7000),
('53', 'Ward', 'N', 2500),
('8455', 'Cabin', 'N', 4000),
('8536', 'Cabin', 'N', 3000);

-- --------------------------------------------------------

--
-- Table structure for table `blood_donate`
--

CREATE TABLE `blood_donate` (
  `patient_id` varchar(10) NOT NULL,
  `user_id` varchar(10) NOT NULL,
  `blood_group` varchar(5) NOT NULL,
  `contact_num` varchar(11) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `need_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blood_donate`
--

INSERT INTO `blood_donate` (`patient_id`, `user_id`, `blood_group`, `contact_num`, `location`, `need_date`) VALUES
('123', '234', 'AB+', '01798345690', 'Lalbag', '2021-04-06');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'hello', 'appointment'),
(8, 'hello', 'bed'),
(9, 'hello', 'blooddonate'),
(10, 'hello', 'doctor'),
(11, 'hello', 'medicine'),
(12, 'hello', 'nurse'),
(13, 'hello', 'organdonate'),
(14, 'hello', 'patient'),
(15, 'hello', 'story'),
(16, 'hello', 'test'),
(18, 'hello', 'user'),
(17, 'hello', 'user1'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-28 03:45:40.668410'),
(2, 'auth', '0001_initial', '2021-12-28 03:45:41.307688'),
(3, 'admin', '0001_initial', '2021-12-28 03:45:41.438430'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-12-28 03:45:41.447904'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-28 03:45:41.460221'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-12-28 03:45:41.537536'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-12-28 03:45:41.588290'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-12-28 03:45:41.617525'),
(9, 'auth', '0004_alter_user_username_opts', '2021-12-28 03:45:41.642779'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-12-28 03:45:41.705145'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-12-28 03:45:41.709931'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-12-28 03:45:41.724170'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-12-28 03:45:41.753396'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-12-28 03:45:41.784157'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-12-28 03:45:41.806613'),
(16, 'auth', '0011_update_proxy_permissions', '2021-12-28 03:45:41.821842'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-12-28 03:45:41.842375'),
(18, 'sessions', '0001_initial', '2021-12-28 03:45:41.890395'),
(19, 'hello', '0001_initial', '2021-12-28 03:58:21.262429'),
(20, 'hello', '0002_user1', '2021-12-28 04:22:25.717580'),
(21, 'hello', '0003_user', '2021-12-31 10:02:17.379780');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `Doctorid` varchar(6) NOT NULL,
  `user_id` varchar(10) NOT NULL,
  `Doctor_Name` varchar(15) NOT NULL,
  `contact_num` varchar(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `meet_link` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`Doctorid`, `user_id`, `Doctor_Name`, `contact_num`, `email`, `meet_link`) VALUES
('106', '110', 'Soniya Jaman', '01723455678', 'sonia@gmail.com', 'fjahfhwogow'),
('126', '456', 'Robert Adler', '01723455655', 'robert@gmail.com', 'vdaifhwogwog3'),
('145', '233', 'Arfaqur Rahman', '0172345533', 'arfaqur', 'bfwihwoggphhp'),
('215', '676', 'Rakesh Khan', '01723455444', 'rakesh@gmail.com', 'qifhoghogh3h'),
('256', '111', 'Shariar Mim', '01723455333', 'mim@gmail.com', 'fwifhwogj3phjp'),
('435', '123', 'piyash', '01734567345', 'piyash@gmail.com', 'dfwghju6k6k');

-- --------------------------------------------------------

--
-- Table structure for table `hello_user1`
--

CREATE TABLE `hello_user1` (
  `id` bigint(20) NOT NULL,
  `username` varchar(30) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `repassword` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `Medicine Id` varchar(15) NOT NULL,
  `Medicine Name` varchar(20) NOT NULL,
  `patient_id` varchar(10) NOT NULL,
  `Expired Date` datetime NOT NULL,
  `Price` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`Medicine Id`, `Medicine Name`, `patient_id`, `Expired Date`, `Price`) VALUES
('1', 'Ampicillin', '121', '2025-02-12 12:10:11', 30),
('2', 'Didanosine', '210', '2025-03-22 11:19:13', 20),
('3', 'Furosemide', '310', '2030-11-20 11:19:13', 45),
('4', 'Linezolid', '114', '2022-04-14 11:19:13', 22),
('45', 'Moxacil', '456', '2024-05-06 00:00:00', 60),
('5', 'Melphalan', '455', '2029-09-17 12:22:24', 10),
('6', 'Melphalan', '232', '2029-11-17 11:22:21', 75);

-- --------------------------------------------------------

--
-- Table structure for table `nurse`
--

CREATE TABLE `nurse` (
  `Nurse_ID` varchar(6) NOT NULL,
  `Nurse_Name` varchar(15) NOT NULL,
  `Floor_No` tinyint(4) NOT NULL,
  `Bed_No` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `nurse`
--

INSERT INTO `nurse` (`Nurse_ID`, `Nurse_Name`, `Floor_No`, `Bed_No`) VALUES
('234', 'Arju', 127, ''),
('320', 'Shetu', 1, '1150'),
('400', 'Diya', 1, '1236'),
('500', 'Tahira', 1, '1504'),
('515', 'Shornali', 9, '2500'),
('610', 'Atia', 1, '53'),
('630', 'Khadija', 8, '8455'),
('660', 'Nabila', 8, '8536'),
('700', 'Prity', 9, '9050');

-- --------------------------------------------------------

--
-- Table structure for table `organ_donate`
--

CREATE TABLE `organ_donate` (
  `patient_id` varchar(10) NOT NULL,
  `user_id` varchar(10) NOT NULL,
  `blood_group` varchar(5) NOT NULL,
  `contact_num` varchar(11) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `need_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `organ_donate`
--

INSERT INTO `organ_donate` (`patient_id`, `user_id`, `blood_group`, `contact_num`, `location`, `need_date`) VALUES
('345', '123', 'B+', '01956784545', 'Kalabagan', '2018-02-03');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `Patient_Id` varchar(5) NOT NULL,
  `Patient_Name` varchar(20) NOT NULL,
  `contact_num` varchar(11) NOT NULL,
  `Age` tinyint(4) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `patient_blood_group` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`Patient_Id`, `Patient_Name`, `contact_num`, `Age`, `Address`, `patient_blood_group`) VALUES
('100', 'Jubaida', '01723455633', 52, '100,Barisal Sadar,Barisal', 'A+'),
('1100', 'Jalil', '01723455444', 23, '64, Rampura, Dhaka', 'AB+'),
('1123', 'Raju', '01723455222', 59, '900,Kalihati,Tangail', 'AB+'),
('1423', 'Farukh', '01723455333', 63, '25,Agrabad,Chittagong', 'B+'),
('200', 'Haris', '01723455333', 19, '74,Gulshan,Dhaka', 'A+'),
('217', 'Karim', '01723455333', 45, '125/B,Bashundhara,Dhaka', 'A+'),
('3120', 'Hasan', '01723455444', 9, '32,Maghbazar,Dhaka', 'AB+');

-- --------------------------------------------------------

--
-- Table structure for table `story`
--

CREATE TABLE `story` (
  `patient_id` varchar(10) NOT NULL,
  `story_date` date NOT NULL,
  `comment` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `story`
--

INSERT INTO `story` (`patient_id`, `story_date`, `comment`) VALUES
('354', '2016-05-02', 'My experience was good');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `Test_Id` varchar(6) NOT NULL,
  `Patient_ID` varchar(5) NOT NULL,
  `test_charge` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`Test_Id`, `Patient_ID`, `test_charge`) VALUES
('150', '100', 600),
('155', '217', 500),
('170', '1100', 5000),
('180', '5320', 5000),
('230', '8901', 5000),
('250', '1123', 50000),
('260', '9002', 7000),
('280', '3120', 7000),
('350', '1423', 5000),
('450', '200', 1000),
('560', '389', 1000),
('650', '3621', 10000),
('850', '459', 1200);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(7) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `blood_group` varchar(3) NOT NULL,
  `age` varchar(3) NOT NULL,
  `email` varchar(30) NOT NULL,
  `user_type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_name`, `address`, `blood_group`, `age`, `email`, `user_type`) VALUES
(234, 'Arfaqur', 'Lalbag', 'B+', '24', 'arfaqur@gmail.com', 'Patient');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`Appointment_Id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `bed`
--
ALTER TABLE `bed`
  ADD PRIMARY KEY (`bed_id`);

--
-- Indexes for table `blood_donate`
--
ALTER TABLE `blood_donate`
  ADD PRIMARY KEY (`patient_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`Doctorid`);

--
-- Indexes for table `hello_user1`
--
ALTER TABLE `hello_user1`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`Medicine Id`);

--
-- Indexes for table `nurse`
--
ALTER TABLE `nurse`
  ADD PRIMARY KEY (`Nurse_ID`),
  ADD KEY `FK_nurse_bed` (`Bed_No`);

--
-- Indexes for table `organ_donate`
--
ALTER TABLE `organ_donate`
  ADD PRIMARY KEY (`patient_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`Patient_Id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`Test_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `hello_user1`
--
ALTER TABLE `hello_user1`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
