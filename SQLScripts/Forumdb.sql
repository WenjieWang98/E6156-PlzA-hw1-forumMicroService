create database searchbase;
use searchbase;

Drop table if exists catInfo;
Drop table if exists breeder;

CREATE TABLE `breeder` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `organization` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `website` varchar(100) NOT NULL,
  `rating` decimal(2,1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);


CREATE TABLE `catInfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `race` varchar(100) NOT NULL,
  `color` varchar(45) NOT NULL,
  `dob` datetime NOT NULL,
  `father` int NOT NULL,
  `mother` int NOT NULL,
  `breeder` int NOT NULL,
  `listing price` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idCat_UNIQUE` (`id`),
  FOREIGN KEY (id) REFERENCES breeder(id)
);

INSERT INTO breeder ( id, name, organization, phone, email, address, website, rating) VALUES ( '000001','Tom Hanks','TICA','+19176211078','sw@gmail.com','33 brooklyn steet, New York City','www.tomcat.com', 5 );