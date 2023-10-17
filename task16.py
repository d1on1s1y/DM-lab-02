products = (
    ["Яблука", 2.5, 10],
    ["Банани", 1.0, 15],
    ["Апельсини", 3.0, 8]
)
print()

def price_list(products):
    for i in products:
        print("Є ",i[0] ," у кількості ", i[2],". Вартість за штуку становить ",i[1])
        
price_list(products)

def purchase_product(products):
    product_name = str(input("Введіть назву товару: "))

    found_product = None
    for product in products:
        if product[0].lower() == product_name.lower():
            found_product = product
            break

    if found_product is None:
        print("Такого товару немає у списку")
        return -2
    desired_quantity = int(input("Введіть кількість товару: "))
    name, price, available_quantity = found_product

    if desired_quantity > available_quantity:
        print("В наявності немає потрібної кількості товару")
        return -1
    else:
        print("Вартість товару становить ",price * desired_quantity)
        
purchase_product(products)