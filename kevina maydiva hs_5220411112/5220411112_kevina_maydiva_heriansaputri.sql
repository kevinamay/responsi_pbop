-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2024 at 07:36 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411112_kevina_maydiva_heriansaputri`
--

-- --------------------------------------------------------

--
-- Table structure for table `film_kevina`
--

CREATE TABLE `film_kevina` (
  `Id` int(222) NOT NULL,
  `judul` varchar(222) NOT NULL,
  `tahun` varchar(222) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `studio_kevina`
--

CREATE TABLE `studio_kevina` (
  `Id` int(22) NOT NULL,
  `nama` varchar(222) NOT NULL,
  `kapasitas` varchar(222) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tiket_kevina`
--

CREATE TABLE `tiket_kevina` (
  `Id` int(222) NOT NULL,
  `studio_id` int(222) NOT NULL,
  `film_id` int(222) NOT NULL,
  `tanggal` date NOT NULL,
  `jam_tayang` varchar(222) NOT NULL,
  `jam_selesai` varchar(222) NOT NULL,
  `harga` varchar(222) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tr_penjualan_kevina`
--

CREATE TABLE `tr_penjualan_kevina` (
  `Id` int(222) NOT NULL,
  `tiket_id` int(222) NOT NULL,
  `jumlah` varchar(222) NOT NULL,
  `bayar` varchar(222) NOT NULL,
  `kembalian` varchar(222) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `film_kevina`
--
ALTER TABLE `film_kevina`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `studio_kevina`
--
ALTER TABLE `studio_kevina`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `tiket_kevina`
--
ALTER TABLE `tiket_kevina`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `studio_id` (`studio_id`),
  ADD KEY `film_id` (`film_id`);

--
-- Indexes for table `tr_penjualan_kevina`
--
ALTER TABLE `tr_penjualan_kevina`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `tiket_id` (`tiket_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `film_kevina`
--
ALTER TABLE `film_kevina`
  MODIFY `Id` int(222) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `studio_kevina`
--
ALTER TABLE `studio_kevina`
  MODIFY `Id` int(22) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tiket_kevina`
--
ALTER TABLE `tiket_kevina`
  MODIFY `Id` int(222) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tr_penjualan_kevina`
--
ALTER TABLE `tr_penjualan_kevina`
  MODIFY `Id` int(222) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tiket_kevina`
--
ALTER TABLE `tiket_kevina`
  ADD CONSTRAINT `tiket_kevina_ibfk_1` FOREIGN KEY (`studio_id`) REFERENCES `studio_kevina` (`Id`),
  ADD CONSTRAINT `tiket_kevina_ibfk_2` FOREIGN KEY (`film_id`) REFERENCES `film_kevina` (`Id`);

--
-- Constraints for table `tr_penjualan_kevina`
--
ALTER TABLE `tr_penjualan_kevina`
  ADD CONSTRAINT `tr_penjualan_kevina_ibfk_1` FOREIGN KEY (`tiket_id`) REFERENCES `tiket_kevina` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
