use hw5;

LOAD DATA INFILE '/var/lib/mysql-files/conference_ranking.csv'
INTO TABLE conference_ranking
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/field_conference.csv'
INTO TABLE field_conference
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/usnews_university_rankings.csv'
INTO TABLE usnews_university_rankings
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/author.csv'
INTO TABLE author
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(`name`, affiliation, homepage, scholarid, turing_award, acm_fellow, region, country, begin_time, @end_time)
SET end_time = NULLIF(@end_time, '');


LOAD DATA INFILE '/var/lib/mysql-files/pub_info.csv'
INTO TABLE pub_info
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
