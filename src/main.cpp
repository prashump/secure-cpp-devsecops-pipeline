#include <iostream>
#include "calculator.h"

int main() {

    Calculator calc;

    std::cout << "Addition: "
              << calc.add(5, 3)
              << std::endl;

    return 0;
}
