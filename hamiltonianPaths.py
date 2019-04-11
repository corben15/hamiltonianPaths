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
    assert isSquareArray(array)

    l = arrayShape[0]

    print(array)
    print
    print("Array Shape: ", arrayShape)

    for i in range(l):
        for j in range(l):
            print("Position:",i,j, "Value:", array[i][j])
            print("Right:")
            if(array[i][j+1] != (array[i][j] + 1) or array[i][j-1] != (array[i][j] - 1)):
                return False;
            if(array[i+1][j] != (array[i][j] + 1) or array[i-1][j] != (array[i][j] - 1)):
                return False;
    return True;



if __name__ == '__main__':

    myArray = np.array([[1,2,3],[6,5,4],[7,8,9]])
    print(myArray[0][0])

    print(checkIsHamiltonianPath(myArray))
