DROP DATABASE IF EXISTS info_sec;
DROP DATABASE IF EXISTS info_sec1;
DROP DATABASE IF EXISTS info_sec2;


CREATE DATABASE  IF NOT EXISTS info_sec;
USE info_sec;      
CREATE TABLE IF NOT EXISTS info_sec.names(first_name varchar(255),last_name char(255));
CREATE TABLE IF NOT EXISTS info_sec.security_table(username varchar(255),pass char(255));
INSERT INTO info_sec.security_table VALUES ('root','info_pass_ctf_cool');
INSERT INTO info_sec.names VALUES ('Lance','Hayden');
INSERT INTO info_sec.names VALUES ('Peter','Park');
INSERT INTO info_sec.names VALUES ('Batman','Spiderman');



CREATE DATABASE  IF NOT EXISTS info_sec1;
USE info_sec1;      
CREATE TABLE IF NOT EXISTS info_sec1.security_table(username varchar(255),pass char(255));
CREATE TABLE IF NOT EXISTS info_sec1.names(first_name varchar(255),last_name char(255));
INSERT INTO info_sec1.security_table VALUES ('root','oops');


CREATE DATABASE  IF NOT EXISTS info_sec2;
USE info_sec2;      
CREATE TABLE IF NOT EXISTS info_sec2.security_table(username varchar(255),pass char(255));
CREATE TABLE IF NOT EXISTS info_sec2.names(first_name varchar(255),last_name char(255));

INSERT INTO info_sec2.security_table VALUES ('root','oops');

