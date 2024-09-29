from relational_algebra import *
import sqlite3
class Expressions():

    # The following query is the solution to: Retrieve the name of all Trainers who have the credentials CNS
    sample_query = Projection(NaturalJoin(Selection(Relation("Trainer"),Equals("credentials","CNS")),Relation("person")),["name"])

    expression1 = Projection(Relation("Person"), ["name", "gender"])

    expression2 = Projection(
        NaturalJoin(
            NaturalJoin(
                Selection(Relation("non_student"), Equals("member_type", "Faculty")), 
                Relation("university_affiliate")), Relation("person")), ["name", "department"])

    expression3 = Projection(
        ThetaJoin(
            Relation("person"),
            Selection(
                NaturalJoin(
                    Relation("space"),
                    Selection(Relation("location_reading"), Equals("timestamp", "2023-04-01 00:00:00"))
                ), Or(Equals("space_description", "cardio room"), Equals("space_description", "weight room"))
            )
            ,
            Equals("location_reading.person_id", "person.card_id")
        ), ["name"]
    )

    expression4 = Projection(
            NaturalJoin(
                Division(
                    Relation("attends"),
                    Projection(Relation("events"), ["event_id"])
                ),
                Relation("person")
            ),
            ["name"]
    )

    expression5 = Projection(
        Selection(
            ThetaJoin(Relation("space"), Relation("events"), Equals("space.space_id", "events.space_id")),
            GreaterEquals("capacity", "max_capacity")
        ),
        ["event_id"]
    )

    expression6 = Projection(
                    NaturalJoin(Relation("person"),
                        NaturalJoin(
                            Projection(NaturalJoin("usage_reading",
                                NaturalJoin(Relation("equipment"),
                                    Selection(Relation("space"),Equals("space_description","cardio room")))),["card_id","equipment_id"]) / (Projection(NaturalJoin(Relation("equipment"),
                                        Selection(Relation("space"),Equals("space_description","cardio room"))), ["equipment_id"])) , Relation("student"))),["name"])

    
    # sql_con = sqlite3.connect("sample220P.db")

    # result = sample_query.evaluate(sql_con=sql_con)
    # print(result.rows)