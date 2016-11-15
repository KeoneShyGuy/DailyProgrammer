#include "Python_scrap.h"
//#include <iostream>
//#include <string>
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

vector <string> Python_scrap::split(string line, const char* delim, bool debug){
    int vSize = 0; //the size of the new vector. I may not need this
    int c = 0;
    vector <string> splitArr;
    string newStr;
    size_t length, tempLoc; // I feel smart as fuck now
    int delimLoc = 0; //may product an error if the delim is the first char. Error test later
    //cout << "String Length: " << line.size() << "\n";
    while (line.find(delim, delimLoc) != string::npos){
        if (c == 0)
            tempLoc = delimLoc;
        else
            tempLoc = delimLoc + 1;
        delimLoc = line.find(delim, tempLoc);
        if (delimLoc == (-1))
            delimLoc = line.size();
        length = delimLoc - tempLoc;
        //cout << "TempLoc : " << tempLoc << " | DelimLoc: " << delimLoc << " | Length: " << length << "\n";
        newStr = line.substr(tempLoc, length);
        //cout << newStr << "\n";
        splitArr.push_back(newStr);
        c++;
    }
    if (debug){
        for (string s : splitArr)
            cout << "|" << s << "|\n";
    }
    return splitArr;
}
