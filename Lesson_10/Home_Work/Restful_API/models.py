import mongoengine as me

me.connect('RestAPIUsers')


class User(me.Document):
    first_name = me.StringField(min_length=1, max_length=128)
    last_name = me.StringField(min_length=1, max_length=128)