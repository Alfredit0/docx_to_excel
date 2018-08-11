# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:48:46 2018

@author: Benito Alfredo Reyes
"""
import xlsxwriter
def saveDataToExcel(data, fileName):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(fileName+'.xlsx')
    worksheet = workbook.add_worksheet()    
    # Start from the first cell. Rows and columns are zero indexed.
    col = 0    
    for row, data in enumerate(data):
        worksheet.write_row(row,col, data)
    workbook.close()