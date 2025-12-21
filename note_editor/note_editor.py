import os

def load_notes():
    if not os.path.exists("notes.txt"):
        return []
    with open("notes.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()

def save_notes(notes):
    with open("notes.txt", "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

def add_note():
    category = input("Введите категорию заметки: ")
    text = input("Введите текст заметки: ")
    notes = load_notes()
    notes.append(f"{category} | {text}")
    save_notes(notes)
    print("Заметка добавлена.")

def show_notes():
    notes = load_notes()
    if not notes:
        print("Заметок пока нет.")
        return
    print("\nСписок заметок:")
    for note in notes:
        print(f"{note}")

def find_by_category(category):
    notes = load_notes()
    found_notes = []
    for note in notes:
        parts = note.split(" | ", 1)
        if len(parts) == 2 and parts[0].strip().lower() == category.lower():
            found_notes.append(note)
    return found_notes

def search_by_category_menu():
    category = input("Введите категорию для поиска: ")
    found_notes = find_by_category(category)
    if not found_notes:
        print(f"Заметок с категорией '{category}' не найдено.")
    else:
        print(f"\nНайдено {len(found_notes)} заметок с категорией '{category}':")
        for note in found_notes:
            print(f"{note}")

def search_word(word):
    notes = load_notes()
    found_notes = []
    word_lower = word.lower()
    for note in notes:
        if word_lower in note.lower():
            found_notes.append(note)
    return found_notes

def search_by_word_menu():
    word = input("Введите слово для поиска: ")
    found_notes = search_word(word)
    if not found_notes:
        print(f"Заметок со словом '{word}' не найдено.")
    else:
        print(f"\nНайдено {len(found_notes)} заметок со словом '{word}':")
        for note in found_notes:
            print(f"{note}")

def main():
    while True:
        print("\nМЕНЮ")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Поиск по категории")
        print("4. Поиск по слову")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            show_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            search_by_category_menu()
        elif choice == "4":
            search_by_word_menu()
        elif choice == "5":
            print("До свидания.")
            break
        else:
            print("Неверный выбор.")

main()