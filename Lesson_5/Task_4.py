import datetime
import shelve


class Users:
    FILE_NAME = 'users_list'
    temp_login = ''
    temp_password = ''

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def registration(self):
        with shelve.open(Users.FILE_NAME) as db:
            db[self.login] = (self.password, time_now())
            print('Регистрация прошла успешно.')


class Admin(Users):
    admin = {
        'Td': '1Qw'
    }

    def view_user_posts(self):
        with shelve.open(User.FILE_NAME) as up:
            if len(up) == 0:
                print('Нет ни одного поста.')
            else:
                for key in up:
                    print('Пользователь -', up[key][0], ':',
                          'Пост -', key, ':',
                          'Время публикации -', up[key][1])


    def view_all_users(self):
        with shelve.open(Users.FILE_NAME) as db:
            if len(db) == 0:
                print('Нет ни одного зарегистрированного пользователя.')
            else:
                for key, value in db.items():
                    print('Логин -', key, ':',
                          'Пароль -', value[0], ':',
                          'Время регистрации -', value[1])


class User(Users):
    FILE_NAME = 'users_posts'

    def create_post(self):
        with shelve.open(User.FILE_NAME) as up:
            new_post = input('Напишите свой пост\n')
            up[new_post] = (Users.temp_login, time_now())


def time_now():
    return datetime.datetime.now().strftime('%d.%m.%Y' + ' %H.%M.%S')


def password_is_valid():
    if any(map(lambda x: x.isdigit(), Users.temp_password)):
        if any(map(lambda x: x.islower(), Users.temp_password)):
            if any(map(lambda x: x.isupper(), Users.temp_password)):
                return True
            else:
                print('В вашем пароле нет букв в верхнем регистре.')
        else:
            print('В вашем пароле нет букв в нижнем регистре.')
    else:
        print('В вашем пароле нет цифр.')


def login_is_unique():
    with shelve.open(Users.FILE_NAME) as db:
        if Users.temp_login in Admin.admin or \
                Users.temp_login in db:
            print('Пользователь с таким логином уже существует.')
        else:
            return True


def log_into_account(k, v):
    with shelve.open(Users.FILE_NAME) as db:
        if k in db and db[k][0] == v:
            Users.temp_login = v
            Users.temp_login = k
            print('Вы успешно вошли в свою учетную запись')
            return True
        else:
            print('Пользователя с таким логином и/или паролем не существует.')


def is_admin(k, v):
    if k in Admin.admin and Admin.admin[k] == v:
        return True


def admin_options():
    print('Просмотреть всех зарегистрированных пользователей - введите "v_u"')
    print('Просмотреть все посты пользователей - введите "v_p"')
    print('Хотите выйти - введите "exit"')
    return input()


def user_options():
    print('Написать пост - введите "n_p"')
    print('Перелогиниться введите "relog"')
    print('Хотите выйти - "exit"')
    return input()


exit_point = True
while exit_point:
    print('Зарегистрироваться - введите "reg"')
    print('Войти в свою учетную запись - введите "log"')
    reg_or_log = input()
    if reg_or_log == 'log':
        set_login = input('Введите ваш логин - ')
        set_password = input('Введите ваш пароль - ')
        if is_admin(set_login, set_password):
            new_user = Admin(Users.temp_login, Users.temp_password)
            print('Вы вошли под учетной записью администратора')
            while True:
                admin_option = admin_options()
                if admin_option == 'v_u':
                    new_user.view_all_users()
                elif admin_option == 'v_p':
                    new_user.view_user_posts()
                elif admin_option == 'exit':
                    exit_point = False
                    break
        elif log_into_account(set_login, set_password):
            new_user = User(Users.temp_login, Users.temp_password)
            while True:
                user_option = user_options()
                if user_option == 'n_p':
                    new_user.create_post()
                elif user_option == 'exit':
                    exit_point = False
                    break
                elif user_option == 'relog':
                    break
    elif reg_or_log == 'reg':
        Users.temp_login = input('Введите ваш логин - ')
        if login_is_unique():
            Users.temp_password = input('Введите ваш пароль - ')
            if password_is_valid():
                repeat_password = input('Повторите пароль - ')
                if repeat_password != Users.temp_password:
                    print('Вы допустили ошибку.')
                else:
                    new_user = Users(Users.temp_login, Users.temp_password)
                    new_user.registration()
