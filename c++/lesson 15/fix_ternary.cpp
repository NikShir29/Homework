#include <iostream>
#include <windows.h>

int main() {
    SetConsoleCP(65001); SetConsoleOutputCP(65001);
    int score = 82;

    // Ошибка А: не было скобок вокруг тернарника (приоритет операторов)
    std::cout << (score >= 60 ? "сдан" : "не сдан") << std::endl;
    // Ошибка Б: перепутаны местами результаты для "хорошо" и "отлично"
    std::cout << (score >= 90 ? "отлично" : "хорошо") << std::endl;
    return 0;
}