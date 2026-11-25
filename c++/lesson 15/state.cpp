#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int t; std::cin >> t;

    if (t <= 0) {
        std::cout << "Состояние: лёд" << std::endl;
        if (t == 0) std::cout << "Точка замерзания" << std::endl;
    }
    else if (t < 100) {
        std::cout << "Состояние: вода" << std::endl;
    }
    else {
        std::cout << "Состояние: пар" << std::endl;
        if (t == 100) std::cout << "Точка кипения" << std::endl;
    }

    std::cout << (t >= 20 && t <= 25 ? "комфортно" : "некомфортно") << std::endl;
    return 0;
}