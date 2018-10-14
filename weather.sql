-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Oct 14, 2018 at 07:09 AM
-- Server version: 5.6.28
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `weather`
--
CREATE DATABASE IF NOT EXISTS `weather` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `weather`;

-- --------------------------------------------------------

--
-- Table structure for table `observations`
--

DROP TABLE IF EXISTS `observations`;
CREATE TABLE `observations` (
  `id` int(11) NOT NULL,
  `temperature` float DEFAULT NULL,
  `dewpoint` float DEFAULT NULL,
  `humidity` int(11) DEFAULT NULL,
  `wind_direction` int(11) DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `wind_gust` float DEFAULT NULL,
  `rain` float DEFAULT NULL,
  `pressure` float DEFAULT NULL,
  `dt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `raw_air_pressure`
--

DROP TABLE IF EXISTS `raw_air_pressure`;
CREATE TABLE `raw_air_pressure` (
  `id` int(11) NOT NULL,
  `dt` datetime NOT NULL,
  `pressure` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `raw_rain`
--

DROP TABLE IF EXISTS `raw_rain`;
CREATE TABLE `raw_rain` (
  `id` int(11) NOT NULL,
  `dt` datetime NOT NULL,
  `rain` float NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `raw_temp_rh`
--

DROP TABLE IF EXISTS `raw_temp_rh`;
CREATE TABLE `raw_temp_rh` (
  `id` int(11) NOT NULL,
  `dt` datetime NOT NULL,
  `temperature` float NOT NULL,
  `humidity` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `raw_wind`
--

DROP TABLE IF EXISTS `raw_wind`;
CREATE TABLE `raw_wind` (
  `id` int(10) UNSIGNED NOT NULL,
  `dt` datetime NOT NULL,
  `wind_speed` float DEFAULT NULL,
  `wind_direction` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `observations`
--
ALTER TABLE `observations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `raw_air_pressure`
--
ALTER TABLE `raw_air_pressure`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `raw_rain`
--
ALTER TABLE `raw_rain`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `raw_temp_rh`
--
ALTER TABLE `raw_temp_rh`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `raw_wind`
--
ALTER TABLE `raw_wind`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `observations`
--
ALTER TABLE `observations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
--
-- AUTO_INCREMENT for table `raw_air_pressure`
--
ALTER TABLE `raw_air_pressure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `raw_rain`
--
ALTER TABLE `raw_rain`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=213;
--
-- AUTO_INCREMENT for table `raw_temp_rh`
--
ALTER TABLE `raw_temp_rh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `raw_wind`
--
ALTER TABLE `raw_wind`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128797;