import mysql.connector
from constants import Constants

class Queries(object):
    """Database queries"""
    connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD, database=Constants.DATABASE)
    cursor = connection.cursor()
    
    """Retrieve the names and genders of all people associated with ARC (i.e., members, employees, etc.)"""
    
    query1 = '''
        CREATE VIEW Top_Machines_Used AS
        SELECT
            e.equipment_type AS `Equipment Name`,
            COUNT(DISTINCT u.timestamp) AS `Total Number Of Days Used`,
            COUNT(DISTINCT u.card_id) AS `Number Of Unique Users Using Equipment`,
            RANK() OVER (ORDER BY COUNT(DISTINCT u.card_id) DESC) AS `Rank` 
        FROM
            usage_reading u
        JOIN
            equipment e ON u.equipment_id = e.equipment_id
        WHERE
            u.timestamp >= '2023-01-01 00:00:00' AND u.timestamp <= '2023-06-30 00:00:00'
        GROUP BY
            e.equipment_type
		ORDER BY
			COUNT(DISTINCT u.card_id) DESC
		LIMIT 15;
    '''
    
    query2 = '''
        CREATE VIEW Machines_Used_By_Day_Of_Week AS
        SELECT
			e.equipment_type AS `Equipment Name`,
            DAYNAME(u.timestamp) AS `Day of Week`,
            COALESCE(s.student_type, ns.member_type, 'Family') AS `Type of Member`,count(*) AS `Count`
        FROM
            usage_reading u
        JOIN
            equipment e ON u.equipment_id = e.equipment_id
        LEFT JOIN
            student s ON u.card_id = s.card_id
        LEFT JOIN
            non_student ns ON u.card_id = ns.card_id
        LEFT JOIN
            family f ON u.card_id = f.card_id
        GROUP BY e.equipment_type ,`Type of Member`, `Day of Week` with rollup;
    '''
    
    query3 = '''
        CREATE TRIGGER noupdate 
        BEFORE UPDATE ON employee
        FOR EACH ROW
        BEGIN 
            IF NEW.salary_hour < OLD.salary_hour THEN
                SET NEW.salary_hour = OLD.salary_hour;
            END IF;
        END;
    '''
    
    query4 = '''
        ALTER TABLE employee
        ADD CONSTRAINT check_min_salary
        CHECK (salary_hour >= 12);
    '''

    query5 = '''
        WITH RECURSIVE SupervisorHierarchy AS (
            SELECT
                card_id,
                supervisor_card_id,
                1 AS SupervisorLength
            FROM
                employee
            WHERE
                supervisor_card_id IS NOT NULL
            
            UNION ALL
            
            SELECT
                e.card_id,
                e.supervisor_card_id,
                sh.SupervisorLength + 1
            FROM
                employee e
            JOIN
                SupervisorHierarchy sh ON e.card_id = sh.supervisor_card_id
        )
        SELECT
            MAX(SupervisorLength) AS MaxSupervisorLength
        FROM
            SupervisorHierarchy;
    '''

    query6 = '''
        WITH RankedEmployees AS (
            SELECT
                e.card_id,
                p.name,
                p.dob,
                e.schedule,
                e.employee_type,
                e.salary_hour,
                RANK() OVER (ORDER BY e.salary_hour DESC, p.dob DESC) as Ranking
            FROM
                employee e
            JOIN
                person p ON e.card_id = p.card_id
        )
        SELECT
            name
        FROM
            RankedEmployees
        WHERE
            Ranking = 2
    '''

    cursor.execute(query1)
    
    print(cursor.fetchall())