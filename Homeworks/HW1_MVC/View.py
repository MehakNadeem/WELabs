from Student import Student
from Faculty import Faculty

class StudentView:
    def register_student(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        id = int(input('Enter student id: '))
        sems = input("Enter semester: ")
        cgpa = float(input("Enter cgpa: "))
        major = input('Enter major: ')
        stud = Student(username,password,id,sems,cgpa,major)
        return stud

    def registration_status(self,status):
        if status:
            print("Student registered successfully!!")
        else:
            print("ERROR! Student can't be registered.")

    def authenticate_student(self):
        username = input('Enter student name: ')
        password = input('Enter Password: ')
        return (username,password)

    def update_student(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        id = int(input('Enter student id: '))
        sems = input("Enter semester: ")
        cgpa = float(input("Enter cgpa: "))
        major = input('Enter major: ')
        stud = Student(username,password,id, sems, cgpa, major)
        return stud

    def updation_status(self,status):
        if status:
            print("Student data updated successfully!!")
        else:
            print("ERROR! Student data can't be updated.")

    def delete_student(self):
        id = int(input('Enter student id to delete: '))
        return id

    def deletion_status(self,status):
        if status:
            print("Student data deleted successfully!!")
        else:
            print("ERROR! Student data can't be deleted.")

class FacultyView:
    def register_faculty(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        id = int(input("Enter faculty ID: "))
        desg = input("Enter designation: ")
        subj = input("Enter subject: ")
        fac = Faculty(username,password,id,desg,subj)
        return fac

    def registration_status(self, status):
        if status:
            print("Faculty member registered successfully!!")
        else:
            print("ERROR! Faculty member can't be registered.")

    def authenticate_faculty(self):
        username = input('Enter faculty member name: ')
        password = input('Enter Password: ')
        return (username,password)

    def update_faculty(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        id = int(input("Enter faculty ID: "))
        desg = input("Enter designation: ")
        subj = input("Enter subject: ")
        fac = Faculty(username,password,id, desg, subj)
        return fac

    def updation_status(self,status):
        if status:
            print("Faculty member data updated successfully!!")
        else:
            print("ERROR! Faculty member data can't be updated.")

    def delete_faculty(self):
        id = int(input("Enter faculty ID to delete: "))
        return id

    def deletion_status(self,status):
        if status:
            print("Faculty member data deleted successfully!!")
        else:
            print("ERROR! Faculty member data can't be deleted.")