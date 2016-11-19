// https://redd.it/5c5jx9
#include <iostream>
#include <cmath>        //pow() and fmod()
#include <algorithm>    //find()
#include <stdlib.h>     //atoi and itoa
#include <iomanip>      //setprecision
//I got C++ 11 working midway through, but I don't feel like fixing everything
#include "..\..\Python_scrap\Python_scrap.h" //Should work wherever I download it now

using namespace std;
int factorial(int factor);
double rpn(vector<string> e);

int main()
{
    Python_scrap py;

    string eq1 = "1 2 3 4 ! + - / 100 *";
    string eq2 = "0.5 1 2 ! * 2 1 ^ + 10 + *";
    string eq3 = "100 807 3 331 * + 2 2 1 + 2 + * 5 ^ * 23 10 558 * 10 * + + *";
    vector<string> equations = {eq1, eq2, eq3};
    vector<string> eqList;
    for (string eq : equations){
        string split = "\n______________________________________\n";
        eqList = py.split(eq, " ");
        cout << "Input Equation:\n" << eq << "\n";
        cout.setf(ios::fixed);
        cout << "Final Answer:\n" << std::setprecision(0) << rpn(eqList) << split;
    }
    return 0;
}

int factorial(int factor){
    int product = 1;
    for (int i = 2; i<= factor; i++)
        product *= i;
    return product;
}

double rpn(vector<string> e){
    for (unsigned int i = 0; i < e.size(); i++){ //look into signed vs unsigned
        if (e[i] == "!"){ // Factorial
            int factor = factorial(stoi(e[i-1]));
            e.erase(e.begin() + i);
            e[i - 1] = to_string(factor);
            i--;
        }
        else if (e[i] == "+"){ // Addition
            double sum = stod(e[i - 2]) + stod(e[i - 1]);
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            e[i-2] = to_string(sum);
            i -= 2;
        }
        else if (e[i] == "-"){ // Subtraction
            double difference = stod(e[i-2]) - stod(e[i-1]);
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            e[i-2] = to_string(difference);
            i -= 2;
        }
        else if (e[i] == "*" || e[i] == "x"){ // Multiplication
            double product = stod(e[i-2]) * stod(e[i-1]);
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            e[i-2] = to_string(product);
            i -= 2;
        }
        else if (e[i] == "/"){ // Float Division
            double quotient = stod(e[i-2]) / stod(e[i-1]);
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            e[i-2] = to_string(quotient);
            i -= 2;
        }
        else if (e[i] == "//"){ // Int Division
            int quotient = int(stod(e[i-2]) / stod(e[i-1]));
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            e[i-2] = to_string(quotient);
            i -= 2;
        }
        else if (e[i] == "%"){ // Modulus
            double remainder = fmod(stod(e[i-2]), stod(e[i-1]));
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            e[i-2] = to_string(remainder);
            i -= 2;
        }
        else if (e[i] == "^"){ // Power
            double power = pow(stod(e[i-2]), stod(e[i-1]));
            e.erase(e.begin() + i);
            e.erase(e.begin() + i - 1);
            e[i-2] = to_string(power);
            i -= 2;
        }
        else{/*Don't do a damn thing*/}
    }

    return stod(e[0]);
}
