"""
Created on Wed May 18 2022

@author: Jake Carter
PiE Homework 1 file 2:
Includes pyramid, findSquares, calSalary, calLetterGrade functions for homework 1
"""


def pyramid(s:str):
    """
    pyramid(s:str)
    Takes a string input (s) and creates a message pyramid out of it
    """
    i = 1
    while i <= len(s):
        print(s[0:i])
        i += 1

def findSquares(s:int = 0, e:int = 0):
    """
    findSquares(s:int = 0, e:int = 0)
    Takes 2 integer inputs and finds all perfect squares between them
    If only one arguement is entered, all perfect squares less than the input will be output
    """
    import math
    squares = []
    i = max(0, min(s, e)) #Sets minimum perfect square to 0 or smaller input
    upperBound = max(s, e)
    while i <= upperBound:
        if math.isqrt(i) ** 2 == i:
            squares.append(i)
        i +=1
    return squares

def calSalary(h:float, r:float = 20):
    """
    calSalary(h:float, r:float = 20)
    Takes a float inputs for hours (h) worked and for hourly rate (r) and calulates salary
    If no hourly rate is specified, a default rate of 20 will be used
    """
    if h < 0: #
        print("Not valid Hours")
        return -1
    elif h > 40: #overtime case
        return (40 * r) + ((h - 40) * r * 1.2)
    else: #base case
        return h * r * 1.0

def calLetterGrade(points:float, gradescale:list = [98, 94, 91, 88, 85, 82, 79, 76, 73, 70, 67, 64]):
    """
    calLetterGrade(points:float, gradescale:list = [98, 94, 91, 88, 85, 82, 79, 76, 73, 70, 67, 64])
    Calculates letter grade (points) based on number grade and the gradescale arguement (gradescale)
    The gradescale arguement should be input as a list of at most 12 numbers in decending order
    If no gradescale list is entered, the function calculates the letter grade based on the gradescale for PiE
    """
    lGrades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]
    try:
        if len(gradescale) > 12:
            print("gradescale has too many entries")
            return -1
        for i in range(0, len(gradescale)):
            if gradescale.count(gradescale[i]) > 1:
                print("gradescale has repeated entry")
                return -1
            i += 1
        #List is valid, calculate grade:
        if points < gradescale[-1]:
            return "F"
        for j in range(0, len(gradescale)):
            if points >= gradescale[j]:
                return lGrades[j]
    except:
        return -1
