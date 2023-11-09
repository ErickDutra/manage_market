from data import addProduct, selectAllProduct, selectForId, dellAllTable, create_table

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
        
def insertName():
    name_product = str(input('name:')) 
    return name_product
    
def insertValue():
    value_product= float(input('value:'))
    return value_product
    
def insertAmount():    
    quantityAmount = int(input('amount:'))
    return quantityAmount
    
name = insertName()
value = insertValue()
amount = insertAmount()

productInputed = Product(name, value, amount)
productList = vars(productInputed)

#selectAllProduct()
#addProduct(productList)

