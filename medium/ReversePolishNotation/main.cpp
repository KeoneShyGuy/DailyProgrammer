// https://redd.it/5c5jx9
#include <iostream>
#include "F:\Documents\DailyProgrammer\Python_scrap\Python_scrap.h"

using namespace std;
int factorial(int factor);

int main()
{
    Python_scrap py;
    vector<string> stck;
    string equation = "1 2 3 4 ! + - / 100 *";
    stck = py.split(equation, " ");
    for (string s : stck)
        cout << s << "\n";
    cout << factorial(4);
    return 0;
}

int factorial(int factor){
    int product = 1;
    for (int i = 2; i<= factor; i++)
        product *= i;
    return product;
}
