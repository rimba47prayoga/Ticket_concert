-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2018 at 05:41 PM
-- Server version: 10.2.11-MariaDB
-- PHP Version: 7.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ticket_concert`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add album', 7, 'add_album'),
(20, 'Can change album', 7, 'change_album'),
(21, 'Can delete album', 7, 'delete_album'),
(22, 'Can add cart', 8, 'add_cart'),
(23, 'Can change cart', 8, 'change_cart'),
(24, 'Can delete cart', 8, 'delete_cart'),
(25, 'Can add event', 9, 'add_event'),
(26, 'Can change event', 9, 'change_event'),
(27, 'Can delete event', 9, 'delete_event'),
(28, 'Can add music', 10, 'add_music'),
(29, 'Can change music', 10, 'change_music'),
(30, 'Can delete music', 10, 'delete_music'),
(31, 'Can add ticket_transaction', 11, 'add_ticket_transaction'),
(32, 'Can change ticket_transaction', 11, 'change_ticket_transaction'),
(33, 'Can delete ticket_transaction', 11, 'delete_ticket_transaction'),
(34, 'Can add transaction_info', 12, 'add_transaction_info'),
(35, 'Can change transaction_info', 12, 'change_transaction_info'),
(36, 'Can delete transaction_info', 12, 'delete_transaction_info'),
(37, 'Can add user profile', 13, 'add_userprofile'),
(38, 'Can change user profile', 13, 'change_userprofile'),
(39, 'Can delete user profile', 13, 'delete_userprofile'),
(40, 'Can add application', 14, 'add_application'),
(41, 'Can change application', 14, 'change_application'),
(42, 'Can delete application', 14, 'delete_application'),
(43, 'Can add access token', 15, 'add_accesstoken'),
(44, 'Can change access token', 15, 'change_accesstoken'),
(45, 'Can delete access token', 15, 'delete_accesstoken'),
(46, 'Can add grant', 16, 'add_grant'),
(47, 'Can change grant', 16, 'change_grant'),
(48, 'Can delete grant', 16, 'delete_grant'),
(49, 'Can add refresh token', 17, 'add_refreshtoken'),
(50, 'Can change refresh token', 17, 'change_refreshtoken'),
(51, 'Can delete refresh token', 17, 'delete_refreshtoken'),
(52, 'Can add cors model', 18, 'add_corsmodel'),
(53, 'Can change cors model', 18, 'change_corsmodel'),
(54, 'Can delete cors model', 18, 'delete_corsmodel');

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
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$0d2GywsLStsW$0U5oUjIoBz+cWfKvv0q7JMwJuE/rcQxvHRh6X/hccLA=', '2018-04-29 17:39:56.759567', 1, 'admin', '', '', 'admin@admin.com', 1, 1, '2018-04-26 21:28:37.470257'),
(4, 'pbkdf2_sha256$100000$nbe6YsxUXHOt$NmQZj1HI5InnyK8sxFmeg7zebeY7ZgvWgxT/arn11H0=', '2018-04-29 22:40:33.612206', 0, 'rimba47prayoga', 'Rimba', 'Prayoga', 'rimba47prayoga@gmail.com', 0, 1, '2018-04-27 00:20:52.836389'),
(5, 'pbkdf2_sha256$100000$4CFRNLCapXAA$QeVu+jOnqniQ296TNHprTTJI3GPIobmm4rf94LVuxYQ=', '2018-04-27 14:57:48.996090', 0, 'rimba28prayoga', 'Rimba', 'Prayoga', 'rimba28prayoga@gmail.com', 0, 1, '2018-04-27 14:57:47.987032'),
(6, 'pbkdf2_sha256$100000$VJk1pyo5dxbg$jIsXxhBv5oT4dVrbBem4a7n2eWvHCAECuphy/M43uBk=', '2018-04-27 15:05:28.848392', 0, 'rimba27prayoga', 'Rimba', 'Prayoga', 'rimba27prayoga@gmail.com', 0, 1, '2018-04-27 15:05:28.080348'),
(13, 'pbkdf2_sha256$100000$PourJOuTwJaZ$tgtRAxXcHOVenG38LGROYYfkHZw0yMvv9EAr9N3zvYE=', NULL, 0, 'rimba23prayoga', 'Rimba', 'Prayoga', 'rimba23prayoga@gmail.com', 0, 1, '2018-04-27 21:30:41.162341');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(18, 'corsheaders', 'corsmodel'),
(7, 'music', 'album'),
(8, 'music', 'cart'),
(9, 'music', 'event'),
(10, 'music', 'music'),
(11, 'music', 'ticket_transaction'),
(12, 'music', 'transaction_info'),
(13, 'music', 'userprofile'),
(15, 'oauth2_provider', 'accesstoken'),
(14, 'oauth2_provider', 'application'),
(16, 'oauth2_provider', 'grant'),
(17, 'oauth2_provider', 'refreshtoken'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-04-29 22:20:19.547766'),
(2, 'auth', '0001_initial', '2018-04-29 22:20:28.606284'),
(3, 'admin', '0001_initial', '2018-04-29 22:20:30.188374'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-04-29 22:20:30.229377'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-04-29 22:20:31.103427'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-04-29 22:20:31.962476'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-04-29 22:20:32.703518'),
(8, 'auth', '0004_alter_user_username_opts', '2018-04-29 22:20:32.764522'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-04-29 22:20:33.221548'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-04-29 22:20:33.295552'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-04-29 22:20:33.345555'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-04-29 22:20:34.852641'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-04-29 22:20:35.560681'),
(14, 'music', '0001_initial', '2018-04-29 22:20:45.462248'),
(15, 'oauth2_provider', '0001_initial', '2018-04-29 22:20:52.105628'),
(16, 'oauth2_provider', '0002_08_updates', '2018-04-29 22:20:54.460762'),
(17, 'oauth2_provider', '0003_auto_20160316_1503', '2018-04-29 22:20:55.622829'),
(18, 'oauth2_provider', '0004_auto_20160525_1623', '2018-04-29 22:20:56.498879'),
(19, 'oauth2_provider', '0005_auto_20170514_1141', '2018-04-29 22:21:11.882759'),
(20, 'oauth2_provider', '0006_auto_20171214_2232', '2018-04-29 22:21:15.026939'),
(21, 'sessions', '0001_initial', '2018-04-29 22:21:15.537968');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3czmgm96madmazoz7c4r3t8nvj6g0jqj', 'OWFkZWI3OTBkYWI5YTEyN2JkNjBhOTAyMmY5OWU3OGM3ZjdiODE5MDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNzY5OTIxOTRiOGFmZmQ3YTU2NjkxNDQxYTJlNDY2YjY5MTJmM2NkIiwidG9rX2hyIjoyMywidG9rX21pbiI6NDF9', '2018-05-13 22:41:25.724187');

-- --------------------------------------------------------

--
-- Table structure for table `music_album`
--

CREATE TABLE `music_album` (
  `idapp` int(11) NOT NULL,
  `nameapp` varchar(125) NOT NULL,
  `release_date` date NOT NULL,
  `genre` varchar(250) DEFAULT NULL,
  `picture` varchar(100) DEFAULT NULL,
  `descriptions` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_album`
--

INSERT INTO `music_album` (`idapp`, `nameapp`, `release_date`, `genre`, `picture`, `descriptions`) VALUES
(1, 'Revolutions Radio', '2016-10-07', 'Punk rock, Punk pop, Rock alternatif', 'Revolutions_Radio.jpg', 'This new album, “Revolution Radio” is a dream come true. It’s a punk band in their 40’s showing the youngsters how it’s done. The sound is reminiscent of American Idiot and 21st Century Breakdown (2 of their best-selling albums), yet takes on new territory. From start to finish, this album showcases the many styles of Green Day from folk (Somewhere Now) to Dance-punk (Say Goodbye) to arena rock (Forever Now) to classic Green Day-style punk rock (Bang Bang, Too Dumb to Die, and more). I know I have loved just about everything they have put out, and probably always will. But this album is amazing!'),
(2, 'American Idiot', '2004-09-20', 'Punk rock, Punk pop, Opera rock, Rock alternatif, Pop rock', 'American_idiot.jpg', 'The first original album since 2000 from modern rock superheroes Green Day, American Idiot is one of the most anticipated and controversial albums of the year. Scathing yet self-effacing as it tells the tale of Green Day''s Billie Joe Armstrong, American Idiot is the punk rock epic. "A bold, polished punk opera." (Entertainment Weekly) "They''re the biggest, most successful, punk band the world has ever seen. What''s more, Green Day''s next album may well be their masterpiece." (Kerrang!)'),
(3, '21st Century Breakdown', '2009-05-15', 'Musik rok, Punk rock, Punk pop, Rock alternatif, Opera rock, Power pop', '21st_Century_Breakdown_Album.jpg', '21st Century Breakdown is the eighth studio album by American punk rock band Green Day, released on May 15, 2009 through Reprise Records. It is the band''s second rock opera, following American Idiot (2004), and their first album to be produced by Butch Vig. Green Day commenced work on the record in January 2006 and forty-five songs were written by vocalist/guitarist Billie Joe Armstrong by October 2007, but the band members did not enter studio work until January 2008.');

-- --------------------------------------------------------

--
-- Table structure for table `music_cart`
--

CREATE TABLE `music_cart` (
  `idapp` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_cart`
--

INSERT INTO `music_cart` (`idapp`, `quantity`, `ticket_id`, `user_id`) VALUES
(34, 3, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `music_event`
--

CREATE TABLE `music_event` (
  `idapp` int(11) NOT NULL,
  `total_ticket` int(11) NOT NULL,
  `ticket_date` datetime(6) NOT NULL,
  `location` varchar(120) NOT NULL,
  `price` decimal(30,2) NOT NULL,
  `descriptions` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_event`
--

INSERT INTO `music_event` (`idapp`, `total_ticket`, `ticket_date`, `location`, `price`, `descriptions`) VALUES
(1, 9969, '2018-05-26 21:33:11.000000', 'Jakarta, Arena Pekan Raya Jakarta (PRJ).', '1500000.00', 'There''s No Descriptions'),
(2, 9982, '2018-05-25 17:01:46.000000', 'Surabaya', '150000.00', 'There''s No Descriptions'),
(3, 9995, '2018-05-05 20:00:00.000000', 'ICC, Sidney , Australia', '2875000.00', 'There''s No Descriptions'),
(4, 10000, '2018-04-27 21:30:00.000000', 'Los Angeles, USA', '2534000.00', 'There''s No Descriptions'),
(5, 20000, '2018-05-29 22:00:00.000000', 'Amalie Arena, Tampa, America Serikat', '3145000.00', 'There''s No Descriptions'),
(6, 30000, '2018-06-01 15:00:00.000000', 'Parc de Can Zam, Santa coloma, Spanyol', '5134000.00', 'There''s No Descriptions');

-- --------------------------------------------------------

--
-- Table structure for table `music_event_ticket_for`
--

CREATE TABLE `music_event_ticket_for` (
  `id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  `music_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_event_ticket_for`
--

INSERT INTO `music_event_ticket_for` (`id`, `event_id`, `music_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 2),
(6, 2, 3),
(7, 2, 4),
(8, 2, 5),
(9, 3, 13),
(10, 3, 14),
(11, 3, 15),
(12, 3, 16),
(13, 3, 17),
(14, 3, 18),
(15, 4, 12),
(16, 4, 14),
(17, 4, 15),
(18, 4, 16),
(19, 4, 17),
(20, 4, 18),
(21, 5, 4),
(22, 5, 5),
(23, 5, 6),
(24, 5, 7),
(25, 5, 11),
(26, 5, 12),
(27, 5, 13),
(28, 5, 16),
(29, 6, 4),
(30, 6, 5),
(31, 6, 6),
(32, 6, 15),
(33, 6, 17),
(34, 6, 18);

-- --------------------------------------------------------

--
-- Table structure for table `music_music`
--

CREATE TABLE `music_music` (
  `idapp` int(11) NOT NULL,
  `nameapp` varchar(150) NOT NULL,
  `durations` varchar(4) DEFAULT NULL,
  `createddate` datetime(6) NOT NULL,
  `album_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_music`
--

INSERT INTO `music_music` (`idapp`, `nameapp`, `durations`, `createddate`, `album_id`) VALUES
(1, 'Stay The Night', '3:14', '2018-04-21 08:40:32.080965', 1),
(2, 'Missing You', '3:46', '2018-04-21 08:40:54.550250', 1),
(3, 'American Idiot', '2:54', '2018-04-22 07:51:36.203002', 2),
(4, 'Holiday', '4:14', '2018-04-22 07:52:12.351069', 2),
(5, 'Give Me Novacaine', '5:26', '2018-04-22 07:52:56.912618', 2),
(6, 'Somewhere now', '4:09', '2018-04-27 16:00:06.330853', 1),
(7, 'Bang bang', '3:25', '2018-04-27 16:00:29.805196', 1),
(8, 'Revolution Radio', '3:00', '2018-04-27 16:01:01.674019', 1),
(9, 'Too Dumb to Die', '3:23', '2018-04-27 16:01:44.253454', 1),
(10, 'Ordinary World', '3:00', '2018-04-27 16:02:11.810030', 1),
(11, 'Boulevard of Broken Dreams', '4:22', '2018-04-27 16:03:36.170856', 2),
(12, 'Know your Enemy', '3:11', '2018-04-27 16:08:17.080923', 3),
(13, '21st Century Breakdown', '5:09', '2018-04-27 16:09:07.747821', 3),
(14, '!Viva La Gloria!', '3:31', '2018-04-27 16:10:36.440894', 3),
(15, 'Last Night on Earth', '3:57', '2018-04-27 16:11:00.238255', 3),
(16, '21 Guns', '5:21', '2018-04-27 16:11:17.637250', 3),
(17, 'Boulevard of Broken Dreams', '4:41', '2018-04-27 16:11:37.978413', 3),
(18, 'American Idiot', '4:18', '2018-04-27 16:12:11.064306', 3);

-- --------------------------------------------------------

--
-- Table structure for table `music_ticket_transaction`
--

CREATE TABLE `music_ticket_transaction` (
  `idapp` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_purchase` int(11) DEFAULT NULL,
  `createddate` datetime(6) NOT NULL,
  `modifieddate` datetime(6) NOT NULL,
  `info_id` int(11) DEFAULT NULL,
  `ticket_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_ticket_transaction`
--

INSERT INTO `music_ticket_transaction` (`idapp`, `quantity`, `total_purchase`, `createddate`, `modifieddate`, `info_id`, `ticket_id`, `user_id`) VALUES
(8, 3, NULL, '2018-04-26 23:02:13.234449', '2018-04-27 11:22:30.618701', 1, 1, 1),
(9, 1, NULL, '2018-04-26 23:02:13.239449', '2018-04-27 11:22:23.519295', 1, 2, 1),
(10, 5, NULL, '2018-04-26 23:17:14.276984', '2018-04-27 11:22:09.373486', 1, 2, 1),
(11, 3, NULL, '2018-04-27 14:12:05.339163', '2018-04-27 14:12:05.339163', NULL, 1, 4),
(12, 4, NULL, '2018-04-27 14:14:10.486321', '2018-04-27 14:14:10.486321', NULL, 2, 4),
(13, 2, 600000, '2018-04-27 15:47:43.132345', '2018-04-27 15:47:43.132345', 2, 1, 4),
(14, 1, 250000, '2018-04-27 15:53:54.504586', '2018-04-27 15:53:54.504586', 2, 2, 4),
(15, 2, 600000, '2018-04-27 15:54:42.780347', '2018-04-27 15:54:42.780347', 2, 1, 4),
(16, 10, 3000000, '2018-04-27 15:56:29.493451', '2018-04-27 15:56:29.493451', 2, 1, 4),
(17, 2, 300000, '2018-04-28 18:08:10.134478', '2018-04-28 18:08:10.134478', 1, 2, 1),
(18, 2, 3000000, '2018-04-28 18:08:10.137478', '2018-04-28 18:08:10.137478', 1, 1, 1),
(19, 3, 4500000, '2018-04-28 18:09:00.808376', '2018-04-28 18:09:00.808376', 1, 1, 1),
(20, 1, 150000, '2018-04-28 18:09:00.810377', '2018-04-28 18:09:00.811377', 1, 2, 1),
(21, 1, 1500000, '2018-04-28 18:12:23.376963', '2018-04-28 18:12:23.376963', 1, 1, 1),
(22, 1, 150000, '2018-04-28 18:12:23.379963', '2018-04-28 18:12:23.379963', 1, 2, 1),
(23, 2, 3000000, '2018-04-29 00:51:46.295563', '2018-04-29 00:51:46.295563', 3, 1, 4),
(24, 3, 450000, '2018-04-29 18:44:35.325398', '2018-04-29 18:44:35.325398', 1, 2, 1),
(25, 5, 14375000, '2018-04-29 18:44:44.995952', '2018-04-29 18:44:44.995952', 1, 3, 1),
(26, 3, 4500000, '2018-04-29 18:44:52.450378', '2018-04-29 18:44:52.450378', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `music_transaction_info`
--

CREATE TABLE `music_transaction_info` (
  `idapp` int(11) NOT NULL,
  `no_telp` varchar(15) DEFAULT NULL,
  `province` varchar(50) DEFAULT NULL,
  `code_pos` varchar(10) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `createddate` datetime(6) NOT NULL,
  `modifieddate` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_transaction_info`
--

INSERT INTO `music_transaction_info` (`idapp`, `no_telp`, `province`, `code_pos`, `city`, `address`, `createddate`, `modifieddate`, `user_id`) VALUES
(1, '089454512211', 'Jawa Barat', '40512', 'Cimahi', 'Dasdasdas', '2018-04-26 22:02:11.513450', '2018-04-26 22:02:11.513450', 1),
(2, '0895332085649', 'Jawa Barat', '40512', 'Cimahi', 'Kp.Cisurupan no.146 Rt 03/07', '2018-04-27 11:47:38.887967', '2018-04-27 11:47:38.887967', 4),
(3, '089545488787', 'Jawa Barat', '40512', 'Cimahi', 'Unknown', '2018-04-28 20:56:51.496387', '2018-04-28 20:56:51.496387', 4);

-- --------------------------------------------------------

--
-- Table structure for table `music_userprofile`
--

CREATE TABLE `music_userprofile` (
  `id` int(11) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `music_userprofile`
--

INSERT INTO `music_userprofile` (`id`, `picture`, `user_id`) VALUES
(1, 'User_image/mataku_UswwEt5.jpg', 1),
(2, 'User_image/20170904_135132.jpg', 4);

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_accesstoken`
--

CREATE TABLE `oauth2_provider_accesstoken` (
  `id` bigint(20) NOT NULL,
  `token` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `source_refresh_token_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

INSERT INTO `oauth2_provider_accesstoken` (`id`, `token`, `expires`, `scope`, `application_id`, `user_id`, `created`, `updated`, `source_refresh_token_id`) VALUES
(15, 'Icxj2TdNhfbwW5t0aR1h6l0BUDob90', '2018-04-27 15:57:49.572123', 'read write', 1, 5, '2018-04-27 14:57:49.143099', '2018-04-27 14:57:49.143099', NULL),
(17, 'i7fQEIzg6M2HuY76Xv3vA6LDGtDuf9', '2018-04-27 16:06:28.424800', 'read write', 1, 6, '2018-04-27 15:05:28.987400', '2018-04-27 15:05:28.987400', NULL),
(29, 'qZSxqeQrbNe4GMv0buS5YH4OYkiS8A', '2018-04-27 21:53:25.209452', 'read write', 1, 6, '2018-04-27 20:53:25.209452', '2018-04-27 20:53:25.209452', NULL),
(56, 'tGHoUPidbA7M9PV6WHOTDle1V8zKBt', '2018-04-29 23:14:27.955656', 'read write', 1, 1, '2018-04-29 17:39:57.057584', '2018-04-29 17:39:57.057584', NULL),
(57, 'H2CP69Ue5Qc7gcJVHqPDXc2XuhBOzV', '2018-04-29 23:41:25.679184', 'read write', 1, 4, '2018-04-29 22:40:33.717212', '2018-04-29 22:40:33.717212', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_application`
--

CREATE TABLE `oauth2_provider_application` (
  `id` bigint(20) NOT NULL,
  `client_id` varchar(100) NOT NULL,
  `redirect_uris` longtext NOT NULL,
  `client_type` varchar(32) NOT NULL,
  `authorization_grant_type` varchar(32) NOT NULL,
  `client_secret` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `oauth2_provider_application`
--

INSERT INTO `oauth2_provider_application` (`id`, `client_id`, `redirect_uris`, `client_type`, `authorization_grant_type`, `client_secret`, `name`, `user_id`, `skip_authorization`, `created`, `updated`) VALUES
(1, 'tDDrJCTF6IKR05hlXkjISiSiuYgp6BJXTiehcoit', 'http://django-oauth-toolkit.herokuapp.com/consumer/exchange/', 'confidential', 'password', 'AcfRaSbii1VEhZl8uN7J0ArTVUPTnsVJA1VPJYMZfdop7QROO5mfNQAFy68Vc1d0ucJXDIrfgqXhxw7a3DAhbbmo4rhW9grRvkr8rbZekgNA5WlVdOUhUOrVEHxAsI9u', 'Ticket', 1, 0, '2018-04-26 21:36:29.566260', '2018-04-26 21:39:30.691620');

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_grant`
--

CREATE TABLE `oauth2_provider_grant` (
  `id` bigint(20) NOT NULL,
  `code` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` varchar(255) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` bigint(20) NOT NULL,
  `token` varchar(255) NOT NULL,
  `access_token_id` bigint(20) DEFAULT NULL,
  `application_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `revoked` datetime(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

INSERT INTO `oauth2_provider_refreshtoken` (`id`, `token`, `access_token_id`, `application_id`, `user_id`, `created`, `updated`, `revoked`) VALUES
(1, '1NxfH0rWN4dlH8JTEPg8D6ScdmOTPC', NULL, 1, 1, '2018-04-26 21:38:44.459975', '2018-04-26 21:38:44.459975', NULL);

--
-- Indexes for dumped tables
--

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
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

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
-- Indexes for table `music_album`
--
ALTER TABLE `music_album`
  ADD PRIMARY KEY (`idapp`);

--
-- Indexes for table `music_cart`
--
ALTER TABLE `music_cart`
  ADD PRIMARY KEY (`idapp`),
  ADD KEY `music_cart_ticket_id_3ec0b998_fk_music_event_idapp` (`ticket_id`),
  ADD KEY `music_cart_user_id_7a39cabf_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `music_event`
--
ALTER TABLE `music_event`
  ADD PRIMARY KEY (`idapp`);

--
-- Indexes for table `music_event_ticket_for`
--
ALTER TABLE `music_event_ticket_for`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `music_event_ticket_for_event_id_music_id_7818d06a_uniq` (`event_id`,`music_id`),
  ADD KEY `music_event_ticket_for_music_id_ea7ccbbe_fk_music_music_idapp` (`music_id`);

--
-- Indexes for table `music_music`
--
ALTER TABLE `music_music`
  ADD PRIMARY KEY (`idapp`),
  ADD KEY `music_music_album_id_8cc7f386_fk_music_album_idapp` (`album_id`);

--
-- Indexes for table `music_ticket_transaction`
--
ALTER TABLE `music_ticket_transaction`
  ADD PRIMARY KEY (`idapp`),
  ADD KEY `music_ticket_transac_info_id_6f0703f6_fk_music_tra` (`info_id`),
  ADD KEY `music_ticket_transaction_ticket_id_d4bd7e6d_fk_music_event_idapp` (`ticket_id`),
  ADD KEY `music_ticket_transaction_user_id_7e51e10d_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `music_transaction_info`
--
ALTER TABLE `music_transaction_info`
  ADD PRIMARY KEY (`idapp`),
  ADD KEY `music_transaction_info_user_id_18afe727_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `music_userprofile`
--
ALTER TABLE `music_userprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `oauth2_provider_accesstoken`
--
ALTER TABLE `oauth2_provider_accesstoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `oauth2_provider_accesstoken_token_8af090f8_uniq` (`token`),
  ADD UNIQUE KEY `source_refresh_token_id` (`source_refresh_token_id`),
  ADD KEY `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_auth_user_id` (`user_id`),
  ADD KEY `oauth2_provider_accesstoken_application_id_b22886e1_fk` (`application_id`);

--
-- Indexes for table `oauth2_provider_application`
--
ALTER TABLE `oauth2_provider_application`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `client_id` (`client_id`),
  ADD KEY `oauth2_provider_application_client_secret_53133678` (`client_secret`),
  ADD KEY `oauth2_provider_application_user_id_79829054_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `oauth2_provider_grant`
--
ALTER TABLE `oauth2_provider_grant`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `oauth2_provider_grant_code_49ab4ddf_uniq` (`code`),
  ADD KEY `oauth2_provider_grant_application_id_81923564_fk` (`application_id`),
  ADD KEY `oauth2_provider_grant_user_id_e8f62af8_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `oauth2_provider_refreshtoken`
--
ALTER TABLE `oauth2_provider_refreshtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `access_token_id` (`access_token_id`),
  ADD UNIQUE KEY `oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq` (`token`,`revoked`),
  ADD KEY `oauth2_provider_refreshtoken_application_id_2d1c311b_fk` (`application_id`),
  ADD KEY `oauth2_provider_refreshtoken_user_id_da837fce_fk_auth_user_id` (`user_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT for table `music_album`
--
ALTER TABLE `music_album`
  MODIFY `idapp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `music_cart`
--
ALTER TABLE `music_cart`
  MODIFY `idapp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT for table `music_event`
--
ALTER TABLE `music_event`
  MODIFY `idapp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `music_event_ticket_for`
--
ALTER TABLE `music_event_ticket_for`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT for table `music_music`
--
ALTER TABLE `music_music`
  MODIFY `idapp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `music_ticket_transaction`
--
ALTER TABLE `music_ticket_transaction`
  MODIFY `idapp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `music_transaction_info`
--
ALTER TABLE `music_transaction_info`
  MODIFY `idapp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `music_userprofile`
--
ALTER TABLE `music_userprofile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `oauth2_provider_accesstoken`
--
ALTER TABLE `oauth2_provider_accesstoken`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;
--
-- AUTO_INCREMENT for table `oauth2_provider_application`
--
ALTER TABLE `oauth2_provider_application`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `oauth2_provider_grant`
--
ALTER TABLE `oauth2_provider_grant`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `oauth2_provider_refreshtoken`
--
ALTER TABLE `oauth2_provider_refreshtoken`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
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
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `music_cart`
--
ALTER TABLE `music_cart`
  ADD CONSTRAINT `music_cart_ticket_id_3ec0b998_fk_music_event_idapp` FOREIGN KEY (`ticket_id`) REFERENCES `music_event` (`idapp`),
  ADD CONSTRAINT `music_cart_user_id_7a39cabf_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `music_event_ticket_for`
--
ALTER TABLE `music_event_ticket_for`
  ADD CONSTRAINT `music_event_ticket_for_event_id_b7a3668f_fk_music_event_idapp` FOREIGN KEY (`event_id`) REFERENCES `music_event` (`idapp`),
  ADD CONSTRAINT `music_event_ticket_for_music_id_ea7ccbbe_fk_music_music_idapp` FOREIGN KEY (`music_id`) REFERENCES `music_music` (`idapp`);

--
-- Constraints for table `music_music`
--
ALTER TABLE `music_music`
  ADD CONSTRAINT `music_music_album_id_8cc7f386_fk_music_album_idapp` FOREIGN KEY (`album_id`) REFERENCES `music_album` (`idapp`);

--
-- Constraints for table `music_ticket_transaction`
--
ALTER TABLE `music_ticket_transaction`
  ADD CONSTRAINT `music_ticket_transac_info_id_6f0703f6_fk_music_tra` FOREIGN KEY (`info_id`) REFERENCES `music_transaction_info` (`idapp`),
  ADD CONSTRAINT `music_ticket_transaction_ticket_id_d4bd7e6d_fk_music_event_idapp` FOREIGN KEY (`ticket_id`) REFERENCES `music_event` (`idapp`),
  ADD CONSTRAINT `music_ticket_transaction_user_id_7e51e10d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `music_transaction_info`
--
ALTER TABLE `music_transaction_info`
  ADD CONSTRAINT `music_transaction_info_user_id_18afe727_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `music_userprofile`
--
ALTER TABLE `music_userprofile`
  ADD CONSTRAINT `music_userprofile_user_id_5531150c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `oauth2_provider_accesstoken`
--
ALTER TABLE `oauth2_provider_accesstoken`
  ADD CONSTRAINT `oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr` FOREIGN KEY (`source_refresh_token_id`) REFERENCES `oauth2_provider_refreshtoken` (`id`),
  ADD CONSTRAINT `oauth2_provider_accesstoken_application_id_b22886e1_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  ADD CONSTRAINT `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `oauth2_provider_application`
--
ALTER TABLE `oauth2_provider_application`
  ADD CONSTRAINT `oauth2_provider_application_user_id_79829054_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `oauth2_provider_grant`
--
ALTER TABLE `oauth2_provider_grant`
  ADD CONSTRAINT `oauth2_provider_grant_application_id_81923564_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  ADD CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `oauth2_provider_refreshtoken`
--
ALTER TABLE `oauth2_provider_refreshtoken`
  ADD CONSTRAINT `oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`),
  ADD CONSTRAINT `oauth2_provider_refreshtoken_application_id_2d1c311b_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  ADD CONSTRAINT `oauth2_provider_refreshtoken_user_id_da837fce_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
