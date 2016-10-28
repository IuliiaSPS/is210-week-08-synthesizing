#! usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


BASE_COLOR = ['Seattle Gray', 'Manatee']
USER_COLOR = raw_input(('Which base color, "{0}" or "{1}"?:'.
                        format(BASE_COLOR[0], BASE_COLOR[1])))
if USER_COLOR == BASE_COLOR[0]:
    ACCENT = ['Ceramic Glaze', 'Cumulus Nimbus']
    USER_ACCENT = raw_input(('Which accent color, "{0}" or "{1}"?:'.
                             format(ACCENT[0], ACCENT[1])))
    if USER_ACCENT == ACCENT[0]:
        HIGHLIGHT = ['Basically White', 'White']
        USER_HIGH = raw_input(('Which highlight color, "{0}" or "{1}"?:'.
                               format(HIGHLIGHT[0], HIGHLIGHT[1])))
    if USER_ACCENT == ACCENT[1]:
        HIGHLIGHT = ['Off-White', 'Papper White']
        USER_HIGH = raw_input(('Which highlight color, :"{0}" or "{1}"?:'.
                               format(HIGHLIGHT[0], HIGHLIGHT[1])))
if USER_COLOR == BASE_COLOR[1]:
    ACCENT = ['Platinum Mist', 'Spartan Sage']
    USER_ACCENT = raw_input(('Which accent color, "{0}" or "{1}"?:'.
                             format(ACCENT[0], ACCENT[1])))
    if USER_ACCENT == ACCENT[0]:
        HIGHLIGHT = ['Bone White', 'Just White']
        USER_HIGH = raw_input(('Which highlight color, "{0}" or "{1}"?:'.
                               format(HIGHLIGHT[0], HIGHLIGHT[1])))
    if USER_ACCENT == ACCENT[1]:
        HIGHLIGHT = ['Fractal White', 'Not White']
        USER_HIGH = raw_input(('Which highlight color, "{0}" or "{1}"?:'.
                               format(HIGHLIGHT[0], HIGHLIGHT[1])))
print ('Your selected colors are, {0}, {1}, and {2}.'.
       format(USER_COLOR, USER_ACCENT, USER_HIGH))
