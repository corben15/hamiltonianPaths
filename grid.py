
# Todo: enumerate all 3x3
# TODO: Enumerates nxn
# TODO: input 2 graphs output cycle lengths
# TODO: 3x3 and 4x4 tabulare cycle length
# Todo: Check if path is cut off

import copy
import math

class Cell:
    def __init__(self, number=0, df=4):
        # number is the number in that cell of the grid
        # df is the degrees of freedom that the point has for its next move (max=4, min=0)
        # if df is negative then it hasn't been initialized
        self.number = number
        self.df = df

    def __hash__(self):
        return hash((self.number, self.df))

    def __eq__(self, other):
        return self.number == other.number and self.df == self.df

    def get_value(self):
        return self.number

    def get_df(self):
        return self.df


class Grid:

    def __init__(self, *args):
        # Initialize from List
        if(type(args[0])== list):
            gridList = args[0]
            n = int(math.sqrt(len(gridList)))
            self.n = n
            self.cellCount = len(gridList)
            self.grid = []
            for i in range(len(gridList)):
                self.grid.append(Cell(gridList[i]))

        # Initialize from integer
        elif(type(args[0]==int)):
            n = args[0]
            self.n = n
            self.cellCount = n**2
            self.grid = []
            row=0
            for i in range(self.cellCount):
                self.grid.append(Cell())
                if(i >= n and i%n==0): row +=1
                if(row == 0 or row == n-1):
                    if(i%n == 0 or i%n==n-1):
                        self.grid[i].df = 2
                    else:
                        self.grid[i].df = 3
                else:
                    if(i%n == 0 or i%n==n-1):
                        self.grid[i].df = 3
                    else:
                        self.grid[i].df = 4
    def __hash__(self):
        return hash(tuple([i.number for i in self.grid]))

    def __eq__(self, other):
        return tuple([i.number for i in self.grid])==tuple([i.number for i in other.grid])

    def grid_print(self):
        maxNumber = self.cellCount
        maxNumberString = str(maxNumber)

        row = ""
        for i in range(len(self.grid)):
            row += "  "+" "*(len(maxNumberString)-len(str(self.grid[i].number))) + str(self.grid[i].number)
            if(i%self.n==self.n-1):
                print(row)
                row = ""

    def grid_print_df(self):
        maxNumber = self.cellCount
        maxNumberString = str(maxNumber)

        row = ""
        for i in range(len(self.grid)):
            row += "  "+" "*(len(maxNumberString)-len(str(self.grid[i].df))) + str(self.grid[i].df)
            if(i%self.n==self.n-1):
                print(row)
                row = ""

    def set_cell(self,val,row,col=None):
        if(col == None and row != None):
            index = row
        else:
            index = row*self.n + col
            if(row > 0):
                self.grid
        if(index > self.n**2 - 1): return
        self.grid[index].number = val

        # Set degrees of freedom for neighbors
        n = self.n
        self.grid[index].df = 0
        # Left Column
        if(index%n == 0):

            if(index == 0):
                if(self.grid[index+1].df > 0):
                    self.grid[index+1].df -= 1
                if(self.grid[index+n].df > 0):
                    self.grid[index+n].df -= 1
            elif(index == n*(n-1)):
                if(self.grid[index+1].df > 0):
                    self.grid[index+1].df -= 1
                if(self.grid[index-n].df > 0):
                    self.grid[index-n].df -= 1
            elif(index > 0 and index < n*(n-1)):
                if(self.grid[index-n].df > 0):
                    self.grid[index-n].df -= 1
                if(self.grid[index+1].df > 0):
                    self.grid[index+1].df -= 1
                if(self.grid[index+n].df > 0):
                    self.grid[index+n].df -= 1
        # Right Column
        elif(index%n == n-1):

            if(index == n-1):
                if(self.grid[index-1].df > 0):
                    self.grid[index-1].df -= 1
                if(self.grid[index+n].df > 0):
                    self.grid[index+n].df -= 1
            elif(index == (n**2)-1):
                if(self.grid[index-1].df > 0):
                    self.grid[index-1].df -= 1
                if(self.grid[index-n].df > 0):
                    self.grid[index-n].df -= 1
            elif(index > 0 and index<(n**2)-1 ):
                if(self.grid[index-n].df > 0):
                    self.grid[index-n].df -= 1
                if(self.grid[index-1].df > 0):
                    self.grid[index-1].df -= 1
                if(self.grid[index+n].df > 0):
                    self.grid[index+n].df -= 1
        # Middle Columns
        elif(index%n>0 and index%n<n-1):
            if(index>0 and index<n-1):
                if(self.grid[index-1].df > 0):
                    self.grid[index-1].df -= 1
                if(self.grid[index+n].df > 0):
                    self.grid[index+n].df -= 1
                if(self.grid[index+1].df > 0):
                    self.grid[index+1].df -= 1
            elif(index>n*(n-1) and index<(n**2)-1):
                if(self.grid[index-1].df > 0):
                    self.grid[index-1].df -= 1
                if(self.grid[index-n].df > 0):
                    self.grid[index-n].df -= 1
                if(self.grid[index+1].df > 0):
                    self.grid[index+1].df -= 1
            elif(index>n and index<n*(n-1) ):
                if(self.grid[index-n].df > 0):
                    self.grid[index-n].df -= 1
                if(self.grid[index-1].df > 0):
                    self.grid[index-1].df -= 1
                if(self.grid[index+n].df > 0):
                    self.grid[index+n].df -= 1
                if(self.grid[index+1].df > 0):
                    self.grid[index+1].df -= 1

    def is_hamiltonian(self):
        n = self.n
        for i in range(int(len(self.grid))):
            count = 0
            if (i%n) != 0:
                if abs(self.grid[i-1].number - self.grid[i].number) == 1:
                    count += 1
            if (i%n) != (n-1):
                if abs(self.grid[i].number - self.grid[i+1].number) == 1:
                    count += 1
            if (i//n) > 0:
                if abs(self.grid[i].number - self.grid[i-n].number) == 1:
                    count += 1
            if (i//n) < (n-1):
                if abs(self.grid[i].number - self.grid[i+n].number) == 1:
                    count += 1
            if (self.grid[i].number == 1) or (self.grid[i].number == n*n):
                if count != 1:
                    return False
            elif count != 2:
                return False
        return True

    def get_cell_value(self,c):
        # Make sure c is a valid location in the grid
        if(c<0):
            return None
        elif(c>self.n**2 - 1):
            return None
        return self.grid[c].get_value()

    def get_cell_df(self,c):
        # make sure c is a valid loaction in the grid
        if(c<0):
            return None
        elif(c>self.n**2 - 1):
            return None
        return self.grid[c].get_df()

    def can_move(self, move, current_loc):
        if(move == 'r'):
            if((current_loc+1)%self.n != 0):
                return True
        elif(move == 'd'):
            if((current_loc+self.n) < self.n**2):
                return True
        elif(move == 'l'):
            if((current_loc-1)%self.n != self.n-1):
                return True
        elif(move == 'u'):
            if((current_loc-self.n) > 0):
                return True
        return False

    def copy(self):
        return copy.deepcopy(self)









#end
