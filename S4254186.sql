-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 11, 2018 alle 20:04
-- Versione del server: 5.5.55-0+deb8u1
-- PHP Version: 7.0.19-1~dotdeb+8.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `S4254186`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `raspberry`
--

CREATE TABLE IF NOT EXISTS `raspberry` (
  `id_rasp` varchar(40) NOT NULL,
  `url` varchar(255) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `raspberry`
--

INSERT INTO `raspberry` (`id_rasp`, `url`, `date`) VALUES
('00000000be1effcd', 'https://078bd8ad.ngrok.io', '2018-11-07 15:20:13');

-- --------------------------------------------------------

--
-- Struttura della tabella `token`
--

CREATE TABLE IF NOT EXISTS `token` (
  `username` varchar(32) NOT NULL,
  `token` varchar(42) NOT NULL,
  `expireDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `token`
--

INSERT INTO `token` (`username`, `token`, `expireDate`) VALUES
('pime', '111aaa', '2018-11-11 23:00:00'),
('pime', '19d175cf6f11be3b28ea3e61f65516967f228717', '0000-00-00 00:00:00'),
('pime', '5d0b8d9698e49e3db8c70a8a6239a9a1cbfb60ed', '2018-11-10 00:54:13');

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

CREATE TABLE IF NOT EXISTS `utenti` (
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `id_rasp` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`username`, `password`, `id_rasp`) VALUES
('pime', 'ciaociao', '00000000be1effcd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `raspberry`
--
ALTER TABLE `raspberry`
 ADD PRIMARY KEY (`id_rasp`);

--
-- Indexes for table `token`
--
ALTER TABLE `token`
 ADD PRIMARY KEY (`username`,`token`);

--
-- Indexes for table `utenti`
--
ALTER TABLE `utenti`
 ADD PRIMARY KEY (`username`), ADD UNIQUE KEY `username` (`username`,`id_rasp`);

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `token`
--
ALTER TABLE `token`
ADD CONSTRAINT `token_dell_utente` FOREIGN KEY (`username`) REFERENCES `utenti` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
