class Subject(db.Model):
    __tablename__ = 'subjects'

    class_id = db.Column(db.String(50),unique = True,
                                    primary_key = True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    teacher_id = db.relationship(db.String(50),
                                 db.ForeignKey('teachers.staff_id'))

