def print_header(line):
    print()
    print('-'*40)
    print(line.center(40))
    print('-'*40)

def print_menu():
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    print("-" * 40)


def isValidCGPA(cgpa):
    if cgpa >= 0 and cgpa < 4:
        return True