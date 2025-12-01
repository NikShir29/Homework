store_items = {
    "Смартфон будущего": frozenset({"техника", "электроника", "редкое", "инновации"}),
    "Квантовый ноутбук": frozenset({"техника", "электроника", "редкое", "инновации", "бытовое"}),
    "Викторианский компас": frozenset({"редкое", "антиквариат", "путешествия"}),
    "Свиток древнего заклинания": frozenset({"редкое", "мистика", "коллекционное"}),
    "Умная кофемашина": frozenset({"бытовое", "техника", "электроника"}),
    "Кристаллическая ваза": frozenset({"бытовое", "декор", "редкое"}),
    "Беспроводная зарядка": frozenset({"электроника", "техника", "бытовое"}),
    "Голографический проектор": frozenset({"электроника", "редкое", "инновации"}),
    "Окаменелость трилобита": frozenset({"редкое", "коллекционное", "научное"}),
    "Эликсир молодости": frozenset({"редкое", "мистика", "здоровье"}),
    "Механический паук": frozenset({"техника", "редкое", "инновации", "игрушка"}),
}

for item in store_items:
    print(item)

def menu():
    while True:
        choice = int(input("""
Введите 1 для добавления товара
2 для вывода всех товаров
3 для поиска товаров по категории
4 для выхода: """))
        if choice == 1:
            new_item = input("Введите название товара: ")
            new_item_category_list = input("Введите категории товара через запятую: ")
            new_item_category_list = new_item_category_list.split(",")
            new_item_category_list = [s.strip() for s in new_item_category_list]
            new_item_category_list = [h.lower() for h in new_item_category_list]
            store_items[new_item] = frozenset(new_item_category_list)
            print(new_item)
            print(new_item_category_list)
            print(store_items)

menu()
