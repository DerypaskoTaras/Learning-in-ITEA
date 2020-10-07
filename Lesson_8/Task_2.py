import sqlite3


def change_student(old_ID, new_ID):
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE Students SET Student_ID=? WHERE Student_ID=?", (new_ID, old_ID))
        connection.commit()
    finally:
        connection.close()


def change_group(stud_id, Institute=None, Faculty=None, Group_name=None, Course=None):
    group_id = None
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Groups_ID FROM Students WHERE Student_ID=?", (stud_id,))
        for i in cursor:
            group_id = i[0]
        if Institute:
            cursor.execute("UPDATE Groups SET Institute=? WHERE ID=?", (Institute, group_id))
        if Faculty:
            cursor.execute("UPDATE Groups SET Faculty=? WHERE ID=?", (Faculty, group_id))
        if Group_name:
            cursor.execute("UPDATE Groups SET Group_name=? WHERE ID=?", (Group_name, group_id))
        if Course:
            cursor.execute("UPDATE Groups SET Course=? WHERE ID=?", (int(Course), group_id))
        connection.commit()
    finally:
        connection.close()


def change_student_evalution(old_eval, new_eval, stud_id):
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE Student_evalutions"
                       " SET Evalution=?"
                       " WHERE Student_link=? AND Evalution_ID=?", (new_eval, stud_id, old_eval))
        connection.commit()
    finally:
        connection.close()


def view_student_evalution(stud_id):
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Evalution, Evalution_ID FROM Student_evalutions WHERE Student_link=?", (stud_id,))
        for eval, id in cursor:
            print(f'Оценка №{id} - {eval}')
    finally:
        connection.close()


def view_all_students():
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Student_ID FROM Students")
        student_list = []
        for student in cursor:
            student_list.append(*student)
        evalutions_dict = dict()
        for student in student_list:
            cursor.execute("SELECT Evalution FROM Student_evalutions WHERE Student_link=?", (student,))
            temp_list = list()
            for evalution in cursor:
                temp_list.append(*evalution)
                evalutions_dict[student] = tuple(temp_list)
        cursor.execute("SELECT Student_ID, Institute, Faculty, Group_name, Course FROM Students"
                       " INNER JOIN Groups"
                       " ON Students.Groups_ID=Groups.ID")
        for student in cursor:
            print(f'Студент: {student[0]}\n'
                  f'Институт: {student[1]}\n'
                  f'Факультет: {student[2]}\n'
                  f'Группа: {student[3]}\n'
                  f'Курс: {student[4]}\n'
                  f'Оценки: {evalutions_dict[student[0]]}\n')
    finally:
        connection.close()


def add_group(institute, faculty, group, course):
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Groups ('Institute', 'Faculty', 'Group_name', 'Course')"
                       " VALUES (?, ?, ?, ?)", (institute, faculty, group, course))
        connection.commit()
        cursor.execute("SELECT ID FROM Groups ORDER BY ID DESC LIMIT 1")
        for ID in cursor:
            return ID[0]
    finally:
        connection.close()


def add_evalutions(stud_id, evalutions):
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        for eval in evalutions:
            cursor.execute("INSERT INTO Student_evalutions ('Student_link', 'Evalution')"
                           " VALUES (?, ?)", (stud_id, int(eval)))
            connection.commit()
    finally:
        connection.close()


def add_student(stud_id, group_link):
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Students ('Student_ID', 'Groups_ID') VALUES (?, ?)", (stud_id, group_link))
        connection.commit()
    finally:
        connection.close()


def view_excellent_students():
    student_id_list = list()
    excellent_student_dict = dict()
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT DISTINCT Student_link FROM Student_evalutions")
        for student in cursor:
            student_id_list.append(*student)
        for id in student_id_list:
            cursor.execute("SELECT AVG(Evalution) FROM Student_evalutions"
                           " WHERE Student_link=?", (id,))
            for avg_evalution in cursor:
                if avg_evalution[0] >= 10:
                    excellent_student_dict[id] = avg_evalution[0]
    finally:
        connection.close()
        if len(excellent_student_dict) == 0:
            print('Отличников в списке студентов нет !')
        else:
            for stud, eval in excellent_student_dict.items():
                print(f'Студент {stud} средний балл - {eval}')


def seach_student(stud_id):
    connection = sqlite3.connect('STUDENTS.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Evalution FROM Student_evalutions WHERE Student_link=?", (stud_id,))
        temp_list = list()
        for eval in cursor:
            temp_list.append(*eval)
        cursor.execute("SELECT Student_ID, Institute, Faculty, Group_name, Course FROM Students"
                       " INNER JOIN Groups"
                       " ON Student_ID=? AND Groups_ID=ID", (stud_id,))
        for info in cursor:
            print(f'Студент: {info[0]}\n'
                  f'Институт: {info[1]}\n'
                  f'Факультет: {info[2]}\n'
                  f'Группа: {info[3]}\n'
                  f'Курс: {info[4]}\n'
                  f'Оценки: {tuple(temp_list)}\n')
    finally:
        connection.close()


exit_point = True
while exit_point:
    print('Войти как админ? Введите - 1\nВойти как пользователь? Введите - 2')
    admin_or_user = input()
    if admin_or_user == '1':
        print('Вы успешно вошли в учетную запись администратора !\n')
        while True:
            print('Для просмотра всех студентов введите - "view"\n'
                  'Для добавления студента в базу введите - "add"\n'
                  'Для изменения записи студента введите - "change"\n'
                  'Для выхода введите - "exit"')
            admin_options = input()
            if admin_options == 'view':
                view_all_students()
            elif admin_options == 'add':
                student_id = int(input('ID студента - '))
                institute = input('Институт - ')
                faculty = input('Факультет - ')
                group = input('Группа - ')
                course = int(input('Курс - '))
                evalutions = list(input('Оценки - ').split())
                group_id = add_group(institute, faculty, group, course)
                add_student(student_id, group_id)
                add_evalutions(student_id, evalutions)
            elif admin_options == 'change':
                student_id = int(input('Введите ID студента запись которого хотите изменить. ID - '))
                print('Изменить ID студента ? введите "yes"')
                if input() == 'yes':
                    new_id = int(input('Введите новый ID-'))
                    change_student(student_id, new_id)
                print('Изменить Институт, группу и т.д. ? введите "yes"')
                if input() == 'yes':
                    institute = input('Институт - ')
                    faculty = input('Факультет - ')
                    group = input('Группа - ')
                    course = input('Курс - ')
                    change_group(student_id, institute, faculty, group, course)
                print('Изменить оценки студента ? Введите "yes"')
                if input() == 'yes':
                    view_student_evalution(student_id)
                    old_evalution = int(input('№ оценки, которую хотите изменить - '))
                    new_evaluyion = int(input('Введите оценку - '))
                    change_student_evalution(old_evalution, new_evaluyion, student_id)
            elif admin_options == 'exit':
                exit_point = False
                break
    elif admin_or_user == '2':
        print('Вы успешно вошли в учетную запись пользователя !\n')
        while True:
            print('Для просмотра списка отличников введите "view_ex"\n'
                  'Для просмотра всех студентов введите "view"\n'
                  'Для поиска студента введите "search"\n'
                  'Для просмотра информации о студенте введите "view_st"\n'
                  'Для выхода введите "exit"')
            user_options = input()
            if user_options == 'view_ex':
                view_excellent_students()
            if user_options == 'view':
                view_all_students()
            if user_options == 'search':
                stud_id = int(input('Введите ID студента - '))
                seach_student(stud_id)
            if user_options == 'exit':
                exit_point = False
                break
