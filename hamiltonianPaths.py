'''
author: Nicholas Corbett

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

import math
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

'''A hamiltonian path is a path in a grid is a path that visits each node exactly once
    and in this case visits them in increasing order. Examples of a grid in which a hamiltonian
    path exists for 3x3 matrices are:
    [1,2,3          and         [5,4,3
     6,5,4                       6,1,2
     7,8,9]                      7,8,9]

    This function will determine if any matix has a hamiltonian path given it is a square matrix.
'''
def checkIsHamiltonianPath(array):
    arrayShape = array.shape
    #assert isSquareArray(array)
    length = arrayShape[0]
    numElements = length**2
    print(array)
    print(array[1][2])

    # for each element in the matrix there must be exactly two adjacent numbers
    # except for the start and end points which should have one adjacent number
    for i in range(l**2):
        count = 0;
        row = i//l
        col = i%l
        if(row == 0): #you are in the top row of the matrix
            if(col =0):
                print
            if(col = l-1);
                print
        
        elif(i%l == l-1):
            print
    return True;

""" Checks to see if a matrix is a hamiltonian path. Matrix is represented as a list
args: list P
return: bool
"""
def buds_is_hamiltonian(P):
    good = True
    n = int(math.sqrt(len(P)))
    for i in range(n):
        count = 0
        if (i%n) != 0:
            if abs(P[i-1] - P[i]) == 1:
                count += 1
        if (i%n) != (n-1):
            if abs(P[i] - P[i+1]) == 1:
                count += 1
        if (i//n) > 0:
            if abs(P[i] - P[i-n]) == 1:
                count += 1
        if (i//n) < (n-1):
            if abs(P[i] - P[i+n]) == 1:
                count += 1
        if (P[i] == 1) or (P[i] == n*n):
            if count != 1:
                return False
        elif count != 2:
            return False
    return good

if __name__ == '__main__':

    myArray = np.array([[1,2,3],[6,5,4],[7,8,9]])
    myList = [1,2,3,6,5,4,7,8,9]
    print(myArray[0][0])
    print(0%3)
    print(buds_is_hamiltonian(myList))

    #print(checkIsHamiltonianPath(myArray))
