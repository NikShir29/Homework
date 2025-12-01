products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80), ("Груши", 20, 70), ("Апельсины", 30, 60)],
    "Овощи": [("Морковь", 20, 30), ("Капуста", 40, 60), ("Лук", 30, 50), ("Томаты", 60, 80)],
    "Напитки": [("Вода", 20, 30), ("Сок", 40, 60), ("Чай", 60, 80)],
    "Молочка": [("Молоко", 30, 50), ("Сыр", 40, 80), ("Йогурт", 30, 60)],
    "Сладости": [("Конфеты", 60, 100), ("Зефир", 40, 60), ("Шоколад", 30, 140)]
}
most_expensive_item = None
most_expensive_item_price = 0
most_items_product = None
most_items_count = 0
all_products_price = 0

for product in products:
    print(f"\n{product}:")
    for item in products[product]:
        print(f"{item[0]} — {item[1]}шт., по {item[2]} руб.")
        if item[2] > most_expensive_item_price:
            most_expensive_item = item[0]
            most_expensive_item_price = item[2]
        all_products_price += item[1] * item[2]
    if sum(item[1] for item in products[product]) > most_items_count:
        most_items_count = sum(item[1] for item in products[product])
        most_items_product = product

print(f"\nВ магазине товаров на сумму: {all_products_price} руб.")
print(f"Больше всего товаров в категории: {most_items_product}, количество: {most_items_count}шт.")
print(f"Самый дорогой продукт: {most_expensive_item} ({most_expensive_item_price} руб.)")
