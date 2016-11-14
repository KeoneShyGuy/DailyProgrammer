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

vector <string> split(string line, const char* delim, bool debug){
    int vSize = 0; //the size of the new vector. I may not need this
    vector <string> splitArr;
    size_t stringStart, stringEnd, tempLoc; // I feel smart as fuck now
    int delimLoc = 0; //may product an error if the delim is the first char. Error test later
    while (line.find(delim, (delimLoc)) != string::npos){
        delimLoc = line.find(delim, delimLoc);
        splitArr.push_back(line.substr());
    }
    if (debug){
        for (string s : splitArr)
            cout << s << "\n";
    }
    return splitArr;
}
