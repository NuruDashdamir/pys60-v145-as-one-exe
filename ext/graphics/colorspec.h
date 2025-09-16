/*
 * colorspec.h
 *
 *  Created on: Sep 16, 2025
 *      Author: Administrator
 */

#ifndef COLORSPEC_H_
#define COLORSPEC_H_

int ColorSpec_AsRgb(PyObject *color_object, TRgb *rgb);
int ColorSpec_Check(PyObject *color_object);
PyObject * ColorSpec_FromRgb(TRgb color);

#endif /* COLORSPEC_H_ */
