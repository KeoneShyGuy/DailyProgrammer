#include <iostream>
#include "Python_scrap.h"

using namespace std;
//using namespace Python_scrap;

int main()
{
    string meh = "Some old hags came around here and took our apples";
    vector<string> test;
    Python_scrap python;
    //python.split_line(meh, " ", true);
    test = python.split(meh, " ");
    cout << test.size();
    for (string n : test)
        cout << n << "\n";
    return 0;
}
