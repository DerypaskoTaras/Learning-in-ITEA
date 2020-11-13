from Lesson_11.Home_Work.models.models import Category, Product

appliances = Category.objects.create(title='Бытовая техника')

large_home_appliances = Category.objects.create(title='Крупная бытовая техника')
appliances.add_subcategory(large_home_appliances)

refrigerator = Category.objects.create(title='Холодильники')
large_home_appliances.add_subcategory(refrigerator)

refrigerator1 = Product.objects.create(
    title='Холодильник с морозильной камерой LG DoorCooling+ GA-B509SLKM',
    price=14499,
    amount=10,
    category=refrigerator
)

refrigerator2 = Product.objects.create(
    title='Холодильник с морозильной камерой Bosch KGN39UL316',
    price=12999,
    amount=15,
    category=refrigerator
)

washing_machine = Category.objects.create(title='Стиральные машины')
large_home_appliances.add_subcategory(washing_machine)

washing_machine1 = Product.objects.create(
        title='Стиральная машина автоматическая Beko WUE7636XCW',
        price=7677,
        amount=28,
        category=washing_machine
)

air_conditioning_equipment = Category.objects.create(title='Климатическая техника')
appliances.add_subcategory(air_conditioning_equipment)

heater = Category.objects.create(title='Обогреватели')
air_conditioning_equipment.add_subcategory(heater)

heater1 = Product.objects.create(
    title='Обогреватель Xiaomi SmartMi Electric Heater Smart Edition White (DNQZNB03ZM)',
    price=2800,
    amount=5,
    category=heater
)

conditioner = Category.objects.create(title='Кондиционеры')
air_conditioning_equipment.add_subcategory(conditioner)


home_appliances = Category.objects.create(title='Техника для дома')
appliances.add_subcategory(home_appliances)

vacuum_cleaner = Category.objects.create(title='Пылесосы')
home_appliances.add_subcategory(vacuum_cleaner)

vacuum_cleaner1 = Product.objects.create(
    title='Вертикальный+ручной пылесос (2в1) Rowenta RH9490WO',
    price=11159,
    amount=12,
    category=vacuum_cleaner
)

smoothing_iron = Category.objects.create(title='Утюги')
home_appliances.add_subcategory(smoothing_iron)

smoothing_iron1 = Product.objects.create(
    title='Утюг с паром Bosch TDA3026110',
    price=1099,
    amount=1,
    category=smoothing_iron
)

housing = Category.objects.create(title='Все для дома')

furniture = Category.objects.create(title='Мебель')
housing.add_subcategory(furniture)

bed = Category.objects.create(title='Кровати')
furniture.add_subcategory(bed)

bed1 = Product.objects.create(
    title='Односпальная кровать ОЛИМП Лика Стандарт с изножьем без ящиков',
    price=2792,
    amount=2,
    category=bed
)

dishes = Category.objects.create(title='Посуда')
housing.add_subcategory(dishes)

saucepans = Category.objects.create(title='Кастрюли')
dishes.add_subcategory(saucepans)

saucepan1 = Product.objects.create(
    title='Кастрюля Krauff 26-238-009',
    price=368,
    amount=4,
    category=saucepans
)

knifes = Category.objects.create(title='Ножи')
dishes.add_subcategory(knifes)

