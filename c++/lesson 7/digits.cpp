#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    int num;
    std::cout << "Двузначное число: ";
    std::cin >> num;

    // Деление на 10 отбрасывает последнюю цифру (получаем десятки)
    int tens = num / 10; 
    
    // Остаток от деления на 10 дает последнюю цифру (получаем единицы)
    int units = num % 10;

    std::cout << "Цифры: " << tens << " и " << units << std::endl;

    return 0;
}