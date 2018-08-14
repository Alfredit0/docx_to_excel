# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:46:54 2018

@author: Benito Alfredo Reyes
"""

from os import listdir
from os.path import isfile, join


from glob import glob
   

def ls(ruta):
    return [arch for arch in listdir(ruta) if not isfile(join(ruta, arch))]

def allDocxFiles(ruta='MEXICO'):
    result = []
    for folder in ls(ruta):
        for fname in glob('MEXICO/'+folder+'/*.docx'):
            result.append(fname)
    return result
        

print (allDocxFiles())

