#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    bool A = false, B = false;
    std::cout << "A=" << A << " B=" << B << " &&=" << (A && B) << " || =" << (A || B) << std::endl;
    
    B = true;
    std::cout << "A=" << A << " B=" << B << " &&=" << (A && B) << " || =" << (A || B) << std::endl;

    A = true, B = false;
    std::cout << "A=" << A << " B=" << B << " &&=" << (A && B) << " || =" << (A || B) << std::endl;

    B = true;
    std::cout << "A=" << A << " B=" << B << " &&=" << (A && B) << " || =" << (A || B) << std::endl;

    return 0;
}