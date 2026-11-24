#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    double c, f;
    
    std::cout << "Цельсий: ";
    std::cin >> c;
    std::cout << "Фаренгейт: " << c * 9.0 / 5.0 + 32.0 << std::endl;

    std::cout << "Фаренгейт: ";
    std::cin >> f;
    // Обратная формула: C = (F - 32) * 5 / 9
    std::cout << "Цельсий: " << (f - 32.0) * 5.0 / 9.0 << std::endl;

    // Намеренно портим формулу
    int scale = 9 / 5; // Целочисленное деление: 9 / 5 = 1
    std::cout << "Испорченная прямая формула: " << c * scale + 32.0 << std::endl;

    /*
     * Объяснение: При испорченной формуле переменная scale равна 1. 
     * Поэтому 36.6 * 1 + 32 = 68.6. Масштаб 1.8 превратился в 1.
     */
    return 0;
}