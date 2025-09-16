#ifndef INTERNAL_MODULE_IMPORTS_H_
#define INTERNAL_MODULE_IMPORTS_H_

void initgraphics(void);
void initcalendar(void);
void initcontacts(void);
void initglobalui(void);
void inite32db(void);
void initinbox(void);
void initkeycapture(void);
void initzlib(void);
void inittopwindow(void);
void inittelephone(void);
void initmessaging(void);
void initlogs(void);
void initlocationacq(void);
void initsysinfo(void);
void initsocket(void);

void initcamera(void); //missing lib on SymOS 9.1 SDK - mmfcontroller?
void initrecorder(void); //missing lib on SymOS 9.1 SDK - mmfcontroller?

#endif
