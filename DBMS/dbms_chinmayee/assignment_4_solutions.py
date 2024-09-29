import mysql.connector
from constants import Constants

class Queries(object):
    """Database queries"""
    connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD, database=Constants.DATABASE)
    cursor = connection.cursor()
    
    """Retrieve the names and genders of all people associated with ARC (i.e., members, employees, etc.)"""
    
    query1 = "select name, gender from person;"
    
    query2 = "select name, department from person natural join non_student natural join university_affiliate where member_type = 'faculty'";
    
    query3 = "SELECT DISTINCT p.name \
FROM person p \
JOIN location_reading lr ON p.card_id = lr.person_id \
JOIN space s ON lr.space_id = s.space_id \
WHERE (s.description = 'weight room' OR s.description = 'cardio room') \
  AND DATE(lr.timestamp) = '2023-04-01';"
    

    query4 = "with attends1 as (select card_id, count(event_id) as count from person natural join attends natural join events group by card_id \
              having count = (select count(*) from events)) \
              select name from person natural join attends1;"
    
    query5 = "SELECT e.event_id FROM events e JOIN space s ON e.space_id = s.space_id WHERE e.capacity >= s.max_capacity;"

    query6 = "SELECT DISTINCT p.name FROM person p JOIN student s ON p.card_id = s.card_id WHERE NOT EXISTS (SELECT e.equipment_id FROM equipment e WHERE e.space_id = (SELECT space_id FROM space sp WHERE sp.description = 'cardio room') AND NOT EXISTS ( SELECT u.sensor_id FROM usage_reading u WHERE u.card_id = p.card_id AND u.equipment_id = e.equipment_id));"

    query7 = "select equipment_id, equipment_type from equipment where is_available = 1";
    
    query8 = "select name from person natural join employee";
    
    query9 = "SELECT DISTINCT p.name FROM person p JOIN attends a ON p.card_id = a.card_id JOIN events e ON a.event_id = e.event_id JOIN space s ON e.space_id = s.space_id WHERE s.description = 'yoga studio';"

    query10 = "select name from \
     person natural join family natural join attends natural join events e \
     where e.description = 'Summer Splash Fest';"

    query11 = "select avg(salary_hour) as average_hourly_rate from employee where employee_type= 'student';"

    query12 = "with avg_salary_table as ( \
               select name, avg(salary_hour) as avg_sal from \
               person p natural join employee e inner join Trainer t on \
               e.card_id = t.person_id group by name) \
               select name from avg_salary_table \
               where avg_sal = (select max(avg_sal) from avg_salary_table where \
                                avg_sal < (select max(avg_sal) from avg_salary_table))"
    query13 = "SELECT COUNT(DISTINCT DATE(lr.timestamp)) AS total_days FROM location_reading lr JOIN space s ON lr.space_id = s.space_id JOIN person p ON lr.person_id = p.card_id WHERE p.name = 'Mekhi Sporer' AND s.description = 'weight room';"
   
    query14 = "SELECT p.name FROM person p JOIN member m ON p.card_id = m.card_id JOIN location_reading lr ON p.card_id = lr.person_id JOIN space s ON lr.space_id = s.space_id WHERE s.description = 'cardio room'  AND EXTRACT(MONTH FROM lr.timestamp) = 5 GROUP BY p.card_id ORDER BY COUNT(DISTINCT DATE(lr.timestamp)) DESC ;"
    
    query15 = "SELECT s.description, SUM(a.occupancy)/COUNT(DISTINCT e.event_id) AS avg_occupancy FROM space s JOIN events e ON s.space_id = e.space_id LEFT JOIN (SELECT a.event_id, COUNT(a.card_id) AS occupancy FROM attends a  GROUP BY a.event_id ) a ON e.event_id = a.event_id GROUP BY s.description ORDER BY avg_occupancy LIMIT 1;"
   

    
    #cursor.execute(query12)
    #
    #print(cursor.fetchall())