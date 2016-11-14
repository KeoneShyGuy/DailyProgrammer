#include "Python_scrap.h"
#include <iostream>
#include <string>
using namespace std;

string* Python_scrap::split_line(string line, const char* splitter, bool deb){
    int c = 0;
    int locationBuff[100]; //will store 100 locations. Shouldn't need more than that
    locationBuff[0] = 0;;
    size_t found = 0;
    while (line.find(splitter, (found + 1)) != string::npos){
        c++;
        found = line.find(splitter, (found + 1));
        locationBuff[c] = int(found + 1);
    }
    string* lineArr = new string[c + 1];
    for(int i = 0; i <= c; i++){
        if (i < c)
            lineArr[i] = line.substr(locationBuff[i], (locationBuff[i+1] - locationBuff[i] -1));

        else
            lineArr[i] = line.substr(locationBuff[i]);
    }
    if (deb){
        for (int i = 0; i <= c; i++){
            cout << "|" << lineArr[i] << "|\n";
        }
    }
    return lineArr;
}
