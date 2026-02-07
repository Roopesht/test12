from cart_class import Cart
from free_delivery_cart_class import FDCart

amazon = Cart()
amazon.additem ("pencil",10,5)
amazon.displaycart()

amazon_f = FDCart()
amazon_f.additem ("corriander",10,2)
amazon_f.additem ("carrot",10,20)
amazon_f.displaycart()

print ('Grand Total: ', Cart.grand_total)