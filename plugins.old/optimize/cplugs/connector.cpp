# include <Python.h>
# include "connector.hpp"
# include "ctopy.hpp"

typedef struct {
    PyObject_HEAD
    Connector* cpp_obj;
} PyConnector;

PyObject* PyConnector_connect(PyConnector* self, PyObject* args) {
    const char* url;
    if (!PyArg_ParseTuple(args, "s", &url)) {
        return NULL;
    }
    
    const char* result = self->cpp_obj->connect(url);
    return string_to_str(result);
}

PyObject* PyConnector_reqcount(PyConnector* self, PyObject* args) {
    int result = self->cpp_obj->reqcount();

    return Py_BuildValue("i", result);
}

static PyMethodDef PyConnector_methods[] = {
    {"connect", (PyCFunction)PyConnector_connect, METH_VARARGS, "Connect to a URL"},
    {"reqcount", (PyCFunction)PyConnector_reqcount, METH_VARARGS, "Return count of requests"},
    {NULL}
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "connector",
    "Python interface for the C++ Connector class",
    -1,
    PyConnector_methods
};

PyMODINIT_FUNC PyInit_connector(void) {
    return PyModule_Create(&module);
}