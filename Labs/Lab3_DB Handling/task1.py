import pymysql
from Exceptions import *

class User:
    def __init__(self,accNo,password,bal):
        self.__accountNo = accNo
        self.__password = password
        self.__balance = bal

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self,accNo):
        self.__accountNo = accNo

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, pw):
        self.__password = pw

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, bal):
        self.__balance = bal

    def printUserData(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host = 'localhost', user='root', password='pythOn~2022', database='mehakdb')
            mydbCursor = mydb.cursor()
            sql = "Select user_id,account_no,account_balance,password from users"
            mydbCursor.execute(sql)
            myresults = mydbCursor.fetchall()
            for r in myresults:
                print("User_ID: ", r[0], "   Account No# ", r[1], "   Account Balance: ", r[2], "   Password: ",r[3])
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()
            if mydb != None:
                mydb.close()

u = User('acc00123','1234',2300)
u.printUserData()

class ATM(User):
    def __init__(self,accNo,password,balance):
        super.__init__(self,accNo,password,balance)



def register():
    opening_account_balance = 100
    account_balance = opening_account_balance
    accountNo = input("\nEnter Account No : ")
    password = input("Enter Password(4-digit number): ")
    while True:
        try:
            if len(password) != 4:
                raise InvalidPin
            else:
                break
        except InvalidPin:
            print("Invalid Pin")
            password = input("Enter Password(4-digit number): ")
    try:
        file = open("atmData.txt", "a")
        file.write(accountNo + "," + password + "," + str(account_balance) + "\n")
        file.close()
        print("\nYour account has been registered as " + accountNo + "\n")
    except Exception:
        print("Permission denied while creating a file.")


def login():
    try:
        file = open("atmData.txt", "r")
        data = file.readlines()
        file.close()
    except Exception:
        print("Please Register First.")
        return
    account_number = input("Account Number: ")
    while account_number == '':
        account_number = input("Account Number: ")
    password = input("Password: ")
    while password == '':
        password = input("Password: ")
    exist = False
    user = []
    try:
        for strings in data:
            string_data = strings.split(',')
            if string_data[0] == account_number and string_data[1] == password:
                user = string_data
                exist = True
        if not exist:
            raise AccountNotFound
    except AccountNotFound:
        print("\nAccount not Found")
        return
    choice = login_menu()
    while choice != 4:
        if choice == 1:
            display_balance(user)
        elif choice == 2:
            new_balance = withdraw(user)
            user[2] = str(new_balance)
            for i in range(0, len(data)):
                string_data = data[i].split(',')
                if string_data[0] == user[0]:
                    data[i] = user[0] + "," + user[1] + "," + user[2] + "\n"
                    break
            update_file(data)
        elif choice == 3:
            new_balance = deposit(user)
            user[2] = str(new_balance)
            for i in range(0, len(data)):
                string_data = data[i].split(',')
                if string_data[0] == user[0]:
                    data[i] = user[0] + "," + user[1] + "," + user[2] + "\n"
                    break
            update_file(data)
        choice = login_menu()


def main():
    choice = 0
    while choice != 3:
        print('\n1. Register')
        print("2. Login")
        print("3. Exit")
        choice = input("> ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 3:
                raise Exception
            if choice == 1:
                register()
            elif choice == 2:
                login()
        except Exception:
            print("Invalid choice")
    print("System Terminated Successfully...")


print("\n=== ATM System in Python ===")
if __name__ == "__main__":
    main()























'''
u = User('ACC0002456',2300,'mehak1234')
u.printUserData()
'''