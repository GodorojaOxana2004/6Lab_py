from datetime import datetime

class Employee:
    def __init__(self, nameEmployee, phone, bday, email, position):
        self.__nameEmployee = nameEmployee
        self.__phone = phone
        self.__bday = bday
        self.__email = email
        self.__position = position

    @property
    def nameEmployee(self):
        return self.__nameEmployee

    @nameEmployee.setter
    def nameEmployee(self, name):
        self.__nameEmployee = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def bday(self):
        return self.__bday

    @bday.setter
    def bday(self, bday):
        self.__bday = bday

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def calculateAge(self):
        list_date = []
        list_date = self.__bday.split('.')
        bday_day = list_date[0]
        bday_month = list_date[1]
        bday_year = list_date[2]

        today = datetime.today()
        age = today.year - int(bday_year)
        if today.month < int(bday_month) or (today.month == int(bday_month) and today.day < int(bday_day)):
            age -= 1
        return age

    def _calculateSalary(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, nameEmployee, phone, bday, email, position, nmbrOfHour, hourlyPay):
        super().__init__(nameEmployee, phone, bday, email, position)
        self.__nmbrOfHour = nmbrOfHour
        self.__hourlyPay = hourlyPay

    def _calculateSalary(self):
        return self.__nmbrOfHour * self.__hourlyPay


class SalaryEmployee(Employee):
    def __init__(self, nameEmployee, phone, bday, email, position, salary):
        super().__init__(nameEmployee, phone, bday, email, position)
        self.__salary = salary

    def _calculateSalary(self):
        return self.__salary
