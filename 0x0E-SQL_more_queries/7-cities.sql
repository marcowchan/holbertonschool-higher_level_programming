-- Creates a hbtn_0d_usa database with a the states table.
-- Creates a hbtn_0d_usa database.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use the hbtn_0d_usa database.
USE `hbtn_0d_usa`;
-- Creates a cities table.
CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT AUTO_INCREMENT NOT NULL,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
);
