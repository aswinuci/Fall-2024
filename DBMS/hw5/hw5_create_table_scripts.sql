drop database hw5;

create database hw5;
use hw5;

create table if not exists conference_ranking (
conf_abbr varchar(100) NOT NULL,
`name` varchar(300) NOT NULL,
`rank` varchar(10) NOT NULL,
primary key (conf_abbr)
);

create table if not exists field_conference (
major varchar(200),
`field` varchar(200),
conference varchar(100),
foreign key (conference) references conference_ranking(conf_abbr)
);

create table if not exists usnews_university_rankings (
university_name varchar(200),
alias_names varchar(200),
state varchar(3),
city varchar(100),
zip integer,
institution_control varchar(100),
`rank` int,
tied varchar(10),
acceptance_rate integer,
tution integer,
enrollment integer,
primary key (university_name)
);

create table if not exists author (
`name` varchar(300) not null,
affiliation varchar(200),
homepage varchar(300),
scholarid varchar(100),
turing_award boolean,
acm_fellow boolean,
region varchar(100),
country varchar(100),
begin_time integer,
end_time integer null,
primary key (`name`),
foreign key (affiliation) references usnews_university_rankings(university_name)
);

create table if not exists pub_info (
`name` varchar(300),
conference varchar(100),
`count` integer,
`year` integer,
foreign key (conference) references conference_ranking(conf_abbr)
);



