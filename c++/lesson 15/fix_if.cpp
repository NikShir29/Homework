#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int age = 15; // Попробуйте поменять на 20

    // Ошибка А: было age => 18 (синтаксическая, исправлено на >=)
    if (age >= 18) {
        std::cout << "Вход разрешён" << std::endl;
    }
    // Ошибка Б: отсутствовали фигурные скобки, из-за чего вторая строка 
    // выполнялась всегда (логическая).
    else {
        std::cout << "Вход запрещён" << std::endl;
        std::cout << "Приходите в 18+" << std::endl;
    }
    return 0;
}