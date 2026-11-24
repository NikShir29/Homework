#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    int a, b;
    std::cout << "Числа a и b: ";
    std::cin >> a >> b;

    // Каждое сравнение строго в скобках, иначе cout выведет только 'a' и выдаст ошибку
    std::cout << "a == b: " << (a == b) << std::endl;
    std::cout << "a != b: " << (a != b) << std::endl;
    std::cout << "a > b: " << (a > b) << std::endl;
    std::cout << "a < b: " << (a < b) << std::endl;
    std::cout << "a >= b: " << (a >= b) << std::endl;
    std::cout << "a <= b: " << (a <= b) << std::endl;

    return 0;
}