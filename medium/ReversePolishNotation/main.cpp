// https://redd.it/5c5jx9
#include <iostream>
#include <cmath>
#include <algorithm> //find()
#include <stdlib.h> //atoi
#include "..\..\Python_scrap\Python_scrap.h" //Should work wherever I download it now

using namespace std;
int factorial(int factor);
float rpn(vector<string> e);

int main()
{
    Python_scrap py;
    vector<string> eqList;
    string equation = "1 2 3 4 ! + - / 100 *";
    eqList = py.split(equation, " ");
    rpn(eqList);
    //atoi() converts to a string to an int
    cout << (atoi("512") + atoi("400"));

    return 0;
}

int factorial(int factor){
    int product = 1;
    for (int i = 2; i<= factor; i++)
        product *= i;
    return product;
}

float rpn(vector<string> e){
    vector<float> stck;

    for (string n : e){
        if (n == "!")
            cout << "Factorial\n";
        else if (n == "+")
            cout << "Addition\n";
        else
            cout << n << "\n";
        }



    return 0;
}
