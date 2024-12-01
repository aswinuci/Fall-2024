from relational_algebra import *

class Expressions:
    expression1 = Projection(
        Selection(
            NaturalJoin(
                NaturalJoin(
                    Relation("author"),
                    Relation("pub_info")
                ),
                Relation("field_conference")
            ),
            And(
                And(
                    Equals("author.affiliation", "University of California, Berkeley"),
                    Equals("field_conference.field", "Databases")
                ),
                And(
                    GreaterEquals("pub_info.year", 2010),
                    LessThan("pub_info.year", 2025)
                )
            )
        ),
        ["author.name", "pub_info.conference", "pub_info.year", "pub_info.count"]
    )

    expression2 = Projection(
        Selection(
            NaturalJoin(
                NaturalJoin(
                    Relation("field_conference"),
                    Relation("pub_info")
                ),
                Relation("author")
            ),
            And(
                Equals("field_conference.major", "Computer Science"),
                Not(Equals("author.affiliation","University of California, Irvine"))
            )
        ),
        ["field_conference.conference"]
    )
