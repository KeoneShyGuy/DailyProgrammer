#ifndef PYTHON_SCRAP_H
#define PYTHON_SCRAP_H

#include <iostream>
#include <string>
using namespace std;

class Python_scrap{

  public:
      string* split_line(string line, const char* splitter, bool deb = false);
};
#endif // PYTHON_SCRAP_H
