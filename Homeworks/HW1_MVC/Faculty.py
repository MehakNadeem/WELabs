from User import User

class Faculty(User):
    def __init__(self,username='',password='',fid= 0,designation ='',subject =''):
        super().__init__(username, password)
        self.facultyID=fid
        self.designation=designation
        self.subject=subject

    def __str__(self):
        return f"Username: {self.username}\nPassword: {self.password}\nFaculty ID: {self.facultyID}\nDesignation: {self.designation}\nSubject: {self.subject}"

