#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    double lbs, inches;

    std::cout << "Вес в фунтах: ";
    std::cin >> lbs;
    std::cout << "Вес в кг: " << lbs * 0.453592 << std::endl;

    std::cout << "Рост в дюймах: ";
    std::cin >> inches;
    std::cout << "Рост в см: " << inches * 2.54 << std::endl;

    return 0;
}