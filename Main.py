# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:21:48 2018

@author: Benito Alfredo Reyes
"""
import ReadWord
import RulesValidate
import WriteExcel
import io

filePath='AGUASCALIENTES.docx'
content= io.StringIO(ReadWord.get_docx_text(filePath))

university = ''
name = ''
mail = ''
data = ''
contactsData = []
cont= 0
for line in content.readlines(): #Reading line by line of the content
    if  line.find("Enviado el") == -1:
        if line.isupper() and len(line)>10:          
            university = line.strip()           
        elif RulesValidate.isName(line):#Identify if the line is a university name    
            name = line.strip()
        elif  line.find("@") != -1: #Identify if the line is an email            
            mail = line.strip()
        else: 
            if  len(line) > 1:                
                data = data + line.strip() + ","    
    else:
        cont=cont+1        
        contactsData.append(['MEXICO', university, data.rstrip(','),name, mail, '1'])
        name = ''
        mail = ''
        data = ''                

WriteExcel.saveDataToExcel(contactsData, 'Contacts')