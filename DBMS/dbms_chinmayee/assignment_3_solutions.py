from relational_algebra import *


class Expressions():
    # The following query is the solution to: Retrieve the name of all Trainers who have the credentials CNS
    sample_query = Projection(
        NaturalJoin(Selection(Relation("Trainer"), Equals("credentials", "CNS")), Relation("person")), ["name"])

    expression1 = Projection(Relation("Person"), ["name", "gender"])

    expression2 = Projection(NaturalJoin(
        NaturalJoin(Relation("Person"), Selection(Relation("non_student"), Equals("member_type", "Faculty"))),
        Relation("university_affiliate")), ["name", "department"])

    expression3 = Projection(
        ThetaJoin(
            NaturalJoin(
                Selection(
                    Relation("location_reading"),
                    And(
                        GreaterEquals('timestamp', '2023-04-01 00:00:00'),
                        LessThan('timestamp', '2023-04-02 00:00:00')
                    )
                ),
                Selection(
                    Relation("space"),
                    Or(
                        Equals("space_description", "weight room"),
                        Equals("space_description", "cardio room")
                    )
                )
            ),
            Relation("person"),
            Equals('location_reading.person_id', 'person.card_id')
        ),
        ["name"]
    )

    expression4 = Projection(NaturalJoin(Relation("person"),
                                         Division(Relation("attends"), Projection(Relation("attends"), ["event_id"]))),
                             ["name"])

    expression5 = Projection(
        Selection(NaturalJoin(Relation("events"), Relation("space")), GreaterEquals("capacity", "max_capacity")),
        ["event_id"])

    expression6 = Projection(
        NaturalJoin(
            NaturalJoin(
                Division(
                    Projection(
                        NaturalJoin(
                            NaturalJoin(
                                Relation('usage_reading'), Relation('equipment')
                            ),
                            Selection(
                                Relation('space'),
                                Equals('space_description', 'cardio room')
                            )
                        ),
                        ['card_id', 'equipment_id'],
                    ),
                    Projection(
                        NaturalJoin(
                            NaturalJoin(
                                Relation('usage_reading'), Relation('equipment')
                            ),
                            Selection(
                                Relation('space'),
                                Equals('space_description', 'cardio room')
                            )
                        ),
                        ['equipment_id'],
                    )
                ),
                Relation('student')
            ), Relation('person')),
        ['name']
    )

    expression7 = Projection(Selection(Relation("Equipment"), Equals("is_available", 1)),
                             ["equipment_id", "equipment_type"])

    expression8 = Projection(NaturalJoin(Relation('person'), Relation('employee')), ['name'])

    expression9 = Projection(
        (NaturalJoin(NaturalJoin(Relation("member"),
                                 NaturalJoin(Relation('attends'),
                                             Selection(NaturalJoin(Relation('events'), Relation('space')),
                                                       Equals('space_description', 'yoga studio')))),
                     Relation('person'))),

        ['name'])

    expression10 = Projection(
        NaturalJoin(NaturalJoin(NaturalJoin(Relation("person"), Relation("family")),
                                Relation('attends')),
                    Selection(Relation("events"), Equals("events.description", "Summer Splash Fest"))),
        ['name'])

    # sql_con = sqlite3.connect("sample220P.db")
    #
    # result = expression9.evaluate(sql_con=sql_con)
    # print(result.rows)
