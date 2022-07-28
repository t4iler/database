import peewee

from main import db
from datetime import datetime


class BaseModel(peewee.Model):
    create_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db

class Category(BaseModel):
    category_id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=100, unique=True)
    
    class Meta: 
        db_table = 'categories'
        order_by = ('created_at',)

class Product(BaseModel):
    product_id = peewee.PrimaryKeyField(null=False)
    title = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=None)
    category = peewee.ForeignKeyField(Category, related_name='products', to_field='category_id', on_delete='cascade')

    class Meta:
        db_table = 'products'
        order_by = ('created_at',)
    

db.connect()
# Category.create_table()
# Product.create_table()
