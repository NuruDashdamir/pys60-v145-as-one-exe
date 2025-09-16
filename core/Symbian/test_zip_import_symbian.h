#ifndef ZIP_MODULE_LOADER_H
#define ZIP_MODULE_LOADER_H

#ifdef __cplusplus
extern "C" {
#endif
	int is_in_modules_zip(char* module_name);
	int load_module_from_zip(char* module_name);
#ifdef __cplusplus
}
#endif

#endif // ZIP_MODULE_LOADER_H
