-- Separator for readability
SELECT '===== Question 1 =====' '';

-- Question 1
SELECT 
    author.name,
    pub_info.conference,
    pub_info.year,
    pub_info.count
FROM 
    author
JOIN 
    pub_info ON author.name = pub_info.name
JOIN 
    field_conference ON pub_info.conference = field_conference.conference
WHERE 
    author.affiliation = 'University of California, Berkeley'
    AND field_conference.field = 'Databases'
    AND pub_info.year BETWEEN 2010 AND 2024;

-- Line gap for readability
SELECT '' '';

-- Separator for readability
SELECT '===== Question 2 =====' '';

-- Question 2
SELECT 
    DISTINCT field_conference.conference
FROM 
    field_conference
LEFT JOIN 
    pub_info ON field_conference.conference = pub_info.conference
LEFT JOIN 
    author ON pub_info.name = author.name
WHERE 
    field_conference.major = 'Computer Science'
    AND (author.affiliation IS NULL OR author.affiliation != 'University of California, Irvine');

-- Line gap for readability
SELECT '' '';

-- Separator for readability
SELECT '===== Question 3 =====' '';

-- Question 3
SELECT 
    pub_info.conference,
    pub_info.year,
    author.name,
    author.affiliation
FROM 
    pub_info
JOIN 
    author ON pub_info.name = author.name
JOIN 
    field_conference ON pub_info.conference = field_conference.conference
JOIN (
    SELECT 
        conference, 
        year, 
        MAX(count) max_count
    FROM 
        pub_info
    GROUP BY 
        conference, year
) max_pub ON pub_info.conference = max_pub.conference 
           AND pub_info.year = max_pub.year 
           AND pub_info.count = max_pub.max_count
WHERE 
    field_conference.field = 'Databases';

-- Line gap for readability
SELECT '' '';

-- Separator for readability
SELECT '===== Question 4 =====' '';

-- Question 4
SELECT 
    DISTINCT author.affiliation university_name
FROM 
    author
JOIN 
    pub_info ON author.name = pub_info.name
JOIN 
    field_conference ON pub_info.conference = field_conference.conference
WHERE 
    field_conference.field = 'Databases'
    AND pub_info.year BETWEEN 2020 AND 2024
GROUP BY 
    author.affiliation
HAVING 
    COUNT(DISTINCT field_conference.conference) = (SELECT COUNT(DISTINCT conference) 
                                                   FROM field_conference 
                                                   WHERE field = 'Databases');

-- Line gap for readability
SELECT '' '';

-- Separator for readability
SELECT '===== Question 5 =====' '';

-- Question 5
SELECT 
    usnews_university_rankings.university_name
FROM 
    usnews_university_rankings
JOIN 
    usnews_university_rankings uci ON uci.university_name = 'University of California, Irvine'
LEFT JOIN 
    author ON usnews_university_rankings.university_name = author.affiliation
LEFT JOIN 
    pub_info ON author.name = pub_info.name
LEFT JOIN 
    field_conference ON pub_info.conference = field_conference.conference
LEFT JOIN 
    conference_ranking ON pub_info.conference = conference_ranking.conf_abbr
WHERE 
    usnews_university_rankings.rank < uci.rank
    AND (conference_ranking.rank != 'A*' OR conference_ranking.rank IS NULL OR field_conference.field != 'Databases' OR pub_info.conference IS NULL);

-- Final line gap for readability
SELECT '' '';
