// https://redd.it/5c5jx9

#include <iostream>
#include <string>

int factorial(int factor);

int main(){
    std::string equation;
    int duh = factorial(7);
    std::cout << "Enter your equation: \n";
    std::getline(std::cin, equation);
    std::cout << equation << "\n";
    std::cout << duh;
return 0;
}

int factorial(int factor){
    int product = 1;
    for(int i = 2; i <= factor; i++)
        product *= i;
    return product;
}
