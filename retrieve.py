# import peewee
from models import Category, Product

def find_all_categories():
    return Category.select()

def find_all_products():
    return Product.select()

categories = find_all_categories()
products = find_all_products()

# # print(categories)
# print('Категории в бд:')
# for i in categories:
#     # print(i)
#     print(i.name) 

# # ==============================================================

try:
    choice = int(input('Введите категорию(1-платья, 2-джинсы, 3-футболки, 4-худи, 5-обувь): '))
    for i in products:
        if i.category == categories[choice-1]:
            print(f'Title: {i.title}, Price: {i.price}, Category: {i.category}')
except:
    print('Вы ввели некоректный input()')
