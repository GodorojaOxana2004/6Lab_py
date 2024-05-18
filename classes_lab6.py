from datetime import datetime  # Импортируем модуль для работы с датой и временем

# Создаем класс Employee (Сотрудник)
class Employee:
    # Инициализируем объект с основными атрибутами
    def __init__(self, nameEmployee, phone, bday, email, position):
        self.__nameEmployee = nameEmployee  # Имя сотрудника (скрытое поле)
        self.__phone = phone  # Телефон (скрытое поле)
        self.__bday = bday  # Дата рождения (скрытое поле)
        self.__email = email  # Электронная почта (скрытое поле)
        self.__position = position  # Должность (скрытое поле)

    # Создаем геттер и сеттер для имени
    @property
    def nameEmployee(self):
        return self.__nameEmployee

    @nameEmployee.setter
    def nameEmployee(self, name):
        self.__nameEmployee = name

    # Создаем геттер и сеттер для телефона
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    # Создаем геттер и сеттер для даты рождения
    @property
    def bday(self):
        return self.__bday

    @bday.setter
    def bday(self, bday):
        self.__bday = bday

    # Создаем геттер и сеттер для электронной почты
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # Создаем геттер и сеттер для должности
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    # Метод для расчета возраста сотрудника
    def calculateAge(self):
        list_date = []  # Создаем пустой список
        list_date = self.__bday.split('.')  # Разделяем дату рождения на день, месяц и год
        bday_day = list_date[0]  # День рождения
        bday_month = list_date[1]  # Месяц рождения
        bday_year = list_date[2]  # Год рождения

        today = datetime.today()  # Получаем текущую дату
        age = today.year - int(bday_year)  # Вычисляем возраст
        # Проверяем, был ли день рождения в этом году
        if today.month < int(bday_month) or (today.month == int(bday_month) and today.day < int(bday_day)):
            age -= 1  # Уменьшаем возраст, если день рождения еще не прошел
        return age  # Возвращаем возраст

    # Заготовка для метода расчета зарплаты (переопределяется в дочерних классах)
    def _calculateSalary(self):
        pass

# Создаем класс HourlyEmployee (Почасовой сотрудник), наследуемый от Employee
class HourlyEmployee(Employee):
    def __init__(self, nameEmployee, phone, bday, email, position, nmbrOfHour, hourlyPay):
        super().__init__(nameEmployee, phone, bday, email, position)  # Вызываем конструктор родительского класса
        self.__nmbrOfHour = nmbrOfHour  # Количество отработанных часов
        self.__hourlyPay = hourlyPay  # Почасовая оплата

    # Метод для расчета зарплаты почасового сотрудника
    def _calculateSalary(self):
        return self.__nmbrOfHour * self.__hourlyPay  # Умножаем количество часов на ставку

# Создаем класс SalaryEmployee (Сотрудник с фиксированной зарплатой), наследуемый от Employee
class SalaryEmployee(Employee):
    def __init__(self, nameEmployee, phone, bday, email, position, salary):
        super().__init__(nameEmployee, phone, bday, email, position)  # Вызываем конструктор родительского класса
        self.__salary = salary  # Фиксированная зарплата

    # Метод для расчета зарплаты сотрудника с фиксированной зарплатой
    def _calculateSalary(self):
        return self.__salary  # Возвращаем фиксированную зарплату
