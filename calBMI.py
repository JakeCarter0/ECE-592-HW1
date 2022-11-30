"""
Created on Wed May 18 2022

@author: Jake Carter
PiE Homework 1 file 1:
Code for calculating BMI from height and weight inputs from user
"""
import sys

try:
    weightlbs = float(input('Enter weight (lbs): '))
    heightft = float(input('Enter height (ft): '))
except ValueError: # catches any non number inputs
    print('Invalid entry')
    sys.exit(-1)

if weightlbs <= 0 or heightft <= 0:
    print('Invalid weight or height')
    exit(-1)
weightkg = weightlbs * .4536
heightm = heightft * .3048
bmi = weightkg / (heightm ** 2)

print('Weight = {0} lbs = {1} kg,\nHeight = {2} ft = {3} m,\nBMI = {4}'.format(round(weightlbs, 3), round(weightkg,3), round(heightft,3), round(heightm,3), round(bmi,3)))

sys.exit()
