import time


def repeat_func(rep):

    def actual_decorator(func):

        def wrapper():
            total_time = 0
            result = 0
            i = 1
            while i <= rep:
                time_start_func = time.time()
                result = func()
                time_end_func = time.time()
                time_work_func = time_end_func - time_start_func
                total_time += time_work_func
                print(i, '- й вызов функции', time_work_func)
                i += 1
            return print('Имя декорируемой функции -', func.__name__,
                         '\nРезультат декорируемой функции -', result,
                         '\nОбщее время всех вызовов функции -', total_time)

        return wrapper

    return actual_decorator


@repeat_func(5)
def sum_iter():
    res = 0
    for i in range(1, 10000001):
        res += i
    return res


sum_iter()
