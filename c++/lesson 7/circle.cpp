#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    const double PI = 3.14159; // Константа, изменить нельзя
    double r;

    std::cout << "Радиус: ";
    std::cin >> r;

    // В формуле нет магических чисел, используется только переменная и константа
    std::cout << "Площадь: " << r * r * PI << std::endl;

    return 0;
}