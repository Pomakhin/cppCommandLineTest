//
//  test.hpp
//  testCommandLine
//
//  Created by Mikhail Pomakhin on 17.11.15.
//  Copyright © 2015 Mikhail Pomakhin. All rights reserved.
//

#ifndef test_h
#define test_h

#include <stdio.h>
#include <string>

using namespace std;

class TextChecker
{
public:
    static bool check(const string &value, unsigned columnCount, unsigned rowCount);

    std::string m_str;

};

#endif /* test_h */
