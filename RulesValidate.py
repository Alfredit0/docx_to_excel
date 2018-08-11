# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:21:48 2018

@author: Benito Alfredo Reyes
"""
ACRONYM=['DRA. ', 'DR. ', 'M. ', 'MTRO. ', 'MTRA. ', 'PROF. ', 'LIC. ', 'MTE ', 'M.C. ',
        'ING. ', 'M.C.E. ']

def searchAcronym(text):
    text=text.upper()
    for acr in ACRONYM:
        if(text.find(acr)!= -1):                        
            return True
    return False

def findDegreeFormat(text):
    return False

def isName(text):
    if(searchAcronym(text)):                        
            return True
    return False