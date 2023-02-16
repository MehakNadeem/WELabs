from User import User

class Student(User):
    def __init__(self,username='',password='',sID= 0,semester='',cgpa=0.00,major=''):
        super().__init__(username,password)
        self.studentID=sID
        self.semester=semester
        self.cgpa=cgpa
        self.major=major

    def __str__(self):
        return f'Username: {self.username}\nPassword: {self.password}\nStudent_ID: {self.studentID}\nSemester: {self.semester}\nCGPA: {self.cgpa}\nMajor: {self.major}'

