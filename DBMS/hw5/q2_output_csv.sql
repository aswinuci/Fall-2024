use hw5;

SELECT 
    'university_name',
    'score',
    'Ranking'
UNION ALL
-- Append the actual data
SELECT 
    university_name,
    weighted_score AS score,
    RANK() OVER (ORDER BY weighted_score DESC) AS Ranking
FROM 
    Astar_Based_Rating
ORDER BY 
    Ranking
LIMIT 50
INTO OUTFILE '/var/lib/mysql-files/star.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';


-- Write the headers manually
SELECT 
    'university_name',
    'score',
    'Ranking'
UNION ALL
-- Append the actual data
SELECT 
    university_name,
    weighted_score AS score,
    RANK() OVER (ORDER BY weighted_score DESC) AS Ranking
FROM 
    Balanced_Rating
ORDER BY 
    Ranking
LIMIT 50
INTO OUTFILE '/var/lib/mysql-files/balanced.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';


-- Write the headers manually
SELECT 
    'university_name',
    'score',
    'Ranking'
UNION ALL
-- Append the actual data
SELECT 
    university_name,
    weighted_score AS score,
    RANK() OVER (ORDER BY weighted_score DESC) AS Ranking
FROM 
    General_Rating
ORDER BY 
    Ranking
LIMIT 50
INTO OUTFILE '/var/lib/mysql-files/general.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';
