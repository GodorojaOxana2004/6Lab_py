import re
import classes_lab6

def get_employee_details():
    name = input("Введите имя: ")
    while not re.match("^[A-Za-z]+$", name):
        print("Имя должно состоять только из букв.")
        name = input("Введите имя: ")

    phone = input("Введите номер телефона: ")
    while not re.match("^\\+373[0-9]{8}$", phone):
        print("Номер телефона должен соответствовать шаблону +373сссссссс.")
        phone = input("Введите номер телефона: ")

    bday = input("Введите дату рождения: ")
    while not re.match("^(0[1-9]|[12][0-9]|3[01])\\.(0[1-9]|1[012])\\.(19[6-9][0-9]|200[0-7])$", bday):
        print("Дата рождения должна соответствовать шаблону дд.мм.гггг.")
        bday = input("Введите дату рождения: ")

    email = input("Введите email: ")
    while not re.match("^[A-Za-z0-9._-]{2,20}@{1}[A-Za-z]{4,7}\\.{1}[A-Za-z]{2,4}$", email):
        print("Email должен содержать от 2 до 20 букв или цифр, затем символ @, затем от 4 до 7 букв, затем точку и затем от 2 до 4 букв.")
        email = input("Введите email: ")

    position = input("Введите специальность: ")
    while not re.match("^[A-Za-z]{4,20}$", position):
        print("Специальность должна состоять только из букв (от 4 до 20).")
        position = input("Введите специальность: ")

    return name, phone, bday, email, position

def main():
    list_employee = []
    list_hourly_employee = []
    list_salary_employee = []

    for _ in range(2):
        print("\nEmployee")
        name, phone, bday, email, position = get_employee_details()
        list_employee.append(classes_lab6.Employee(name, phone, bday, email, position))

    for _ in range(2):
        print("\nHourly Employee")
        name, phone, bday, email, position = get_employee_details()
        nmbrOfHour = float(input("Введите количество часов: "))
        hourlyPay = float(input("Введите оплату за час: "))
        list_hourly_employee.append(classes_lab6.HourlyEmployee(name, phone, bday, email, position, nmbrOfHour, hourlyPay))

    for _ in range(2):
        print("\nSalary Employee")
        name, phone, bday, email, position = get_employee_details()
        salary = float(input("Введите зарплату: "))
        list_salary_employee.append(classes_lab6.SalaryEmployee(name, phone, bday, email, position, salary))

    for obj in list_employee:
        print("Возраст " + obj.nameEmployee + " : " + str(obj.calculateAge()))

    for obj in list_hourly_employee:
        print("Зарплата" + obj.nameEmployee + " : " + str(obj._calculateSalary()))

    for obj in list_salary_employee:
        print("Зарплата" + obj.nameEmployee + " : " + str(obj._calculateSalary()))

if __name__ == "__main__":
    main()
