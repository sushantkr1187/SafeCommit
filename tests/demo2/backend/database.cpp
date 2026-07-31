#include <iostream>
#include "database.h"

static const std::string CONNECTION =
"postgresql://admin:SuperSecret123@localhost:5432/storedb";

void connectDatabase() {

    std::cout << "Connecting..." << std::endl;
}