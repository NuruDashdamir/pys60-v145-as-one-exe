/*
 * fontspec.h
 *
 *  Created on: Sep 16, 2025
 *      Author: Administrator
 */

#ifndef FONTSPEC_H_
#define FONTSPEC_H_

int system_font_from_label(const char * aLabel, const CFont *&aFont);

int TFontSpec_from_python_fontspec(
    PyObject *aArg,
    TFontSpec &aFontSpec,
    MGraphicsDeviceMap &aDeviceMap);

int CFont_from_python_fontspec(
    PyObject *aArg,
    CFont *&aFont,
    MGraphicsDeviceMap &aDeviceMap);

PyObject * python_fontspec_from_TFontSpec(
    const TFontSpec &aFontSpec,
    MGraphicsDeviceMap &aDeviceMap);

#endif /* FONTSPEC_H_ */
