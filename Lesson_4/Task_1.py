from abc import abstractmethod, ABC
import time
from datetime import date


class Person(ABC):

    def __init__(self, date_of_birth):
        self.date_of_birth = time.strptime(date_of_birth, '%d.%m.%Y')
        self.age = self.age()

    def age(self):
        today = date.today()
        temp_year = today.year - self.date_of_birth.tm_year
        age_person = temp_year - ((today.month, today.day) < (self.date_of_birth.tm_mon, self.date_of_birth.tm_mday))
        return age_person

    @abstractmethod
    def information(self):
        return f'Возраст - {self.age}'


class Applicant(Person):

    def __init__(self, surname, date_of_birth, faculty):
        super().__init__(date_of_birth)
        self.date_of_birth = date_of_birth
        self.surname = surname
        self.faculty = faculty

    def information(self):
        return f'Фамилия - {self.surname}\n' \
               f'Дата рождения - {self.date_of_birth}\n' \
               f'Факультет - {self.faculty}\n'


class Student(Person):

    def __init__(self, surname, date_of_birth, faculty, course):
        super().__init__(date_of_birth)
        self.date_of_birth = date_of_birth
        self.surname = surname
        self.faculty = faculty
        self.course = course

    def information(self):
        return f'Фамилия - {self.surname}\n' \
               f'Дата рождения - {self.date_of_birth}\n' \
               f'Факультет - {self.faculty}\n' \
               f'Курс - {self.course}\n'


class Lecturer(Person):

    def __init__(self, surname, date_of_birth, faculty, function, work_experience):
        super().__init__(date_of_birth)
        self.date_of_birth = date_of_birth
        self.surname = surname
        self.faculty = faculty
        self.function = function
        self.work_experience = work_experience

    def information(self):
        return f'Фамилия - {self.surname}\n' \
               f'Дата рождения - {self.date_of_birth}\n' \
               f'Факультет - {self.faculty}\n' \
               f'Должность - {self.function}\n' \
               f'Стаж работы - {self.work_experience}\n'


def user_options():
    print('Вывести список персон ? Введите "1"')
    print('Задать диапазон поиска по возрасту ? Введите "2"')
    print('Выйти ? Введите "3"')
    return input()


persons = (
    Student('Иванов', '23.09.1984', 'Информатика', 4),
    Applicant('Петров', '28.02.1974', 'Физика'),
    Lecturer('Фролов', '01.10.1971', 'Биология, экология', 'Доцент', '10 лет'),
    Student('Сидоров', '23.09.2001', 'История', 4),
    Applicant('Никитин', '28.02.1998', 'Астрономия'),
    Lecturer('Ставницкий', '01.10.1965', 'Экономика', 'Профессор', '18 лет'),
    Student('Кротов', '23.09.1976', 'Менеджмент, маркетинг', 4),
    Applicant('Шевченко', '28.02.1979', 'Культура, искусство'),
    Lecturer('Фролов', '01.10.1971', 'Право', 'Заведующий кафедрой', '20 лет'),
)

while True:
    option = user_options()
    if option == '1':
        for person in persons:
            print(person.information())
    elif option == '2':
        start = int(input('От - '))
        stop = int(input('До - '))
        for person in persons:
            if start <= person.age <= stop:
                print(f'{person.information()}Возраст - {person.age}\n')
    elif option == '3':
        break
