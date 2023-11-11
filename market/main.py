from data import Data, DB_FILE

data = DB_FILE


class ProductList:
    def __init__(self):
        self.list_products = []


    def insert_product(self, product):
            self.list_products.append(product)
            
    def listing_products(self):
        print()
        product = self.list_products
        return product
        print()
   

class Product:
    def __init__(self, name, value, amount):
        self.name = name
        self.value = value
        self.amount = amount
        

def insert_name():
    name_product = str(input('name:')) 
    return name_product
    
def insert_value():
    value_product= float(input('value:'))
    return value_product
    
def insert_amount():    
    quantity_amount = int(input('amount:'))
    return quantity_amount
 
product_list = ProductList()

for x in range(2):
    name = insert_name()
    value = insert_value()
    amount = insert_amount()
    
    product_insert = Product(name, value, amount)
    product_list.insert_product(vars(product_insert))
    
product_list.listing_products()

lista = product_list.listing_products()


data_base_connect = Data(data)
data_base_connect.add_product(lista)
data_base_connect.select_all_product()

