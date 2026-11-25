#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    char cmd; std::cin >> cmd;

    switch (cmd) {
    case 'w': std::cout << "Вперёд" << std::endl; break;
    case 'a': std::cout << "Влево" << std::endl; break;
    case 's': std::cout << "Назад" << std::endl; break;
    case 'd': std::cout << "Вправо" << std::endl; break;
    case 'q':
    case 'x': std::cout << "Выход из программы" << std::endl; break;
    default: std::cout << "Неизвестная команда" << std::endl;
    }
    return 0;
}