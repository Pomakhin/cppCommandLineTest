//
//  main.cpp
//  testCommandLine
//
//  Created by Mikhail Pomakhin on 17.11.15.
//  Copyright © 2015 Mikhail Pomakhin. All rights reserved.
//

#include <iostream>
#include "test.h"

int main(int argc, const char * argv[])
{
    Foo *foo = new Foo();
    std::cout << foo->m_str << "\n";

    std::cout << "Hello, World!\n";
    return 0;
}
