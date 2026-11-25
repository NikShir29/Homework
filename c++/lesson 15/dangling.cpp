#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int group = 1; int score = 9;

    // Исходный код: else привязан к ближайшему if (score >= 8), а не к group == 1.
    // Поэтому для group 2 не печаталось ничего.
    // Исправление фигурными скобками:
    if (group == 1) {
        if (score >= 8) {
            std::cout << "Утренняя смена, допуск есть" << std::endl;
        } else {
            std::cout << "Утренняя смена, допуска нет" << std::endl;
        }
    } else {
        std::cout << "Вечерняя смена" << std::endl;
    }
    return 0;
}