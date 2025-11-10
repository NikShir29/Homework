player_spells = []
new_spells = ["Снежная буря", "Огненный шар", "Превращение"]

print("Ваша книга заклинаний пуста.")

def player_menu():
    player_choice = int(input("""\nВведите 1 для изучения нового заклинания
2 для показа книги заклинаний
3 для тренировки (выбрать заклинание и повторить его три раза)
4 для применения заклинания
5 для выхода: """))
    return player_choice

while True:
    choice = player_menu()
    if choice == 1:
        while True:
            print("Доступные заклинания: ", new_spells)
            spell_choice = (input("""\nВыберите, какое заклинание изучить.
Введите 8 для выхода: """))
            if spell_choice in new_spells and spell_choice in player_spells:
                print("Такое заклинание уже есть в книге!")
                print("Ваши заклинания: ", player_spells)
            elif spell_choice in new_spells and spell_choice not in player_spells:
                player_spells.append(spell_choice)
                print("Ваши заклинания: ", player_spells)
            elif spell_choice == "8":
                break
            else:
                print("Такого заклинания не существует!")
                print("Ваши заклинания: ", player_spells)
    elif choice == 2:
        print("Ваши заклинания: ", player_spells)
    elif choice == 3:
        print("Ваши заклинания: ", player_spells)
        spell_training = input("Выберите, какое заклинание тренировать: ")
        if spell_training not in player_spells:
            print("Вы не знаете такого заклинания!")
        else:
            print("Вы тренируете:", spell_training)
            print(spell_training, spell_training, spell_training)
    elif choice == 4:
        print("Ваши заклинания: ", player_spells)
        spell_cast = input("Выберите, какое заклинание произнести: ")
        if spell_cast not in player_spells:
            print("У вас нет такого заклинания!")
        else:
            print("Вы применили заклинание:", spell_cast)
    elif choice == 5:
        break
