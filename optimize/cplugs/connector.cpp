# include <boost/python.hpp>
using namespace boost::python;

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

BOOST_PYTHON_MODULE(Connector) {
    class_<Connector>("Connector")
        .def("connect", &Connector::connect)
        .def("reqcount", &Connector::reqcount);
}