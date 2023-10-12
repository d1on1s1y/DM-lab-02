import re
class Student:


    def __init__(self, name ="John Doe", courses =[]):
        self.name = name
        self.courses = courses
        self.phone = ""
        self.email = ""
        print("Створено об’єкт для "+ name)
        
    def printDetails(self):
        print("Ім’я: ", self.name)
        print("Курси: ", self.courses)
        if self.phone:
            print("Номер телефону: ", self.phone)
        if self.email:
            print("Адреса електронної пошти: ", self.email)
            
    def enroll(self, course):
        self.courses.append(course)
        
    def changePhone(self):
        self.phone = str(input("Введіть номер телефону "))
        while(len(self.phone) != 10 or  (not self.phone.isdigit())):
            self.phone = str(input("Введіть номер телефону, він має містити тільки циффри і бути 10 символів в довжину "))

    def changeEmail(self):
        self.email = str(input("Введіть свою адресу електронної пошти "))
        while(not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$', self.email)):
            self.email = str(input("Введіть корректне значення! "))
        
std1 = Student("Denchik",["IA-32"])
std1.changeEmail()
std1.printDetails()


