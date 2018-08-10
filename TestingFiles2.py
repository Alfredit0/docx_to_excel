# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:21:48 2018

@author: Benito Alfredo Reyes
"""
import ReadWord
import RulesValidate
import io

filePath="AGUASCALIENTES.docx"
content= io.StringIO(ReadWord.get_docx_text(filePath))

university = ''
name = ''
mail = ''
data = ''

cont= 0
for line in content.readlines(): #Se comienza a leer cada una de las lineas del contenido
    if  line.find("Enviado el") == -1:
        if line.isupper() and len(line)>10:          
            university = line.strip()#Se identifica si la linea es un nombre de Universidad                
        elif RulesValidate.isNameWithDegree(line):
            name = line.strip()
        elif  line.find("@") != -1: #Se identifica si la linea es un correo            
            mail = line.strip()
        else: 
            if  len(line) > 1:                
                data = data + line.strip() + ","    
    else:
        cont=cont+1
        print('\n\n=== Nuevo contacto # '+str(cont)+ '===')          
        print('Universidad: ' + university)          
        print('Nombre: ' + name)
        print('Correo: ' + mail)
        print("Datos : " + data.rstrip(','))
        name = ''
        mail = ''
        data = ''
                