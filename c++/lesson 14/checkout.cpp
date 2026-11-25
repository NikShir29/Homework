#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    int price, qty;
    std::cout << "Цена и количество: ";
    std::cin >> price >> qty;

    // Шаг 1: Ранний отказ
    if (qty < 1) {
        std::cout << "Количество должно быть не меньше 1" << std::endl;
        return 0;
    }

    // Шаг 2: Сумма и скидка
    int sum = price * qty;
    int percent = 0;
    
    // Границы через "строго больше" (>), чтобы 5000 не давало 10%
    if (sum > 5000) {
        percent = 10;
    } else if (sum > 1000) {
        percent = 5;
    }

    // Скидка 0% не портит сумму, так как sum * 0 / 100 = 0
    int discount = sum * percent / 100;
    int total = sum - discount;

    std::cout << "Сумма: " << sum << ", скидка " << percent << "%, к оплате: " << total << std::endl;

    // Шаг 3: Оплата
    int paid;
    std::cout << "Внесено: ";
    std::cin >> paid;

    if (paid >= total) {
        std::cout << "Оплата прошла" << std::endl;
        std::cout << "Сдача: " << (paid - total) << " руб" << std::endl;
    } else {
        std::cout << "Недостаточно средств: ещё " << (total - paid) << " руб" << std::endl;
    }

    // Шаг 4: Категория (через тернарник)
    std::cout << "Категория: " << (total > 4000 ? "существенная скидка" : "обычная покупка") << std::endl;

    /* 
     * Исследование "Если было легко":
     * Каскад можно переписать так: int percent = sum > 5000 ? 10 : (sum > 1000 ? 5 : 0);
     * Читаемость: обычный if/else читается гораздо лучше, особенно если скидок станет 5. 
     * Вложенные тернарники быстро становятся нечитаемыми.
     */
    return 0;
}