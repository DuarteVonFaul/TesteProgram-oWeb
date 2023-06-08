

class Buyer:

    def __init__(self, name) -> None:
        self.name = name
        self.product = []
        self.addtional = False
        self.valueAddtional = 0.0 
        self.price = 0.0
        pass

    def confirmAdditional(self):
        self.addtional = True
    
    def addProduct(self, product):
        self.product.append(product)
