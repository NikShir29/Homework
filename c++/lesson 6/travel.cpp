#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    double distance, time;

    std::cout << "Расстояние и время: ";
    std::cin >> distance >> time;

    // Скорость = расстояние / время (оба double, поэтому деление дробное)
    std::cout << "Скорость: " << distance / time << std::endl;

    return 0;
}