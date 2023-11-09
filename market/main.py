from data import Data, DB_FILE

data = DB_FILE


class Product:
    def __init__(self, name, value, amount):
        self.name = name
        self.value = value
        self.amount = amount
        
        
    def organized(self):
        product = [
             self.name,
             self.value,
             self.amount
        ]
        return product
        
def insert_name():
    name_product = str(input('name:')) 
    return name_product
    
def insert_value():
    value_product= float(input('value:'))
    return value_product
    
def insert_amount():    
    quantity_amount = int(input('amount:'))
    return quantity_amount
    
name = insert_name()
value = insert_value()
amount = insert_amount()

product_inputed = Product(name, value, amount)
product_list = product_inputed.organized()


data_base_connect = Data(data)
data_base_connect.select_all_product()

#dataBaseConnect.addProduct(productList)

