

class Person(db.Model):

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_address = db.Column(db.String(255),
                    unique = True,
                    primary_key = True)
    person_type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity' :"person",
        'polymorphic_on' : person_type
    }

    def __repr__(self):
        return f"<{self.person_type}: {self.first_name} {self.last_name}>"
        