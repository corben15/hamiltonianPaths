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

import math
from grid import *


""" Checks to see if a matrix is a hamiltonian path. Matrix is represented as a list
args: list P
return: bool
"""
def is_hamiltonian(P):
    good = True
    n = int(math.sqrt(len(P)))

    for i in range(len(P)):
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

""" Enumerates all the hamiltonian paths for and nxn matrix (iteratively)
    1. Only check small upper triangle for starting point of path
    2. Check if you divide Path:
       3x3 example:
       _ are the not yet visited nodes/points
            1,_,_
            2,3,_
            _,4,_
    3. End point degree of freedoms
    4. Symmetry: Test if turns are equal 4 way rotation, more right or more left
        then it only has 2 way symmetry
"""
def enumerate_all_paths_iterative(n):
    print()

""" Enumerates all the hamiltonian paths for and nxn matrix (recursively)
"""
def enumerate_all_paths_recursive(n):
    print()


if __name__ == '__main__':

    lcm_dict = { 3: [4,5],
                 4: [4,5,7],
                 5: [4,5,7,9],
                 6: [4,5,7,9,11],
                 7: [4,5,7,9,11,13],
                 8: [3,5,7,8,11,13,17],
                 9: [1,1,3,4,5,7,11,13,17,19]}






    # UNIT TEST FOR is_hamiltonian
    list_3_3_correct = [1,2,3,6,5,4,7,8,9]
    list_3_3_incorrect = [1,2,3,4,5,6,7,8,9]

    list_4_4_correct = [1,2,3,4,8,7,6,5,9,10,11,12,16,15,14,13]
    list_4_4_incorrect = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


    print(is_hamiltonian(list_3_3_correct))
    print(is_hamiltonian(list_3_3_incorrect))

    print(is_hamiltonian(list_4_4_correct))
    print(is_hamiltonian(list_4_4_incorrect))
    print(is_hamiltonian([1,4,0,3]))
