#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int score, absences;
    std::cin >> score >> absences;

    if (score < 0 || score > 10) {
        std::cout << "Ошибка: балл от 0 до 10" << std::endl;
        return 0;
    }

    std::cout << ((score >= 8 && absences <= 2) ? "Стипендия назначена" : "Стипендия не назначена") << std::endl;
    return 0;
}