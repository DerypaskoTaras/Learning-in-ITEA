import mongoengine as me

me.connect('Internet_Shop')


class Product(me.Document):
    title = me.StringField(required=True)
    price = me.FloatField(required=True)
    is_available = me.BooleanField(default=True)
    amount = me.FloatField()
    views = me.IntField(default=0)
    category = me.ReferenceField('Category')

    def increase_views(self):
        self.views += 1
        self.save()


class Category(me.Document):
    title = me.StringField(required=True)
    description = me.StringField()
    parent = me.ReferenceField('self')
    subcategories = me.ListField(me.ReferenceField('self'))

    @classmethod
    def get_root_categories(cls):
        return cls.objects(parent=None)

    def add_subcategory(self, subcategory: 'Category'):
        subcategory.parent = self
        self.subcategories.append(subcategory)
        subcategory.save()
        self.save()
