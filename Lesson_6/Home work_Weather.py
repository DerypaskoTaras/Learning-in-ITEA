from bs4 import BeautifulSoup
import requests
from datetime import date

date_now = date.today()


def get_my_city():
    URL = 'https://prozavr.ru/tools/uznat_ip_adres.php'
    page = requests.get(URL)
    if page.status_code == 200:
        content = page.content
        soup = BeautifulSoup(content, 'html.parser')
        my_city = soup.findAll('abbr')[2].text.lower()
        return my_city
    else:
        print('Не удалось установить ваше местоположение.')


def get_weather(city, day, month, year):
    date_ = date(year, month, day)
    URL = f'https://sinoptik.ua/погода-{city}/{date_}'
    page = requests.get(URL)
    if page.status_code == 200:
        content = page.content
        soup = BeautifulSoup(content, 'html.parser')
        weather = soup.findAll('div', class_='main')
        for block in weather:
            if int(block.find('p', class_='date').text) == day:
                rain_or_clear = block.find('div')['title']
                temp_min = block.find('div', class_='min').text
                temp_max = block.find('div', class_='max').text
                return f'{rain_or_clear}\n' \
                       f'Температура {temp_min}\n' \
                       f'Температура {temp_max}'


if get_my_city():
    print(f'Погода в вашем городе (г.{get_my_city().capitalize()})'
          f' на {date_now.day}.{date_now.month}.{date_now.year}')
    print(get_weather(get_my_city(), date_now.day, date_now.month, date_now.year))
while True:
    user_option = input('Желаете узнать погоду в другом городе ? Да - введите "yes", нет - введите "no"\n')
    if user_option == 'yes':
        user_city = input('Введите город - ')
        try:
            user_day = int(input('DD - '))
            user_month = int(input('MM - '))
            user_year = int(input('YYYY - '))
        except ValueError:
            print('Вы не корректно ввели дату !')
        else:
            if get_weather(user_city, user_day, user_month, user_year):
                print(f'Погода в городе {user_city.capitalize()} на {user_day}.{user_month}.{user_year}')
                print(get_weather(user_city, user_day, user_month, user_year))
            else:
                print('Нет данных о погоде.')
    elif user_option == 'no':
        break
    else:
        print('Введите "yes" или "no".')