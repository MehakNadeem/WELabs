from Utils import print_header,print_menu
from Controller import Controller



cont = Controller()

choice = 1
while True:
    try:
        print_header('Welcome')
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print("-" * 40)
            print('\t1. Register Student')
            print('\t2. Register Faculty')
            print("-" * 40)
            ch1 = int(input('Select user to register: '))
            if ch1 == 1:
                print('---Enter Student Details---')
                cont.register_student()
            elif ch1 == 2:
                print('---Enter Faculty Details---')
                cont.register_faculty()
        elif choice == 2:
            print("-" * 40)
            print('\t1. Login Student')
            print('\t2. Login Faculty')
            print("-" * 40)
            ch2 = int(input('Select user to Login: '))
            if ch2 == 1:
                print('---Enter Student Details---')
                cont.authenticate_student()
                print("-" * 40)
                print('1. Edit Profile')
                print('2. Delete Profile')
                print("-" * 40)
                ch3 = int(input('Press 1 for editing or 2 for deleting profile: '))
                if ch3 == 1:
                    cont.update_student()
                elif ch3 == 2:
                    cont.delete_student()
            elif ch2 == 2:
                print('---Enter Faculty Details---')
                cont.authenticate_faculty()
                print("-" * 40)
                print('1. Edit Profile')
                print('2. Delete Profile')
                print("-" * 40)
                ch4 = int(input('Press 1 for editing or 2 for deleting profile: '))
                if ch4 == 1:
                    cont.update_faculty()
                elif ch4 == 2:
                    cont.delete_faculty()
        elif choice == 3:
            print_header('Exit successfully!!')
            break
        else:
            print('Invalid Choice')
            break
    except ValueError as e:
        print(str(e))