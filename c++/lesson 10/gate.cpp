#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    int age, passInput;
    std::cout << "Введите возраст и код пропуска: ";
    std::cin >> age >> passInput;

    bool hasPass = passInput != 0;

    bool isAdult = age >= 18;
    bool canEnter = isAdult && hasPass;
    bool isDiscount = (age <= 12) || (age >= 65);
    bool isDenied = !canEnter;

    std::cout << "Взрослый: " << isAdult << std::endl;
    std::cout << "Допуск в зал: " << canEnter << std::endl;
    std::cout << "Льгота: " << isDiscount << std::endl;
    std::cout << "Отказ: " << isDenied << std::endl;
    
    bool demorgan1 = !((age < 18) || (!hasPass));
    bool demorgan2 = (age >= 18) && hasPass;
    std::cout << "Совпадение де Моргана: " << demorgan1 << " " << demorgan2 << std::endl;

    return 0;
}