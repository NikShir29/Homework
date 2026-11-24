#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    char c;
    std::cout << "Буква: ";
    std::cin >> c;

    // Арифметика превращает char в int, а обратное присваивание — обратно в char
    char next = c + 1; 
    
    std::cout << "Следующая: " << next << std::endl;

    /* 
     * Комментарий:
     * Если ввести 'Z', программа выведет символ '[' (открывающая квадратная скобка).
     * Буква 'Z' имеет код 90. Прибавление 1 дает 91, а под кодом 91 
     * в таблице ASCII находится символ '['.
     */
    return 0;
}