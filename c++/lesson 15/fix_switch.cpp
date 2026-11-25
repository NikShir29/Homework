#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int code = 2; // Попробуйте поменять на 4

    switch (code) {
    case 1:
        std::cout << "Эспрессо" << std::endl;
        break;
    case 2:
        std::cout << "Латте" << std::endl;
        // Ошибка А: отсутствовал break, из-за чего печаталось "Какао"
        break; 
    case 3:
        std::cout << "Какао" << std::endl;
        break;
    // Ошибка Б: дублирование case 2 (исправлено на 4)
    case 4: 
        std::cout << "Мокко" << std::endl;
        break;
    }
    return 0;
}