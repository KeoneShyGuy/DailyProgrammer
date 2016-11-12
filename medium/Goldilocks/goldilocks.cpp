#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string* split_line(string line, const char* splitter);

int main(){
    string line;
    ifstream opts("challenge.txt");
    //get stuff from the first line
    getline(opts, line);
    cout << line << '\n';
    //get stuff from the rest of the lines
    getline(opts, line);
    cout << line << '\n';
    opts.close();
    split_line(line, " ");
return 0;
}

string* split_line(string line, const char* splitter){
    int c = 0;
    size_t tempFound = 0;
    size_t found = line.find(splitter);
    cout << found;
    while (found != string::npos){
        c++;
        tempFound = line.find(splitter, found);//I get an endless loop for some reason
        found = line.find(splitter, tempFound);
        cout << found;
    }
    cout << c;

}
