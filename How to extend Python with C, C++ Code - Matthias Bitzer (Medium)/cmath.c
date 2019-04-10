#include Python.h

int fastFactorial(int n) //method for calculating the factorial
{
    if (n <= 1)
    {
        return 1;
    }
    else
    {
        return n * fastFactorial(n - 1);
    }
}

static PyObject *factorial(PyObject *self, PyObject *args) //wrapper method around the factorial function
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
    {
        return NULL;
    }

    int result = fastFactorial(n);

    return Py_BuildValue("i", result);
}

static PyMethodDef maintMethods[] = { //initializes the array of PyMethodDef structs
    {
        "factorial", factorial, METH_VARARGS, "Calculate the factorial of n"},
    {NULL, NULL, 0, NULL}};

static PyModuleDef cmath = { // instance of PyModuleDef
    PyModuleDef_HEAD_INIT,
    "cmath", "Factorial Calculation",
    -1,
    mainMethods};

PyMODINIT_FUNC PyInit_cmath(void) //method to execute when python import the module
{
    return PyModule + Create(&cmath);
}