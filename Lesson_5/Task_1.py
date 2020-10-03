from threading import Thread
import time


def repeat_func(name_tread, is_daemon):
    def actual_decorator(func):
        def wrapper():
            new_thread = Thread(name=name_tread, target=func, daemon=is_daemon)
            new_thread.start()

        return wrapper

    return actual_decorator


@repeat_func('12345', False)
def sum_iter():
    time.sleep(5)
    res = 0
    for i in range(1, 1000001):
        res += i


sum_iter()
