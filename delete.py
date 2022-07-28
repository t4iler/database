from models import Product

'''Удаляем один продукт'''
# product1 = Product.get(product_id=1)
# product1.delete_instance()

# product1 = Product.get(product_id=1)
# print(product1)     #Выведет ошибку, поскольку нет такого продукта

'''Удаляем все продукты id которых больше 4'''
products_to_delete = Product.delete().where(Product.product_id > 7)
products_to_delete.execute()

# print(list(Product.select()))