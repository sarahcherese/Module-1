#Name: Sarah Price
#File: deans_list.py
#Description: This program will determine if a student is on the Dean's List or Honor Roll
last_name = input("Enter your last name: ")
while last_name != "ZZZ":
    first_name = input("Enter your first name: ")
    gpa = float(input("Enter your GPA: "))
    if gpa >= 3.5:
        print(first_name + " " + last_name + " is on the Dean's List")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " is on the Honor Roll")
    else:
        print(first_name + " " + last_name + " is not on the Dean's List or Honor Roll")
    last_name = input("Enter your last name: ")
