# include "cwinfile.hpp"
# include "ctopy.hpp"
# include <Python.h>

static PyObject* write(PyObject *self, PyObject *args) {
	PyObject* filename_obj;
	PyObject* data_obj;

	if (!PyArg_ParseTuple(args, "UU", &filename_obj, &data_obj)) {
		return NULL;
	}

	int result = Cwrite(str_to_string(filename_obj), str_to_string(data_obj));

	return Py_BuildValue("i", result);
}

static PyObject* read(PyObject* self, PyObject* args) {
	PyObject* filename;

	if (!PyArg_ParseTuple(args, "U", &filename)) {
		return NULL;
	}

	string result = Cread(str_to_string(filename));

	return string_to_str(result);
}

static PyObject* exists_file(PyObject* self, PyObject* args) {
	PyObject* filename;

	if (!PyArg_ParseTuple(args, "U", &filename)) {
		return NULL;
	}

	bool result = exists(str_to_string(filename));

	return result ? Py_True : Py_False;
}

static PyMethodDef methods[] = {
	{"read", read, METH_VARARGS, "Reading a file using the low-level C++ programming language"},
	{"write", write, METH_VARARGS, "Writing to file using the low-level C++ programming language"},
	{"exists_file", exists_file, METH_VARARGS, "Checking the existence of the file"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "winfile",
    "I'm fine",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_winfile(void) {
    return PyModule_Create(&module);
}