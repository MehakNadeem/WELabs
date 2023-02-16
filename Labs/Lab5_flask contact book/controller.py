from contact import contact
from DB import DBHandler
from Exceptions import *

class controller:
    def insertContact(self,contact):
        try:
            if len(contact.mobileno) > 11:
                raise InvalidPhoneNumber('Phone number must be 11 digit.')
            for digit in contact.mobileno:
                if digit < '0' and digit > '9':
                    raise InvalidPhoneNumber('Phone number must be digit.')
            db = DBHandler()
            status = db.insertContact(contact)
            return True
        except InvalidPhoneNumber as e:
            print(str(e))
            return True
        except Exception as e:
            print(str(e))
            return True

    def showContact(self):
        try:
            db = DBHandler()
            contact_list = db.getContacts()
            if contact_list is None:
                raise InvalidContact('No contact exist')
            return contact_list
        except InvalidContact as e:
            print(str(e))
            return None
        except Exception as e:
            print(str(e))
            return None

    def getContactByName(self,name):
        try:
            db = DBHandler()
            one_contact=db.getContactByName(name)
            if one_contact is None:
                raise InvalidContact('No such contact exist')
            return one_contact
        except InvalidContact as e:
            print(str(e))
            return None
        except Exception as e:
            print(str(e))
            return None



