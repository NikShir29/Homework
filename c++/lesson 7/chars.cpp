#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    std::cout << 'A' << std::endl;
    
    // Выводим числовой код символа 'A' (65)
    std::cout << static_cast<int>('A') << std::endl; 
    
    std::cout << 'a' << std::endl;
    std::cout << '0' << std::endl;
    std::cout << 0 << std::endl;

    /* 
     * Комментарий:
     * Символ '0' и число 0 на экране выглядят одинаково, но внутри компьютера 
     * это разные вещи. '0' — это символ, который хранится в памяти как число 48 
     * (по таблице ASCII). А число 0 — это математический ноль, хранящийся как 0.
     */
    return 0;
}