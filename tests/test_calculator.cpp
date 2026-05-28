#include "../src/calculator.h"
#include <cassert>

int main() {

    Calculator calc;

    assert(calc.add(2, 3) == 5);

    return 0;
}
