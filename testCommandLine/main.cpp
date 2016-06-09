//
//  main.cpp
//  testCommandLine
//
//  Created by Mikhail Pomakhin on 17.11.15.
//  Copyright © 2015 Mikhail Pomakhin. All rights reserved.
//

#include <iostream>
#include "test.h"

using namespace std;

int main(int argc, const char * argv[])
{

    string inputString = "Internally, the function accesses the output sequence by first constructing a sentry object";

    cout << inputString << '\n';

    bool res = TextChecker::check(inputString, 20, 10);
    cout << '\n' << (res ? "true" : "false") << '\n'; 




/*      for (int i = 1; i < 100; i++)
    {
        std::cout << i / 10 << "\n";
    }*/

/*      Foo *foo = new Foo();
    std::cout << foo->m_str << "\n";

    std::cout << "Hello, World!\n";*/
    return 0;
}
