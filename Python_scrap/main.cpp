#include <iostream>
#include "Python_scrap.h"

using namespace std;
//using namespace Python_scrap;

int main()
{
    string meh = "Some old hags came around here and took our apples";
    Python_scrap python;
    python.split_line(meh, " ", true);
    python.split(meh, " ", true);
    return 0;
}
