stud_list = [{"name": "mehak", "homework_marks": [20, 10, 15], "quiz_marks": [2, 3, 5, 7], "sems_project_marks": 50.5},
             {"name": "hira", "homework_marks": [30, 10, 25], "quiz_marks": [2.5, 5, 10, 7],
              "sems_project_marks": 70.9},
             {"name": "jannat", "homework_marks": [25, 10, 15], "quiz_marks": [8, 6, 5, 7.5],
              "sems_project_marks": 80.78},
             {"name": "ali", "homework_marks": [7, 30, 15], "quiz_marks": [7, 3, 9, 8], "sems_project_marks": 50.57},
             {"name": "laraib", "homework_marks": [50, 10, 5], "quiz_marks": [8, 9, 5, 7], "sems_project_marks": 78.98}]


def print_students(student_list):
    for i in range(5):
        print("Name: ", stud_list[i]["name"])
        print("Homework Marks: ", stud_list[i]["homework_marks"])
        print("Quiz Marks: ", stud_list[i]["quiz_marks"])
        print("Semester Project Marks: ", stud_list[i]["sems_project_marks"])
        print('\n')


def average(mylist):
    s = 0
    for i in range(len(mylist)):
        s = s + mylist[i]
    avg = float(s / len(mylist))
    return avg


def get_average_of_student(mydict):
    a = average(mydict["homework_marks"])
    b = average(mydict["quiz_marks"])
    mytuple = (a, b)
    return mytuple

def weighted_average(stud_tup, proj_marks):
    h = float(stud_tup[0] * 25) / 100
    q = float(stud_tup[1] * 40) / 100
    p = float(proj_marks * 35) / 100
    return h + q + p

def get_letter_grade(wavg):
    if ((wavg >= 80) and (wavg <= 100)):
        return 'A'
    elif ((wavg >= 70) and (wavg <= 79)):
        return 'B'
    elif ((wavg >= 60) and (wavg <= 69)):
        return 'B'
    elif ((wavg >= 50) and (wavg <= 59)):
        return 'C'
    else:
        return 'F'

def get_class_average(list_avg):
    return average(list_avg)


print_students(stud_list)

av = average(stud_list[0]["homework_marks"])
print("Average: ", float(av))

g = get_average_of_student(stud_list[4])

print("Weighted Average: ", weighted_average(g, 78.98))


list_of_avg = []
for i in range(5):
    g = get_average_of_student(stud_list[i])
    list_of_avg.append(weighted_average(g, stud_list[i]["sems_project_marks"]))

print("List of Weighted Average: ", list_of_avg)

print("Class Average: ", float(get_class_average(list_of_avg)))



