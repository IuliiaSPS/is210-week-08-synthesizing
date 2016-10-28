#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_03"""


import decimal


MY_NAME = raw_input('What is your name? ')
MY_PRINCIPAL = int(raw_input('What is the principal of the loan? '))
YEARS = int(raw_input('For how long is this being borrowed? '))
MY_PRE_QUAL = raw_input('Are you pre-qualified? ').lower()
PERIODS = 12


if MY_PRE_QUAL == 'yes' or MY_PRE_QUAL == 'y':
    PRE_QUAL = True
else:
    PRE_QUAL = False

if MY_PRINCIPAL <= 199999:
    if 1 <= YEARS <= 15:
        if PRE_QUAL:
            RATE = 3.63
        else:
            RATE = 4.65
    elif 16 <= YEARS <= 20:
        if PRE_QUAL:
            RATE = 4.04
        else:
            RATE = 4.98
    else:
        if PRE_QUAL:
            RATE = 5.77
        else:
            RATE = 6.39

if 200000 <= MY_PRINCIPAL <= 999999:
    if 1 <= YEARS <= 15:
        if PRE_QUAL:
            RATE = 3.02
        else:
            RATE = 3.98
    elif 16 <= YEARS <= 20:
        if PRE_QUAL:
            RATE = 3.27
        else:
            RATE = 4.08
    else:
        if PRE_QUAL:
            RATE = 4.66
        else:
            RATE = None

if MY_PRINCIPAL >= 1000000:
    if 1 <= YEARS <= 15:
        if PRE_QUAL:
            RATE = 2.05
        else:
            RATE = None
    else:
        if PRE_QUAL:
            RATE = 2.62
        else:
            RATE = None

if PRE_QUAL:
    PRE_QUAL = 'yes'
else:
    PRE_QUAL = 'no'

if RATE is None:
    TOTAL = 'None'
else:
    RATE = RATE / 100
    TOTAL = (round(MY_PRINCIPAL * ((1 + decimal.Decimal(RATE / PERIODS)) **
                                   (PERIODS * YEARS))))
REPORT = ('Loan report for: {0}\n'.format(MY_NAME,) + '-' * 30 +
          '\nPrincipal:        ${0}'.format(MY_PRINCIPAL) +
          '\nDuration:         {0}yrs'.format(YEARS)+
          '\nPre-qualified?:   {0}'.format(PRE_QUAL) +
          '\n\nTotal:         ${0}'.format(TOTAL))

print REPORT
