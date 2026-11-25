#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int level = 2; bool premium = true;

    std::cout << (premium || level >= 3) << std::endl; // 1 (true || false)
    std::cout << (!premium && level > 5) << std::endl; // 0 (false && false)

    if (level >= 3) { std::cout << "верхний ярус" << std::endl; }
    else if (level >= 1) { std::cout << "нижний ярус" << std::endl; }

    switch (level) {
    case 1: std::cout << "один" << std::endl; break;
    case 2:
        std::cout << "два" << std::endl;
        break; // ДОБАВЛЕН BREAK: без него выполнение провалится в case 3
    case 3:
        std::cout << "три" << std::endl;
        break;
    default: std::cout << "другое" << std::endl;
    }

    std::cout << (level >= 2 ? "доступ открыт" : "доступ закрыт") << std::endl;
    return 0;
}