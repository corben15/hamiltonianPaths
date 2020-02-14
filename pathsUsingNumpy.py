'''
author: Nicholas Corbett & Andrew (Bud) Fucarino

Problem Definition:
    Find a maximum translation cycle so that when you translate a hamiltonian
    path you get another hamiltonian pathself.

    ex:
    A solution for the 3x3 is below. The cycle size is 20 which is received by
    finding the lowest common multiple of the  of the sides of the arrayself.

    3*3 = 9 ==> 4+5 = 9 ==> 4*5 = 20

        [1,4,5                              [9,2,3
         2,3,6      ==Translates to ==>      8,1,4
         9,8,7]                              7,6,5]
'''

import numpy as np;


def isSquareArray(array):
    arrayShape = array.shape
    return arrayShape[0] == arrayShape[1]

def findMinValueLocation(array):
    arrayShape = array.shape;
    minLocation = [0,0];
    minValue = array[0][0];
    for i in range(arrayShape[0]):
        for j in range(arrayShape[1]):
            if(array[i][j] <= minValue):
                minValue = array[i][j];
                minLocation = [i,j];
    return minValue;
