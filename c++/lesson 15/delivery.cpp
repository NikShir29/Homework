#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int weight, zone, urgent;
    std::cin >> weight >> zone >> urgent;

    // Проверка веса обязана быть до switch, чтобы не считать стоимость 
    // для несуществующего груза.
    if (weight < 1) {
        std::cout << "Ошибка: вес должен быть не меньше 1" << std::endl;
        return 0;
    }

    int cost = 0;
    switch (zone) {
    case 1: cost += 50; break;
    case 2: cost += 120; break;
    case 3: cost += 250; break;
    default: 
        std::cout << "Ошибка: зоны с кодом " << zone << " нет" << std::endl;
        return 0;
    }

    if (weight > 10) cost += 200;
    else if (weight > 5) cost += 100;

    if (urgent == 1) cost += 150;

    std::cout << "К оплате: " << cost << " руб" << std::endl;
    
    // Упрощенное условие (только weight > 5) опровергается тестом (7, 3, 0), 
    // где вес 7, но доставка не срочная, значит груз стандартный.
    std::cout << ((weight > 5 && urgent == 1) ? "Груз: тяжёлый срочный" : "Груз: стандартный") << std::endl;
    return 0;
}