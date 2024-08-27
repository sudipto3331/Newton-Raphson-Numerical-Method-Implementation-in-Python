#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:39:28 2023

@author: sudipto3331
"""

import math
import numpy as np
from xlwt import Workbook
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy


def func( x ):
	return x * x * x - x * x + 2


# which is 3*x^x - 2*x
def derivFunc( x ):
	return 3 * x * x - 2 * x

# Function to find the root
def newtonRaphson(xi, err, ite):
    x_i=np.zeros([ite])
    x_r=np.zeros([ite])
    
    
    rel_err=np.zeros([ite])
    itern=np.zeros([ite])
    
    x_i[0]=xi
    
    
    h = func(xi) / derivFunc(xi)
    xi = xi - h
    x_r[0] = xi
    
    print(x_i[0], x_r[0])
    
    
    for i in range(ite-1):
        itern[i]=i+1
        
        
        i = i+1
        
        x_i[i] = x_r[i-1]
        h = func(x_i[i])/derivFunc(x_i[i])
    	# x(i+1) = x(i) - f(x) / f'(x)
        x_r[i] = x_i[i] - h

        if i>0:
            rel_err[i]=abs(abs(x_r[i]-x_r[i-1])/x_r[i])*100
        #terminate if error criteria meets
        if all ([i>0, abs(rel_err[i])<err]):
            break 
            
        print(itern[i-1], x_i[i], x_r[i], rel_err[i])
        
        
    itern[i]=i+1
 
    
    wb = Workbook()

    sheet1 = wb.add_sheet('Sheet 1')
    num_of_iter=i-2

    sheet1.merge(0, 0, 1, 2)
    sheet1.write(0,1,'Newton Raphson',xlwt.easyxf("font: bold 1,height 250; align: horiz center"))

    sheet1.write(1,0,'Number of iteration')
    sheet1.write(1,1,'x_i')
    sheet1.write(1,2,'x_r')
    sheet1.write(1,3,'Relative error')
    

    for n in range(num_of_iter+2):
        
        sheet1.write(n+2,0,itern[n])
        sheet1.write(n+2,1,x_i[n])
        sheet1.write(n+2,2,x_r[n])
        sheet1.write(n+2,3,rel_err[n])
    
    sheet1.write(n+4,0,'The')
    sheet1.write(n+4,1,'root')
    sheet1.write(n+4,2,'is')
    sheet1.write(n+4,3,x_r[i])
    wb.save('LAB3.xls')
        

xi=np.float(input ('Enter initial guess: '))   
err=float(input('Enter desired percentage relative error: '))
ite=int(input('Enter number of iterations: '))

newtonRaphson(xi, err, ite)
    
print("Task Successfull");
