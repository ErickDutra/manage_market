from data import Data, DB_FILE
from dataclasses import dataclass, asdict

data = DB_FILE

@dataclass
class ProductList:
    list_products : list


    def insert_product(self, product):
            self.list_products.append(product)
            
    def listing_products(self,):
        print()
        product = self.list_products
        return product
  
   
@dataclass
class Product:
    name : str
    value : float
    amount : int
        

def insert_name():
    name_product = str(input('name:')) 
    return name_product
    
def insert_value():
    value_product= float(input('value:'))
    return value_product
    
def insert_amount():    
    quantity_amount = int(input('amount:'))
    return quantity_amount
 
 
products = []
product_list = ProductList(products)

name = insert_name()
value = insert_value()
amount = insert_amount()

product_insert = Product(name, value, amount)
product_insert = asdict(product_insert)


product_list.insert_product(product_insert)
print(product_list.listing_products())
data_base_connect = Data(data)
data_base_connect.add_product(product_list.listing_products())
data_base_connect.select_all_product()

