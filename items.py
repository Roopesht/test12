from cart import display_cart
from cart import items, total, calculate_total
import cart
def add_item(name, price, qty):
    items.append ({"name": name, "price": price, "qty": qty})
    total = calculate_total(items)




add_item("paper", 1, 20)
display_cart()
