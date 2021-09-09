#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
addition(PyObject *self, PyObject *args)
{

    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}