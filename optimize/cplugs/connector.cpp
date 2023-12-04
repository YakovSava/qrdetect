# include <Python.h>
# include "ctopy.hpp"

class Connector {
public:
  Connector() : reqc(0) {}
  
  const char* connect(const char* url) {
    reqc++;
    return nullptr; // For example
  }
  
  int reqcount() const {
    return reqc;
  }

private:
  int reqc;
};