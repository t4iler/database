from models import Category

category = Category.get(name="обувь")
print(list(category.products))   #В моделс есть related_name = 'products' оттуда и наш продукты