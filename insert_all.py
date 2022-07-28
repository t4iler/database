from insert_data import add_category, add_product
from models import Category, Product
from random import randint

'''добавляем категорию машины'''

# add_category('   МАШИНЫ   ')

# with open('cars.txt', 'r') as file:
#     list_ = file.readlines()
#     # print(list_)
#     for i in list_:
#         car = i.replace('\n', '')
#         add_product(car, 1, 'машины')


'''для просмотра всех машин'''
category = Category.get(name='машины')

for i in category.products:
    print(i.title)


'''Добавляем категорию телефоны'''
add_category('телефоны')

with open('telefon.txt', 'r') as file:
    list_ = file.readlines()

    for i in list_:
        tel = i.replace('\n', '')
        price = randint(10000, 100000)
        add_product(tel, price, 'телефоны')