import mysql.connector
from constants import Constants

class Queries(object):
    """Database queries"""
    connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD, database=Constants.DATABASE)
    cursor = connection.cursor()
    
    """Retrieve the names and genders of all people associated with ARC (i.e., members, employees, etc.)"""
    
    query1 = "select name, gender from person;"
    
    query2 = "select name,department from non_student ns join university_affiliate ua on ns.card_id = ua.card_id join person on ns.card_id = person.card_id  where member_type = 'Faculty'"
    
    query3 = "select distinct name FROM location_reading lr JOIN space sp ON lr.space_id = sp.space_id JOIN person p ON p.card_id = lr.person_id WHERE timestamp = '2023-04-01 00:00:00' AND description IN ('weight room', 'cardio room');"
    
    query4 = "select name from person p where not exists (select * from events e where not exists (select * from attends a where a.card_id = p.card_id and e.event_id = a.event_id))"

    query5 = "select event_id from events e join space s on e.space_id = s.space_id  where e.capacity >= s.max_capacity;"

    query6 = "select name from student st join person p  on st.card_id = p.card_id where not exists (select * from equipment eq where not exists (select * from usage_reading ur where st.card_id = ur.card_id and eq.equipment_id = ur.equipment_id ) and equipment_id in  ( select eq1.equipment_id from equipment eq1 join space sp on eq1.space_id = sp.space_id and sp.description = 'cardio room'))"

    query7 = "SELECT equipment_id, equipment_type FROM equipment where is_available = 1;"
    
    query8 = "Select name from person join employee on employee.card_id = person.card_id;"
    
    query9 = "select distinct(name) from person where card_id in ( select card_id from attends a join events e on a.event_id = e.event_id where e.space_id in ( SELECT space_id from space where description = 'yoga studio'));" 
    
    query10 = "select name from events e join attends a on e.event_id = a.event_id join family f on f.card_id = a.card_id join person p on p.card_id = f.card_id where e.description = 'Summer Splash Fest';"

    query11 = "SELECT avg(salary_hour) FROM employee e where employee_type = 'student';"

    query12 = "WITH NEWTABLE AS (SELECT name, salary_hour FROM Trainer t JOIN employee e ON t.person_id = e.card_id JOIN person p ON p.card_id = t.person_id) SELECT NT.name FROM NEWTABLE NT WHERE NT.salary_hour = (SELECT MAX(NT2.salary_hour) FROM NEWTABLE NT2 WHERE NT2.salary_hour < (SELECT MAX(NT3.salary_hour) FROM NEWTABLE NT3));"

    query13 = "select count(distinct(day(timestamp))) from location_reading where person_id in ( select card_id from person where name = 'Mekhi Sporer') and space_id in (select space_id from space where description = 'weight room')"

    query14 = "SELECT name FROM person p JOIN location_reading lr ON p.card_id = lr.person_id JOIN space sp ON lr.space_id = sp.space_id JOIN member m on p.card_id = m.card_id WHERE sp.description = 'cardio room' AND MONTH(lr.timestamp) = 5 GROUP BY p.card_id ORDER BY COUNT(lr.timestamp) DESC;"

    query15 = "select x.description, avg(x.occupancy) as avg_occupancy from (select s.description,e.event_id,e.space_id,count(*) as occupancy from space s join events e on s.space_id = e.space_id join attends at on e.event_id = at.event_id group by e.event_id, e.space_id) x group by space_id, x.description order by avg_occupancy limit 1"
    
    cursor.execute(query1)
    
    print(cursor.fetchall())