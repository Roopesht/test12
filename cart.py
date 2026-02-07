items = [] # list of items (item is a dictionary)
# Ex. [{"name": "pen", "price": 10, "qty": 2}, {"name": "book", "price": 70, "qty": 10}]
total = 0
def calculate_total(items):
    """
    This function calculate the total (price * qty for al the items) of the cart.
    """
    _total = 0
    for item in items:
        _total = _total + item['qty'] * item['price']
    global total
    total = _total
    return _total

def display_cart ():
    print ("Items: ", items)
    print ("total: ", total)

"""
def _test_cart ():
    items = [{"name": "pen", "price": 10, "qty": 2}, {"name": "book", "price": 70, "qty": 10}]
    total = calculate_total(items)
    print ("total: ", total)


if __name__ == '__main__':
    _test_cart ()

"""
