from View import StudentView,FacultyView
from Utils import isValidCGPA
from DB import DBHandler
from Exceptions import *

class Controller:
    def register_student(self):
        status = False
        try:
            studView = StudentView()
            student = studView.register_student()
            if not isValidCGPA(student.cgpa):
                raise Invalid_CGPA('CGPA must be between 0 and 4.')
            d = DBHandler()
            status = d.register_student(student)
        except Invalid_CGPA as e:
            print(str(e))
            status = False
        except Exception as e:
            print(str(e))
            status = False
        finally:
            studView.registration_status(status)

    def register_faculty(self):
        facView = FacultyView()
        fac = facView.register_faculty()
        d = DBHandler()
        status = d.register_faculty(fac)
        facView.registration_status(status)

    def authenticate_student(self):
        try:
            studView = StudentView()
            studTuple = studView.authenticate_student()
            d = DBHandler()
            student = d.get_student(studTuple[0],studTuple[1])
            if student is None:
                raise StudentNotFound('Invalid username or password')
            else:
                print(student)
                print('Login Successful!!')
        except StudentNotFound as e:
            print(str(e))
        except Exception as e:
            print(str(e))

    def authenticate_faculty(self):
        try:
            facView = FacultyView()
            facTuple = facView.authenticate_faculty()
            d = DBHandler()
            fac = d.get_faculty(facTuple[0],facTuple[1])
            if fac is None:
                raise FacultyNotFound('Invalid username or password')
            else:
                print(fac)
                print('Login Successful!!')
        except FacultyNotFound as e:
            print(str(e))
        except Exception as e:
            print(str(e))

    def update_student(self):
        status = False
        try:
            studView = StudentView()
            student = studView.update_student()
            if not isValidCGPA(student.cgpa):
                raise Invalid_CGPA('CGPA must be between 0 and 4.')
            d = DBHandler()
            status = d.update_student(student)
        except Invalid_CGPA as e:
            print(str(e))
            status = False
        except Exception as e:
            print(str(e))
            status = False
        finally:
            studView.updation_status(status)

    def update_faculty(self):
        facView = FacultyView()
        fac = facView.update_faculty()
        d = DBHandler()
        status = d.update_faculty(fac)
        facView.updation_status(status)

    def delete_student(self):
        studView = StudentView()
        studID = studView.delete_student()
        d = DBHandler()
        status = d.delete_student(studID)
        studView.deletion_status(status)

    def delete_faculty(self):
        facView = FacultyView()
        facID = facView.delete_faculty()
        d = DBHandler()
        status = d.delete_faculty(facID)
        facView.deletion_status(status)