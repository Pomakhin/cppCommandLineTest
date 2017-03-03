//
//  test.cpp
//  testCommandLine
//
//  Created by Mikhail Pomakhin on 17.11.15.
//  Copyright © 2015 Mikhail Pomakhin. All rights reserved.
//

#include "test.h"
#include <iterator>
#include <iostream>
#include <algorithm>

bool processWord(const string::const_iterator &wordBegin, 
                 const string::const_iterator &wordEnd, 
                 const unsigned maxColumn,
                 const unsigned maxRow,
                 unsigned &columnCursor, 
                 unsigned &rowCursor)
{
    bool result = false;
    unsigned wordLength = wordEnd - wordBegin + 1u;
    if (columnCursor + wordLength <= maxColumn)
    {
        for (auto it = wordBegin; it <= wordEnd; ++it)
        {
            cout << *it;
        }
        // inc columnCursor
        columnCursor += wordLength;
        result = true;
    }
    else if (++rowCursor < maxRow)
    {
        cout << '\n';
        columnCursor = 0;
        result = processWord(wordBegin, wordEnd, maxColumn, maxRow, columnCursor, rowCursor);
    }
    return result;
}

bool processWhiteSpace(const string::const_iterator &whiteSpace, 
                 const unsigned maxColumn,
                 unsigned &columnCursor)
{
    bool result = true;
    if (columnCursor + 1 <= maxColumn)
    {
        cout << '_';
        columnCursor++;
    }
    else
    {
        // ignore whitespace in the end of row
    }
    return result;
}

bool TextChecker::check(const string &value, unsigned columnCount, unsigned rowCount)
{
    if (columnCount && rowCount)
    {
        if (value.length())
        {
            bool result = true;
            // row cursor points on the first row with id = 0
            unsigned rowCursor = 0;
            // cursor point exactly on the last char inserted to the row; 0 - is before the first column
            unsigned columnCursor = 0;
            string::const_iterator wordBegin = value.end();
            string::const_iterator wordEnd = value.end();
            //for (all chars)
            for (string::const_iterator charIter = value.begin(); charIter != value.end(); ++charIter)
            {
                // if char from word
                if (*charIter != ' ')
                {
                    // if word not started
                    if (wordBegin == value.end())
                    {
                        // save start word position
                        wordBegin = charIter;
                    }
                }
                else
                // else (not from word)
                {
                    // if word started
                    if (wordBegin != value.end())
                    {
                        // save end word position
                        wordEnd = charIter - 1;
                        // if not process word
                        if (!processWord(wordBegin, wordEnd, columnCount, rowCount, columnCursor, rowCursor))
                        {
                            result = false;
                            break;
                        }
                    }
                    // if not process non-word character
                    if (!processWhiteSpace(charIter, columnCount, columnCursor))
                    {
                        result = false;
                        break;
                    }
                    // reset word
                    wordBegin = value.end();
                    wordEnd = value.end();
                }
            }
            if (result && wordBegin != value.end())
            {
                wordEnd = value.end() - 1;
                result = processWord(wordBegin, wordEnd, columnCount, rowCount, columnCursor, rowCursor);
            }
            return result;
        }
        else
        {
            return true;
        }
    }
    else
    {
        return false;
    }
}


void Foo::test(const std::function<void()> &a_function)
{
    a_function();
}

void Bar::func()
{
    cout << "func\n";
}
void Bar::go()
{
    Foo foo;
    foo.test(
             [&]
                {
                    func();
                });
}




void intrusive_ptr_add_ref(Bar* pointer)
{
    std::cout << "intrusive_ptr_add_ref";
}

void intrusive_ptr_release(Bar* pointer)
{
    std::cout << "intrusive_ptr_release";
}
