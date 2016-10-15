//https://redd.it/4uhqdb

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int gcd(int a, int b);
string* split_line(string x, const char* y);

int main(){

    int answer[2];
    string line;
    ifstream myFile ("fractions.txt");

    if (myFile.is_open()){
        while (getline(myFile, line)){
            string* fractions = split_line(line, " ");
            int numerator, denominator, divisor;
            stringstream(fractions[0]) >> numerator;
            stringstream(fractions[1]) >> denominator;

            divisor = gcd(numerator, denominator);
            printf ("%d %d\n", (numerator / divisor), (denominator / divisor));

        }
        myFile.close();
    }
    else cout << "Unable to open file\n";


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

string* split_line(string x, const char* y){
    size_t SplitLocation  = x.find(y);
    string* words = new string[2];
    string first (x, 0, SplitLocation);
    string second (x, SplitLocation, x.length());
    words[0] = first;
    words[1] = second;

    return words;
}
