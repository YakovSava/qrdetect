# include <stdio.h>

class Connector {
public:
  Connector() : reqc(0) {}
  
  const char* connect(const char* url) {
    reqc++;
    return "Hello world!"; // For example
  }
  
  int reqcount() const {
    return reqc;
  }

private:
  int reqc;
};