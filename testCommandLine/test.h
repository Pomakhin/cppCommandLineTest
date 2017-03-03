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
#include <functional>

using namespace std;

class Foo
{
public:
    void test(const std::function<void()> &a_function);
};

class Bar
{
public:
    void func();
    void go();
};


class TextChecker
{
public:
    static bool check(const string &value, unsigned columnCount, unsigned rowCount);

    std::string m_str;

};


void intrusive_ptr_add_ref(Bar* pointer);
void intrusive_ptr_release(Bar* pointer);

#endif /* test_h */
