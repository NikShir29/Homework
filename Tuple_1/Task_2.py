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

def list_items():
    print("Список товаров:\n")
    for item in store_items:
        print(item)

def find_by_category(category):
    found_items = [key for key, value in store_items.items()
                    if category.lower() in value]
    if found_items:
        print("Список товаров с данной категорией: ")
        for item in found_items:
            print(item)
    else:
        print("Такой категории нет.")

def menu():
    while True:
        choice = int(input("""
Введите 1 для добавления товара
2 для вывода всех товаров
3 для поиска товаров по категории
4 для выхода: 
"""))
        if choice == 1:
            new_item = input("\nВведите название товара: ")
            new_item_category_list = input("Введите категории товара через запятую: ")
            new_item_category_list = new_item_category_list.split(",")
            new_item_category_list = ([s.strip() for s in new_item_category_list])
            new_item_category_list = ([h.lower() for h in new_item_category_list])
            store_items[new_item] = frozenset(new_item_category_list)
            print("\nТовар добавлен.")
        elif choice == 2:
            list_items()
        elif choice == 3:
            find_by_category(input("\nВведите категорию по которой вывести подходящие товары: "))
        elif choice == 4:
            break

menu()
