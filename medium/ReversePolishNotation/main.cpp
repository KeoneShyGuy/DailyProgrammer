// https://redd.it/5c5jx9
#include <iostream>
#include <cmath>
#include <algorithm> //find()
#include <stdlib.h> //atoi and itoa
#include <sstream> //ostringstream

#include "..\..\Python_scrap\Python_scrap.h" //Should work wherever I download it now

using namespace std;
int factorial(int factor);
float rpn(vector<string> e);

int main()
{
    Python_scrap py;
    vector<string> eqList;
    string equation = "1 2 3 4 ! + - / 100 *";
    cout << "Equation: " << equation << "\n";
    eqList = py.split(equation, " ");
    rpn(eqList);
    //atoi() converts to a string to an int
    //cout << (atoi("512") + atoi("400"));

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
    //int idx = 0;

    for (int i = 0; i < e.size(); i++){ //look into signed vs unsigned
        if (e[i] == "!"){
            //cout << "Factorial\n";
            int factor = factorial(atoi(e[i-1].c_str()));
            //cout << factor << "\n";
            char buff[12];
            itoa(factor, buff, 10);
            //e[i-1] =
            e.erase(e.begin() + i);
            e[i - 1] = buff;
            i--;
        }
        else if (e[i] == "+"){
            //cout << "Addition\n";
            float sum = atof(e[i - 1].c_str()) + atof(e[i - 2].c_str());
            //cout << sum << "\n";
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            ostringstream floatSum;
            floatSum << sum;
            string buffer = floatSum.str();
            e[i-2] = buffer;
        }
        else if (e[i] == "-"){
            //cout << "Subtraction\n";
            float difference = atof(e[i-2].c_str()) - atof(e[i-1].c_str());
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            ostringstream floatDiff;
            floatDiff << difference;
            string buffer = floatDiff.str();
            e[i-2] = buffer;
        }
        else if (e[i] == "*" || e[i] == "x"){
            //cout << "Multiplication\n";
        }
        else if (e[i] == "/"){
            //cout << "Float division\n";
        }
        else if (e[i] == "//"){
            //cout << "Integer division\n";
        }
        else if (e[i] == "%"){
            //cout << "Modulus\n";
        }
        else if (e[i] == "^"){
            //cout << "Power\n";
        }
        else{
            //cout << stck[i] << "\n";
            // cout << atoi(stck[i].c_str());
            // .c_str() converts a string to a constant char*
            stck.push_back(float(atoi(e[i].c_str())));
        }
    }
    cout << "Stack:\n";
    for (float f : stck)
        cout << f << "\n";
    cout << "Input Equation:\n";
    for (string s : e)
        cout << s << "\n";


    return 0;
}
