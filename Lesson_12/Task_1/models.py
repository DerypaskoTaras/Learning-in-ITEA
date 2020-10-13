import mongoengine as me

me.connect('Telegram_users')


class Telegram_user(me.Document):
    first_name = me.StringField(min_length=2, max_length=16)
    last_name = me.StringField(min_length=2, max_length=16)
    patronymic = me.StringField(min_length=2, max_length=16)
    phone_number = me.IntField()
    email = me.EmailField()
    city = me.StringField(min_length=2, max_length=128)
    wish = me.ListField(me.StringField())
    state = me.IntField(default=0)

