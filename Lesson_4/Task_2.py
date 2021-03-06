import datetime


class Users:
    temp_login = ''
    temp_password = ''
    users_list = dict()

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def registration(self):
        Users.users_list[self.login] = (self.password, time_now())
        print('Регистрация прошла успешно.')


class Admin(Users):
    admin = {
        'Td': '1Qw'
    }

    def view_user_posts(self):
        if len(User.users_posts) == 0:
            print('Нет ни одного поста.')
        else:
            for key in User.users_posts:
                print('Пользователь -', User.users_posts[key][0], ':',
                      'Пост -', key, ':',
                      'Время публикации -', User.users_posts[key][1])

    def view_all_users(self):
        if len(Users.users_list) == 0:
            print('Нет ни одного зарегистрированного пользователя.')
        else:
            for key, value in Users.users_list.items():
                print('Логин -', key, ':',
                      'Пароль -', value[0], ':',
                      'Время регистрации -', value[1])


class User(Users):
    users_posts = dict()

    def create_post(self):
        new_post = input('Напишите свой пост\n')
        User.users_posts[new_post] = (Users.temp_login, time_now())


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
    if Users.temp_login in Admin.admin or \
            Users.temp_login in Users.users_list:
        print('Пользователь с таким логином уже существует.')
    else:
        return True


def log_into_account(k, v):
    if k in Users.users_list and Users.users_list[k][0] == v:
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
