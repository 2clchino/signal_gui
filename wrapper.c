#include "Python.h"

extern int data(int);

//definition of data method
static PyObject* func_data(PyObject* self, PyObject* args)
{
    int t, g;

    if (!PyArg_ParseTuple(args, "i", &t))
        return NULL;
    g = data(t);
    return Py_BuildValue("i", g);
}

//definition of all methods of my module
static PyMethodDef funcmethods[] = {
    {"data", func_data, METH_VARARGS},
    {NULL},
};

// func module definition struct
static struct PyModuleDef func = {
    PyModuleDef_HEAD_INIT,
    "func",
    "",
    -1,
    funcmethods
};

//module creator
PyMODINIT_FUNC PyInit_func(void)
{
    return PyModule_Create(&func);
}