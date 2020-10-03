import requests
from threading import Thread

url_list = (
    'https://klike.net/uploads/posts/2018-07/1531483091_1.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795460_1.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795464_3.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795495_4.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795425_5.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795476_6.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795503_8.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795482_9.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795505_10.jpg',
    'https://klike.net/uploads/posts/2019-07/1563795484_11.jpg'
)


def download_all_images(urls):

    def actual_decorator(func):

        def wrapper():
            for id_file, url_file in enumerate(urls, 1):
                name_file = f'image{id_file}.jpg'
                thread_name = f'Thread{id_file}'
                thread = Thread(name=thread_name, target=func, args=(name_file, url_file))
                print(f'{thread_name} начал скачивание файла {name_file} по ссылке:\n {url_file}\n')
                thread.start()
        return wrapper

    return actual_decorator


@download_all_images(url_list)
def download_image(name, url):
    with open(name, "wb") as f:
        file_req = requests.get(url)
        f.write(file_req.content)
        print(f'Загрузка {name} успешно завершена')


download_image()
