// https://redd.it/5bn0b7
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

string* split_line(string line, const char* splitter, bool deb = false);

int main(){
    string line;
    string chairs = "";
    ifstream opts("challenge.txt");
    int weight, temperature, tempWeight, tempTemp;
    int count_ = 0;
    //get stuff from the first line
    getline(opts, line);
    string* limits = split_line(line, " ");

    stringstream(limits[0]) >> weight; //convert string to int
    stringstream(limits[1]) >> temperature;
    cout << temperature << "\n";
    while (getline(opts, line)){
        string* tempLimits = split_line(line, " ");
        stringstream(tempLimits[0]) >> tempWeight;
        stringstream(tempLimits[1]) >> tempTemp;
        count_++;
        //cout << count_ << " " << tempWeight << "\n";
        if(tempWeight >= weight && tempTemp <= temperature)
            cout << count_ << "  ";
    }
    opts.close();
    cout << chairs;

return 0;
}

string* split_line(string line, const char* splitter, bool deb){
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
