class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self):
        print(f"{self.name} атакует!")

    def __str__(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Сила: {self.power}"


class Warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp + 20, power + 5)

    def attack(self):
        print(f"{self.name} наносит мощный удар мечом!")


class Mage(Character):
    def __init__(self, name, hp, power, mana):
        super().__init__(name, hp, power - 3)
        self.mana = mana

    def attack(self):
        print(f"{self.name} выпускает огненный шар!")

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Мана: {self.mana}"


def main():
    characters = []

    characters.append(Warrior("Арагорн", 100, 15))
    characters.append(Mage("Гендальф", 60, 12, 200))

    while True:
        print("СИСТЕМА ПЕРСОНАЖЕЙ ИГРЫ")
        print("1. Создать персонажа")
        print("2. Показать всех персонажей")
        print("3. Атака персонажем")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            print("\nСоздание персонажа:")
            print("1. Воин")
            print("2. Маг")
            type_choice = input("Выберите тип персонажа (1-2): ")

            name = input("Введите имя персонажа: ")

            try:
                hp = int(input("Введите здоровье: "))
                power = int(input("Введите силу: "))
            except ValueError:
                print("Нужно вводить числа.")
                continue

            if type_choice == "1":
                new_char = Warrior(name, hp, power)
                characters.append(new_char)
                print(f"Создан новый воин: {new_char.name}")
            elif type_choice == "2":
                try:
                    mana = int(input("Введите количество маны: "))
                except ValueError:
                    print("Мана должна быть числом.")
                    continue
                new_char = Mage(name, hp, power, mana)
                characters.append(new_char)
                print(f"Создан новый маг: {new_char.name}")
            else:
                print("Ошибка выбора типа персонажа.")

        elif choice == "2":
            print("\nСписок всех персонажей:")
            if len(characters) == 0:
                print("Персонажей нет.")
            else:
                for i, char in enumerate(characters, 1):
                    print(f"{i}. {char}")

        elif choice == "3":
            if len(characters) == 0:
                print("Нет персонажей для атаки.")
                continue

            print("\nВыберите персонажа для атаки:")
            for i, char in enumerate(characters, 1):
                print(f"{i}. {char.name}")

            try:
                char_index = int(input("Номер персонажа: ")) - 1
                if 0 <= char_index < len(characters):
                    characters[char_index].attack()
                else:
                    print("Неверный номер персонажа.")
            except ValueError:
                print("Нужно ввести число.")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Введите число от 1 до 4.")

main()