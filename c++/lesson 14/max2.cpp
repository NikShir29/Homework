#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    int a, b;
    std::cout << "Введите два числа: ";
    std::cin >> a >> b;

    // Максимум через тернарник в присваивании
    int max_val = (a > b) ? a : b;
    std::cout << "Максимум: " << max_val << std::endl;

    // Каскад из двух тернарников для сравнения
    std::cout << (a > b ? "Больше первое число" : (b > a ? "Больше второе число" : "Числа равны")) << std::endl;

    return 0;
}