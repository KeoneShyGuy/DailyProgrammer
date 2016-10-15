#include <iostream>
#include <stdio.h>
#include <stdint.h>
//#include <array>
using namespace std;

string reverse_factorial(int64_t factor);

main(){
    int64_t z[5] = {3628800, 479001600, 6, 18};
    z[4] = 2432902008176640000;

    int zLength = sizeof(z) / sizeof(z[0]);

    for(int i = 0; i < zLength; i++)
        cout << z[i] << " " << reverse_factorial(z[i]) << "\n";


    return 0;
}

string reverse_factorial(int64_t factor){
    int64_t x = factor;
    int c = 2;
    int64_t temp;
    char buff[8];
    string answer;
    while (x != 1){
        temp = x;
        if (x % c !=0){
            return "NONE";
        }
        x = x / c;
        c++;
    }
    snprintf(buff, sizeof(buff), "= %d!", temp);
    answer = buff;

    return answer;
}
