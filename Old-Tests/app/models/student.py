
from flask_login import UserMixin

class Student(Person):
    __tablename__ = "students"

    email_address = db.Column(db.String(255),db.ForeignKey(
        "person.email_address"))

    student_id = db.Column(db.String(50),unique=True, primary_key = True)
    major_id = db.Column(db.String(50),db.ForeignKey("subjects.subject_id"))
    created_at = db.Column(db.DateTime,default=datetime.now)
    updated_at = db.Column(db.DateTime,onupdate = datetime.now)
    
    __mapper_args__ {
        "polymorphic_identity" : "students",
    } 

    def __repr__(self):
        return f"<Student ID {self.student_id}>"



