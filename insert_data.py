import peewee
from models import Category, Product


def add_category(name):
    try:
        row = Category(name=name.lower().strip())
        row.save()
        print(f'Сохранили категорию {name.strip()}!')
    except (peewee.IntegrityError, peewee.InternalError): 
        print('Такая категория уже существует!')

# add_category('Платья')
# add_category('Джинсы')
# add_category('  Худи')
# add_category('Футболки  ')
# add_category('  Обувь  ')


def add_product(title, price, categoty_name):
    try:
        category = Category.select().where(Category.name==categoty_name.lower().strip()).get()
        category_exists = True
    except peewee.DoesNotExist:
        category_exists = False
    if category_exists:
        row = Product(
            title = title.lower().strip(),
            price = price,
            category = category
           )
        row.save()
        print(f'Сохранили товар {title.strip()}!')    
    else:
        print(f'Категории {categoty_name} не существует!')
    
# add_product('ZARA Платье Лен', 15000.50, 'Платья')
# add_product('DG Платье Атлас', 22000.00, 'Платья')
# add_product('Supreme 15 Лето', 70000.00, 'Футболки')
# add_product('Aygen Super', 10000, 'Джинсы')
# add_product('Lacoste NY', 100000.00, 'Худи')
# add_product('Nike Кеды Лето', 200000, 'Обувь')

