//
//  main.cpp
//  testCommandLine
//
//  Created by Mikhail Pomakhin on 17.11.15.
//  Copyright © 2015 Mikhail Pomakhin. All rights reserved.
//

#include <iostream>
#include "test.h"
#include <assert.h>
#include <boost/intrusive_ptr.hpp>
#include <boost/signals2.hpp>
#include <functional>
#include "AutoSignal.h"

using namespace std;
//using namespace std::placeholders;
using namespace boost::signals2;
using namespace DrakoSignals;

struct Hello
{
    void operator()() const
    {
        std::cout << "Hello";
    }
    
    
    void test1(int i)
    {
        std::cout << "test" << i << std::endl;
    }
};


void test()
{
    std::cout << "test" << std::endl;
}

struct World
{
    void operator()() const
    {
        std::cout << ", World!" << std::endl;
    }
};

int main(int argc, const char * argv[])
{
    boost::signals2::signal<void ()> sig;
    
    sig.connect(1, Hello());
    sig.connect(0, World());
    sig.connect(&test);
    sig();
    
    Hello h;
    typedef boost::signals2::signal<void (int)> SignalInt;
    SignalInt sig1;
    std::function<void(int)> bind_func = boost::bind(&Hello::test1, &h, _1);
    {
        scoped_connection connection = sig1.connect(bind_func);
        //sig1.connect([&](int i){h.test1(i);});
        
        sig1(2);
        //connection.disconnect();
        {
            //boost::signals2::shared_connection_block block(connection);
            sig1(3);
        }
        
    }
    
    sig1(56);
    
    
    
    
   // assert(false);
   // 
   // string inputString = "Internally, the function accesses the output sequence by first constructing a sentry object";

   // cout << inputString << '\n';

   // bool res = TextChecker::check(inputString, 20, 10);
   // cout << '\n' << (res ? "true" : "false") << '\n'; 

    
    //Bar bar;
    //bar.go();

    //auto foo = boost::intrusive_ptr<Bar>(&bar);


/*      for (int i = 1; i < 100; i++)
    {
        std::cout << i / 10 << "\n";
    }*/

/*      Foo *foo = new Foo();
    std::cout << foo->m_str << "\n";

    std::cout << "Hello, World!\n";*/
    return 0;
}
