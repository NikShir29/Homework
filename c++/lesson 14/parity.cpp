#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    int num;
    std::cout << "Введите целое число: ";
    std::cin >> num;

    // Тернарный оператор обязательно в скобках
    std::cout << num << " — " << (num % 2 == 0 ? "чётное" : "нечётное") << std::endl;

    return 0;
}