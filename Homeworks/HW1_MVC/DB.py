import pymysql
from Student import Student
from Faculty import Faculty
from User import User
from Exceptions import *

class DBHandler:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = pymysql.connect(host='localhost', user='root', password='pythOn~2022', database='fcit')
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(str(e))

    def disconnect(self):
        if self.__connection is not None:
            self.__connection.close()

    def insert_user(self,usr):
        if self.__connection is None:
            self.connect()
        try:
            query = 'insert into user(username,password) values (%s,%s)'
            args = (usr[0],usr[1])
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def select_user(self,args):
        if self.__connection is None:
            self.connect()
        try:
            query = 'select user_ID from user where user.username = %s and user.password = %s'
            self.__cursor.execute(query,args)
            idList = self.__cursor.fetchall()
            for id in idList:
                usrID = id[0]
                return usrID
        except Exception as e:
            print(str(e))

    def select_Student(self,sql):
        if self.__connection is None:
            self.connect()
        students_list = []
        try:
            self.__cursor.execute(sql)
            data = self.__cursor.fetchall()
            for row in data:
                query = 'select * from user,student where user.user_ID = student.userid and student_ID = %s'
                args = (row[0])
                self.__cursor.execute(query,args)
                userData = self.__cursor.fetchall()
                for u in userData:
                    stu = Student(u[1],u[2],row[0], row[1],row[2],row[3])
                    students_list.append(stu)
            return students_list
        except Exception as e:
            print(str(e))
            return None

    def select_faculty(self, sql):
        if self.__connection is None:
            self.connect()
        faculty_list = []
        try:
            self.__cursor.execute(sql)
            data = self.__cursor.fetchall()
            for row in data:
                query = 'select * from user,faculty where user.user_ID = faculty.user_ID and faculty_ID = %s'
                args = (row[0])
                self.__cursor.execute(query, args)
                userData = self.__cursor.fetchall()
                for u in userData:
                    stu = Faculty(u[1],u[2],row[0], row[1], row[2])
                    faculty_list.append(stu)
            return faculty_list
        except Exception as e:
            print(str(e))
            return None

    def register_student(self,student):
        if self.__connection is None:
            self.connect()
        try:
            studList = self.select_Student("select * from student")
            for s in studList:
                if student.studentID == s.studentID:
                    raise InvalidStudent("Invalid Student ID.")
            self.insert_user((student.username,student.password))
            args1 = (student.username,student.password)
            usrID = self.select_user(args1)
            query = 'insert into student (student_ID,semester,cgpa,major,userid) values (%s,%s,%s,%s,%s)'
            args = (student.studentID,student.semester,student.cgpa,student.major,usrID)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except InvalidStudent as e:
            print(str(e))
            return False
        except Exception as e:
            print(str(e))
            return False

    def register_faculty(self, faculty):
        if self.__connection is None:
            self.connect()
        try:
            facList = self.select_faculty("select * from faculty")
            for f in facList:
                if faculty.facultyID == f.facultyID:
                    raise Invalid_Faculty('Invalid Faculty ID.')
            self.insert_user((faculty.username, faculty.password))
            args1 = (faculty.username, faculty.password)
            usrID = self.select_user(args1)
            query = 'insert into faculty (faculty_ID,designation,subject,user_ID) values (%s,%s,%s,%s)'
            args = (faculty.facultyID,faculty.designation,faculty.subject,usrID)
            self.__cursor.execute(query, args)
            self.__connection.commit()
            return True
        except Invalid_Faculty as e:
            print(str(e))
            return False
        except Exception as e:
            print(str(e))
            return False


    def get_student(self,username, password):
        if self.__connection is None:
            self.connect()
        try:
            query = 'select user.username, user.password, student.student_ID, student.semester, student.cgpa, student.major from student,user where user.user_ID = student.userid and user.username = %s and user.password =%s'
            args = (username,password)
            self.__cursor.execute(query,args)
            data = self.__cursor.fetchall()
            for d in data:
                return Student(d[0],d[1],d[2],d[3],d[4],d[5])
        except Exception as e:
            print(str(e))


    def get_faculty(self, username, password):
        if self.__connection is None:
            self.connect()
        try:
            query = 'select user.username, user.password, faculty.faculty_ID, faculty.designation, faculty.subject from faculty,user where user.user_ID = faculty.user_ID and user.username = %s and user.password =%s'
            args = (username, password)
            self.__cursor.execute(query, args)
            data = self.__cursor.fetchall()
            for d in data:
                return Faculty(d[0],d[1],d[2],d[3],d[4])
        except Exception as e:
            print(str(e))

    def update_student(self,studObj):
        if self.__connection is None:
            self.connect()
        try:
            query = 'update student set semester = %s , cgpa = %s, major = %s where student_ID = %s '
            args = (studObj.semester,studObj.cgpa,studObj.major,studObj.studentID)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def update_faculty(self,facObj):
        if self.__connection is None:
            self.connect()
        try:
            query = 'update faculty set designation = %s , subject = %s where faculty_ID = %s '
            args = (facObj.designation,facObj.subject,facObj.facultyID)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def delete_student(self,stud_id):
        if self.__connection is None:
            self.connect()
        try:
            query = 'delete from student where student_ID = %s'
            args = (stud_id)
            self.__cursor.execute(query, args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def delete_faculty(self,fac_id):
        if self.__connection is None:
            self.connect()
        try:
            query = 'delete from faculty where faculty_ID = %s'
            args = (fac_id)
            self.__cursor.execute(query, args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False






