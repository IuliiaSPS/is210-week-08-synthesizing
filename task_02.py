#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_03"""


MY_DAY = raw_input('What day is it? ').lower()
MY_TIME = int(raw_input('What time is it? '))

SNOOZE = (MY_DAY == 'sun' or MY_DAY == 'sat' or MY_TIME < 600)


if SNOOZE is False:
    print 'Beep! Beep! Beep! Beep! Beep!'
