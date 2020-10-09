import mongoengine as me
import DB_generator as gen
from random import choice

me.connect('Students')


class Curator(me.Document):
    first_name = me.StringField(min_length=1, max_length=256)
    last_name = me.StringField(min_length=1, max_length=256)


class Group(me.Document):
    institute = me.StringField(min_length=1, max_length=256, required=True)
    faculty = me.StringField(min_length=1, max_length=256, required=True)
    group = me.StringField(min_length=1, max_length=256, required=True)
    course = me.IntField(min_value=1, max_value=6, required=True)


class Student(me.Document):
    first_name = me.StringField(min_length=1, max_length=256, required=True)
    last_name = me.StringField(min_length=1, max_length=256, required=True)
    evalutions = me.ListField(me.IntField())
    group = me.ReferenceField(Group)
    curator = me.ReferenceField(Curator)


if __name__ == "__main__":
    curators = gen.get_curators_names()
    students = gen.get_students_names()
    groups = gen.get_institutes_list()
    groups_id = list()
    curators_id = list()

    for curator in curators:
        new_curator = Curator(first_name=curator[0], last_name=curator[1])
        new_curator.save()
        curators_id.append(new_curator.id)

    for group in groups:
        new_group = Group(institute=group[0], faculty=group[1], group=group[2], course=group[3])
        new_group.save()
        groups_id.append(new_group.id)

    for student in students:
        students_evalutions = gen.get_evalutions()
        new_student = Student(first_name=student[0], last_name=student[1],
                              evalutions=students_evalutions, group=choice(groups_id),
                              curator=choice(curators_id))
        new_student.save()
