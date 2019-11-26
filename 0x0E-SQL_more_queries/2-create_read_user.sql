-- Creates a hbtn_0d_2 database and a user_0d_2 user.
-- Creates a hbtn_0d_2 database.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- Creates a user_0d_2 user.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT privileges to user_0d_2.
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
