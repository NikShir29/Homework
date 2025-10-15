products = [
    ["Хлеб", 1.2, 10],
    ["Молоко", 2.5, 5],  # Название, цена, количество
    ["Сыр", 5.0, 3],
    ["Шоколад", 3.0, 7],
]

def goods_list():
    for product, price, quantity in products:
        print(f"Название: {product}, Цена: {price}, Количество: {quantity}")

def start():
    bonus_text = ""
    shopping_cart = []
    price_all = 0
    while True:
        goods_list()
        choice_product = input("Введите название товара, либо введите Стоп, чтобы завершить покупки: ")
        if choice_product == "Стоп":
            break
        choice_quantity = int(input("Введите количество товара: "))
        for product in products:
            if choice_product == product[0]:
                if product[2] >= choice_quantity:
                    product[2] -= choice_quantity
                    price_all += product[1] * choice_quantity
                    shopping_cart.append(choice_product)
                else:
                    print("Недостаточно товара на складе.")
        if len(shopping_cart) > 3:
            for product in products:
                if product[0] == "Хлеб" and product[2] > 0:
                    shopping_cart.append("Хлеб (бесплатно)")
                    bonus_text += "Вы получили хлеб бесплатно."
        print(f"Товары в корзине: {shopping_cart}, Цена товаров в корзине: {price_all}")
    if price_all > 20:
        discount = price_all * 0.1
        price_all -= discount
        bonus_text += "\nПрименена скидка 10%."
    if bonus_text:
        print(bonus_text)
    print(f"К оплате: {price_all}$")

start()
