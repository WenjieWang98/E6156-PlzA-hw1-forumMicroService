create database ccforum;
use ccforum;

Drop table if exists UserInformation;
create table UserInformation
(
    id int(11) NOT NULL AUTO_INCREMENT,
	nickname nvarchar(100) not null,
	email varchar(128) not null,
	password varchar(128) not null,
	phone varchar(128) null,
	constraint UserInformation_pk
		primary key (id)
);

create table Issue
(
	Ino varchar(128) not null,
	id int(11) not null,
	title text default null,
	issue_time datetime null,
	constraint Issue_pk
		primary key (Ino)
);

create unique index Issue_Ino_uindex
	on Issue (Ino);

create table Comment
(
	Cno varchar(128) not null,
	Ino varchar(128) not null,
	comment text null,
	comment_time datetime default '1999-9-9 9:9:9' not null,
	id int(11) not null,
	constraint Comment_pk
		primary key (Cno, Ino),
	constraint Comment_Issue_Ino_fk
		foreign key (Ino) references Issue (Ino)
);

INSERT INTO UserInformation ( nickname, email, password, phone) VALUES ( 'Sixuan', 'sw@gmail.com','123', '+19176211078');