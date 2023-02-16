import pymysql
from contact import contact
from Exceptions import *
#from Student import Student,Friend

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

    def getContacts(self):
        contact_list= []
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from contacts"
            self.__cursor.execute(query)
            data = self.__cursor.fetchall()
            for item in data:
                cont = contact(item[1],item[2],item[3],item[4])
                contact_list.append(cont)
        except Exception as e:
            print(str(e))
        finally:
            return contact_list


    def insertContact(self,contact):
        try:
            if self.__connection is None:
                self.connect()
            contact_list = self.getContacts()
            if contact_list is not None:
                for cont in contact_list:
                    if cont.name.lower() == contact.name.lower():
                        raise InvalidName('Contact name must be unique')
            query = "insert into contacts(name,mobileno,city,profession) values(%s,%s,%s,%s)"
            args = (contact.name,contact.mobileno,contact.city,contact.profession)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except InvalidName as e:
            print(str(e))
            return False
        except Exception as e:
            print(str(e))
            return False

    def getContactByName(self,name):
        try:
            if self.__connection is None:
                self.connect()
            query="select * from contacts where name=%s"
            args=(name)
            self.__cursor.execute(query,args)
            data = self.__cursor.fetchall()
            for d in data:
                cont = contact(d[1],d[2],d[3],d[4])
                return cont
        except Exception as e:
            print(str(e))
            return None

