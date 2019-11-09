-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 09, 2019 at 02:46 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.2.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `usertypes`
--

CREATE TABLE `usertypes` (
  `id` int(11) NOT NULL,
  `code` varchar(80) NOT NULL,
  `user_type` varchar(80) NOT NULL,
  `value` smallint(5) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertypes`
--

INSERT INTO `usertypes` (`id`, `code`, `user_type`, `value`) VALUES
(1, 'CUSTOMER_01', 'CUSTOMER', 1),
(2, 'TAILOR_02', 'TAILOR', 2),
(3, 'BOUTIQUE_03', 'BOUTIQUE', 3),
(4, 'MASTER_04', 'MASTER', 4),
(5, 'MAGGAM_DESIGNER_05', 'MAGGAM_DESIGNER', 5),
(6, 'FASHION_DESIGNER_05', 'FASHION_DESIGNER', 6),
(7, 'MASTER_04', 'MASTER', 4),
(8, 'MAGGAM_DESIGNER_05', 'MAGGAM_DESIGNER', 5),
(9, 'FASHION_DESIGNER_05', 'FASHION_DESIGNER', 6);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `usertypes`
--
ALTER TABLE `usertypes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `usertypes`
--
ALTER TABLE `usertypes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
