-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1
-- Tid vid skapande: 31 okt 2016 kl 14:53
-- Serverversion: 5.7.14
-- PHP-version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `pingishack`
--
CREATE DATABASE IF NOT EXISTS `pingishack` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `pingishack`;

-- --------------------------------------------------------

--
-- Tabellstruktur `gamematch`
--

CREATE TABLE IF NOT EXISTS `gamematch` (
  `matchID` int(11) NOT NULL AUTO_INCREMENT,
  `player1ID` int(11) NOT NULL,
  `player2ID` int(11) NOT NULL,
  `player1Set` int(11) NOT NULL,
  `player2Set` int(11) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`matchID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellstruktur `gameset`
--

CREATE TABLE IF NOT EXISTS `gameset` (
  `setID` int(11) NOT NULL AUTO_INCREMENT,
  `player1Points` int(11) NOT NULL,
  `player2Points` int(11) NOT NULL,
  `winnerID` int(11) NOT NULL,
  `loserID` int(11) NOT NULL,
  `matchID` int(11) NOT NULL,
  PRIMARY KEY (`setID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellstruktur `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'playerID',
  `name` varchar(64) NOT NULL COMMENT 'playerName',
  `cardID` varchar(16) NOT NULL COMMENT 'playerCardInfo',
  `wins` int(11) NOT NULL COMMENT 'noWins',
  `losses` int(11) NOT NULL COMMENT 'noLosses',
  `totalGames` int(11) NOT NULL COMMENT 'noGamesPlayed',
  PRIMARY KEY (`id`),
  UNIQUE KEY `cardID` (`cardID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
