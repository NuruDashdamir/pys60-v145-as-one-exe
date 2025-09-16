#include <Python.h>

// C function that will be called to initialize a module from string

int init_embedded_py_module(char* module_name, char* module_code) {
    PyObject* module;
    PyObject* code_object;
    
    // compile the source code string into a code object
    code_object = Py_CompileString(module_code, "<embedded>", Py_file_input);
    
    // check if the compilation was successful
    if (code_object == NULL) {
        PyErr_Print();
        return;
    }
    
    // create and execute the module
    module = PyImport_ExecCodeModuleEx(
        (char*)module_name, 
        code_object, 
        (char*)"<embedded>"
    );
    
    // decrement the reference count for the code object   
    // check for errors during module creation
	Py_DECREF(code_object);
	if (module == NULL)
		return -1;
	//Py_DECREF(module); // I am not sure if I should DECREF the module here, need to read code
	return 1;
}
