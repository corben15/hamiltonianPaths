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
import time
import math
import numpy as np
from grid import *

# TODO: Write code to find all start locations
# TODO: Find all hamiltonian paths

def generate_start_list(n=3):
    half_n = math.ceil(n/2)
    startList = []
    startIndex = 0
    endIndex = half_n
    rowlength = half_n
    for i in range(half_n):
        for j in range(rowlength):
            startList.append(startIndex + j)
        endIndex = endIndex + n
        rowlength -= 1
        startIndex = endIndex - rowlength
    return startList


def enumerate_all_3(startList):
    #while statement
        #check right
        #check down
        #check left
        #check up
        #make step/go back
    print()

def flip_iso(grid,n):
    candidate = np.array([i.number for i in grid.grid])
    flipCandidate = np.full(len(candidate),(n*n+1) - candidate)
    return Grid(list(flipCandidate))

def rot_90(grid,n):
    candidate = np.array([i.number for i in grid.grid])
    temp = candidate.copy()
    for i in range(len(candidate)):
        temp[i] = candidate[((n-1)*n + i//n) - n*(i%n)]
    return Grid(list(temp))

def mirror(grid,n):
    candidate = np.array([i.number for i in grid.grid])
    temp = candidate.copy()
    for i in range(0,n):
        temp[i*n:n*(i+1)] = candidate[(n*(n-i-1)):(n*(n-i))]
    return Grid(list(temp))

def enumerate_all_3_recursive(grid, path_set,previous_loc,current_loc):
    g_copy = grid.copy()

    # Set cell value
    g_copy.set_cell(g_copy.get_cell_value(previous_loc)+1, current_loc)

    # Check to see if grid is solved
    if(g_copy.is_hamiltonian()):
        if(g_copy not in path_set):
            temp = g_copy.copy()
            for i in range(4):
                path_set.add(temp)
                path_set.add(flip_iso(temp,temp.n))
                path_set.add(mirror(flip_iso(temp, temp.n),temp.n))
                path_set.add(mirror(temp, temp.n))
                temp = rot_90(temp, temp.n)
        return

    lastStep = g_copy.get_cell_value(current_loc) == g_copy.n**2 - 1
    if(not lastStep):    # check right
        if(g_copy.can_move("r", current_loc) and g_copy.get_cell_df(current_loc+1)!=0):
            #print("RIGHT")
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc+1)
        # check down
        if(g_copy.can_move("d", current_loc) and g_copy.get_cell_df(current_loc+grid.n)!=0):
            #print("DOWN")
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc+grid.n)
        #check left
        if(g_copy.can_move("l", current_loc) and g_copy.get_cell_df(current_loc-1)!=0):
            #print("LEFT")
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc-1)
        #check up
        if(g_copy.can_move("u", current_loc) and g_copy.get_cell_df(current_loc-grid.n)!=0):
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc-grid.n)

    elif(lastStep):
        # Check Right
        if(g_copy.can_move("r", current_loc)):
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc+1)
        # Check Down
        if(g_copy.can_move("d", current_loc)):
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc+grid.n)
        # Check Left
        if(g_copy.can_move("l", current_loc)):
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc-1)
        # Check Up
        if(g_copy.can_move("u", current_loc)):
            enumerate_all_3_recursive(g_copy,path_set, current_loc,current_loc-grid.n)

def compute_lcm(A):
    lcm = A[0]
    for i in A[1:]:
      lcm = lcm*i/gcd(int(lcm), i)
    return (int(lcm))

def cycle_length(P1,P2):
    P1 = list(P1)
    P2 = list(P2)
    S = set(range(1,len(P1) + 1))
    cycle_lengths = []
    while len(S)>1:
        k = 1
        min_s = min(S)
        S.remove(min_s)
        prev_ind = P1.index(min_s)
        next_num = P2[prev_ind]
        next_ind = P1.index(next_num)
        if next_num != min_s:
            S.remove(int(next_num))
        while next_num != min_s:
            prev_ind = next_ind
            next_num = P2[prev_ind]
            next_ind = P1.index(next_num)
            if next_num != min_s:
                S.remove(int(next_num))
            k += 1
        cycle_lengths.append(k)
    return(compute_lcm(cycle_lengths))

def main():

    path_set = set()

    g1 = Grid(2)
    g1.grid_print()
    print(g1.is_hamiltonian())



    print("----Start List-----")
    n = 5
    startList = generate_start_list(n)
    g_enum = Grid(n)
    g_enum.grid_print()
    print("DF grid")
    g_enum.grid_print_df()

    print("-----enumerate-------")
    start = time.time()
    for i in range(len(startList)):
        enumerate_all_3_recursive(g_enum, path_set,startList[i], startList[i])
    end = time.time()
    print("Enumerating took:", end-start)

    print()
    print("---------------------")
    print("Result Set")
    print(len(path_set))

    '''
    for h in path_set:
        print()
        h.grid_print()
    '''





if __name__ == '__main__':
    main()
