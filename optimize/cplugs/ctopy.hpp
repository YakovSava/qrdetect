# include <Python.h>
# include <map>
# include <string>
# include <vector>
using namespace std;

map<string, int> dict_to_map(PyObject* dict) {
  map<string, int> db;

  PyObject* key = NULL;
  PyObject* value = NULL;
  Py_ssize_t pos = 0;

  while (PyDict_Next(dict, &pos, &key, &value)) {
    string keyStr = PyUnicode_AsUTF8(key);
    int valueStr = PyLong_AsLong(value);

    db[keyStr] = valueStr;
  }
  return db;
}

static PyObject* map_to_dict(map<string, int> db) {
  PyObject* dict = PyDict_New();

  for (const auto& pair : db) {
    PyDict_SetItem(dict, PyUnicode_FromString(pair.first.c_str()), PyLong_FromLong(pair.second));
  }

  return dict;
}

static PyObject* string_to_str(string c_str) {
	return PyUnicode_FromString(c_str.c_str());
}

const char* str_to_string(PyObject* python_string) {
	return PyUnicode_AsUTF8(python_string);
}

vector<int> list_to_vector(PyObject* list) {
	vector<int> lst = {};
	Py_ssize_t listSize = PyList_Size(list);
	for (Py_ssize_t i = 0; i < listSize; ++i) {
		PyObject* pyElement = PyList_GetItem(list, i);

		int intValue = PyLong_AsLong(pyElement);
		lst.push_back(intValue);
	}
	return lst;
}

static PyObject* vector_to_list(vector<int> lst) {
	PyObject* pyList = PyList_New(0);
	for (int i = 0; i < lst.size(); i++) {
		PyList_Append(pyList, PyLong_FromLong(lst[i]));
	}
	return pyList;
}