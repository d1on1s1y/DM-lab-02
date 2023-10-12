import re
class Employee:
    def __init__(self, position = "Джуніор розробник"):
        self.name = str(input("Введіть ім'я працівника "))
        self.age = int(input("Введіть вік працівника "))
        self.pay = int(input("Введіть зарплату працівника "))
        self.position = position
        self.phone = ""
        self.email = ""
    
    def printDetails(self):
        print("Ім'я працівника ",self.name)
        print("Вік працівника ",self.age)
        print("Зарплата працівника ",self.pay)
        print("Посада працівника ",self.position)
        if self.phone:
            print("Номер телефону: ", self.phone)
        if self.email:
            print("Адреса електронної пошти: ", self.email)
            
    def changePhone(self):
        self.phone = str(input("Введіть номер телефону "))
        while(len(self.phone) != 10 or  (not self.phone.isdigit())):
            self.phone = str(input("Введіть номер телефону, він має містити тільки циффри і бути 10 символів в довжину "))

    def changeEmail(self):
        self.email = str(input("Введіть свою адресу електронної пошти "))
        while(not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$', self.email)):
            self.email = str(input("Введіть корректне значення! "))

worker1 = Employee("Мідл розробник")