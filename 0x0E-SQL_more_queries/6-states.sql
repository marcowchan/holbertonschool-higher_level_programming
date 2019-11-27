-- Creates a hbtn_0d_usa database with a the states table.
-- Creates a hbtn_0d_usa database.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use the hbtn_0d_usa database.
USE `hbtn_0d_usa`;
-- Creates a states table.
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT AUTO_INCREMENT UNIQUE NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`)
);
