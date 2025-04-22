#Make a new 'gift' class from the existing 'product' class and override 'get_price' method to add wrapping charge of Rs. 100 in the price.
class product:
    deliveryCharge=50
    def __init__(self,nam="Teddy Bear", prc=500):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
    def __str__(self):
        return "The {} will cost you Rs.{}.".format(self.get_name(),self.get_price())

class gift(product):
    wrappingCharge=100
    def __init__(self, nam, prc):
        super().__init__(nam, prc)
    def get_price(self):
        return self.price + product.deliveryCharge + gift.wrappingCharge