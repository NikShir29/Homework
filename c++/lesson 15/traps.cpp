#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);

    // 1) && требует, чтобы ОБА условия были истинны (5>3 - да, 8<6 - нет => 0).
    // || требует хотя бы одно (5>3 - да => 1).
    std::cout << "1) " << (5 > 3 && 8 < 6) << " " << (5 > 3 || 8 < 6) << std::endl;

    int age = 5;
    // 2) Присваивание = вместо сравнения ==. Возвращает 18 (истина), меняет age на 18.
    if (age = 18) { 
        std::cout << "2) ветка выполнилась" << std::endl;
    }
    std::cout << "2) age = " << age << std::endl;

    int x = -5;
    // 3) (0 < -5) дает 0. Затем (0 < 10) дает 1. Выражение истинно!
    std::cout << "3) " << (0 < x < 10) << " " << (x > 0 && x < 10) << std::endl;

    int a = 16;
    bool hasPass = true;
    // 4) Законы де Моргана: отрицание конъюнкции равно дизъюнкции отрицаний.
    std::cout << "4) " << !(a >= 18 && hasPass) << " " << (a < 18 || !hasPass) << std::endl;
    a = 25;
    std::cout << "4) " << !(a >= 18 && hasPass) << " " << (a < 18 || !hasPass) << std::endl;
    return 0;
}