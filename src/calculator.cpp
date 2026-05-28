#include "calculator.h"
#include <stdexcept>

int Calculator::add(int a, int b) {
    return a + b;
}

int Calculator::divide(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("division by zero");
    }

    return a / b;
}
