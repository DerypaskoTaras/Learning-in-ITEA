from random import choice, randint
import json


def get_institutes_list():
    temp_institutes_list = list()
    result_institutes_list = list()
    with open("Institutes.json", "r") as handle:
        data = json.load(handle)
        for institute in data:
            temp_institutes_list.append([institute, data[institute]])
    while len(result_institutes_list) < 100:
        random_index = randint(0, len(temp_institutes_list) - 1)
        result_institutes_list.append(
            [temp_institutes_list[random_index][0], choice(temp_institutes_list[random_index][1]).capitalize()]
        )
    for inst_list in result_institutes_list:
        group = ''
        for word in inst_list[1].split():
            if word not in ['Факультет', 'факультет', '-', 'и', 'на']:
                group += "".join(word[0].upper())
        inst_list.append(group)
        inst_list.append(randint(1, 5))
    return result_institutes_list


def get_students_names():
    students_names = list()
    with open("students_name.json", "r") as handle:
        data = json.load(handle)
        for name in data:
            students_names.append([data[name], name])
    return students_names


def get_curators_names():
    curators_names = list()
    with open("curators_name.json", "r") as handle:
        data = json.load(handle)
        for name in data:
            curators_names.append([data[name], name])
    return curators_names


def get_evalutions():
    evalutions_list = list()
    while True:
        i = randint(1, 10)
        for j in range(i):
            evalutions_list.append(randint(1, 12))
        break
    return evalutions_list


def get_random_curator():
    random_curator = choice(get_curators_names())
    return random_curator
