#include <iostream>

using namespace std;

int gcd(int a, int b);

int main(){
    cout << gcd(27, 18);
return 0;
}

int gcd(int a, int b){
    int c;

    while (b){
        c = a;
        a = b;
        b = c%b;
    }
    return a;
}
