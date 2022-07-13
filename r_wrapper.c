#include "Python.h"

extern int64_t* value(void);

//definition of data method
static PyObject* read_value(PyObject* self, PyObject* args)
{
    int data_len = 5;
    PyObject *result;
    result = PyList_New(data_len);
    if (result == NULL) {
        return NULL;
    }
    int64_t* data = value();
    for (int i = 0; i < data_len; i++){
        PyObject *item = Py_BuildValue("l", data[i]);
        Py_INCREF(item);
        PyList_SetItem(result, i, item);
        Py_DECREF(item);
    }
    return result;
}

//definition of all methods of my module
static PyMethodDef readmethods[] = {
    {"value", read_value, METH_VARARGS, NULL},
    {NULL},
};

// func module definition struct
static struct PyModuleDef readModule = {
    PyModuleDef_HEAD_INIT,
    "read",
    "",
    -1,
    readmethods
};

//module creator
PyMODINIT_FUNC PyInit_read(void)
{
    return PyModule_Create(&readModule);
}