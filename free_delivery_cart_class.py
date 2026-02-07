from cart_class import Cart
class FDCart (Cart):
    pass
    def calc_total (self):
        super().calc_total()
        print ("Calc total of FD Cart is called")

