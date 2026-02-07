class Cart:
    grand_total = 0

    def __init__(self):
        self.items = []
        self.total = 0
        self.delivery_charge = 0
    
    def calc_total (self):
        _total = 0
        for item in self.items:
            _total = _total + item['qty'] * item['price']
        self.total = _total

    def additem(self, item, price, qty):
        it = {"name": item, "price": price, "qty": qty}
        self.items.append(it)
        self.delivery_charge += 1
        self.calc_total()
        Cart.grand_total += it ['price'] * it['qty']
    
    # def get_all_cart_total():
    def displaycart(self):
        print ("items: ", self.items)
        print ("total: ", self.total)
        print ("Delivery charge: ", self.delivery_charge)

    

# Usage
