//https://redd.it/4uhqdb

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>

using namespace std;

int gcd(int a, int b);

int main(){
    int x = 4;
    int y = 8;
    int answer[2];
    string line;
    ifstream myFile ("fractions.txt");

    if (myFile.is_open()){
        while (getline(myFile, line)){
            cout << line << "\n";
            size_t found = line.find(" ");
            cout << found << "\n";
        }
        myFile.close();
    }
    else cout << "Unable to open file\n";
    int divisor = gcd(x, y);

    answer[0] = x / divisor;
    answer[1] = y / divisor;

    printf( "%d %d", answer[0], answer[1]);


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
