player_spells = []
new_spells = ["Снежная буря", "Огненный шар", "Превращение"]

print("Ваша книга заклинаний пуста.")

player_choice = int(input("""\nВведите 1 для изучения нового заклинания
2 для показа книги заклинаний
3 для тренировки (выбрать заклинание и повторить его три раза)
4 для применения заклинания
5 для выхода: """))

if player_choice == 1:
    while True:
        spell_choice = (input("""\nВыберите, какое заклинание изучить.
Введите 8 для выхода.
Доступные заклинания:
"Снежная буря"
"Огненный шар"
"Превращение": """))
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