-- Question 1
SELECT 
    a.name,
    p.conference,
    p.year,
    p.count
FROM 
    author AS a
JOIN 
    pub_info AS p ON a.name = p.name
JOIN 
    field_conference AS f ON p.conference = f.conference
WHERE 
    a.affiliation = 'University of California, Berkeley'
    AND f.field = 'Databases'
    AND p.year BETWEEN 2010 AND 2024;

-- Question 2
SELECT 
    DISTINCT f.conference
FROM 
    field_conference AS f
LEFT JOIN 
    pub_info AS p ON f.conference = p.conference
LEFT JOIN 
    author AS a ON p.name = a.name
WHERE 
    f.major = 'Computer Science'
    AND (a.affiliation IS NULL OR a.affiliation != 'University of California, Irvine');

-- Question 3
SELECT 
    p.conference,
    p.year,
    a.name,
    a.affiliation
FROM 
    pub_info AS p
JOIN 
    author AS a ON p.name = a.name
JOIN 
    field_conference AS f ON p.conference = f.conference
JOIN (
    SELECT 
        conference, 
        year, 
        MAX(count) AS max_count
    FROM 
        pub_info
    GROUP BY 
        conference, year
) AS max_pub ON p.conference = max_pub.conference 
               AND p.year = max_pub.year 
               AND p.count = max_pub.max_count
WHERE 
    f.field = 'Databases';

-- Question 4
SELECT 
    DISTINCT a.affiliation AS university_name
FROM 
    author AS a
JOIN 
    pub_info AS p ON a.name = p.name
JOIN 
    field_conference AS f ON p.conference = f.conference
WHERE 
    f.field = 'Databases'
    AND p.year BETWEEN 2020 AND 2024
GROUP BY 
    a.affiliation
HAVING 
    COUNT(DISTINCT f.conference) = (SELECT COUNT(DISTINCT conference) 
                                    FROM field_conference 
                                    WHERE field = 'Databases');

-- Question 5
SELECT 
    u.university_name
FROM 
    usnews_university_rankings AS u
JOIN 
    usnews_university_rankings AS uci ON uci.university_name = 'University of California, Irvine'
LEFT JOIN 
    author AS a ON u.university_name = a.affiliation
LEFT JOIN 
    pub_info AS p ON a.name = p.name
LEFT JOIN 
    field_conference AS f ON p.conference = f.conference
LEFT JOIN 
    conference_ranking AS c ON p.conference = c.conf_abbr
WHERE 
    u.rank < uci.rank
    AND (c.rank != 'A*' OR c.rank IS NULL OR f.field != 'Databases' OR p.conference IS NULL);
