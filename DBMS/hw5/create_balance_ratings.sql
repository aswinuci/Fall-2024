use hw5;

--- Drop existing tables
DROP TABLE IF EXISTS Astar_Based_Rating;
DROP TABLE IF EXISTS Balanced_Rating;
DROP TABLE IF EXISTS General_Rating;

-- Create Astar_Based_Rating table
CREATE TABLE IF NOT EXISTS Astar_Based_Rating (
    university_name VARCHAR(255),
    weighted_score REAL,
    PRIMARY KEY (university_name)
);

-- Create Balanced_Rating table
CREATE TABLE IF NOT EXISTS Balanced_Rating (
    university_name VARCHAR(255),
    weighted_score REAL,
    PRIMARY KEY (university_name)
);

-- Create General_Rating table
CREATE TABLE IF NOT EXISTS General_Rating (
    university_name VARCHAR(255),
    weighted_score REAL,
    PRIMARY KEY (university_name)
);



-- Insert data into Astar_Based_Rating with weights (0.4, 0.4, 0.1, 0.1)
INSERT INTO Astar_Based_Rating (university_name, weighted_score)
SELECT 
a.affiliation AS university_name,
(0.4 * SUM(CASE WHEN cr.rank = 'A*' THEN p.count ELSE 0 END) + 
0.4 * COUNT(DISTINCT CASE WHEN cr.rank = 'A*' THEN a.name END) + 
0.1 * SUM(p.count) + 
0.1 * COUNT(DISTINCT a.name)) AS score
FROM 
    author a
JOIN 
    pub_info p ON a.name = p.name
JOIN 
    field_conference fc ON p.conference = fc.conference
JOIN 
    conference_ranking cr ON p.conference = cr.conf_abbr
WHERE 
    p.year BETWEEN 2014 AND 2024
    AND ('ALL' = 'ALL' OR fc.field = 'ALL')
GROUP BY 
    a.affiliation
ORDER BY 
    score DESC
LIMIT 50;

-- Insert data into Balanced_Rating with weights (0.25, 0.25, 0.25, 0.25)
INSERT INTO Balanced_Rating (university_name, weighted_score)
SELECT 
a.affiliation AS university_name,
(0.25 * SUM(CASE WHEN cr.rank = 'A*' THEN p.count ELSE 0 END) + 
0.25 * COUNT(DISTINCT CASE WHEN cr.rank = 'A*' THEN a.name END) + 
0.25 * SUM(p.count) + 
0.25 * COUNT(DISTINCT a.name)) AS score
FROM 
    author a
JOIN 
    pub_info p ON a.name = p.name
JOIN 
    field_conference fc ON p.conference = fc.conference
JOIN 
    conference_ranking cr ON p.conference = cr.conf_abbr
WHERE 
    p.year BETWEEN 2014 AND 2024
    AND ('ALL' = 'ALL' OR fc.field = 'ALL')
GROUP BY 
    a.affiliation
ORDER BY 
    score DESC
LIMIT 50;


-- Insert data into General_Rating with weights (0.1, 0.1, 0.4, 0.4)
INSERT INTO General_Rating (university_name, weighted_score)
SELECT 
a.affiliation AS university_name,
(0.1 * SUM(CASE WHEN cr.rank = 'A*' THEN p.count ELSE 0 END) + 
0.1 * COUNT(DISTINCT CASE WHEN cr.rank = 'A*' THEN a.name END) + 
0.4 * SUM(p.count) + 
0.4 * COUNT(DISTINCT a.name)) AS score
FROM 
    author a
JOIN 
    pub_info p ON a.name = p.name
JOIN 
    field_conference fc ON p.conference = fc.conference
JOIN 
    conference_ranking cr ON p.conference = cr.conf_abbr
WHERE 
    p.year BETWEEN 2014 AND 2024
    AND ('ALL' = 'ALL' OR fc.field = 'ALL')
GROUP BY 
    a.affiliation
ORDER BY 
    score DESC
LIMIT 50;