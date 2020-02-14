


class Cell:
    def __init__(self, number=0, df=-1):
        # number is the number in that cell of the grid
        # df is the degrees of freedom that the point has for its next move (max=4, min=0)
        # if df is negative then it hasn't been initialized
        self.number = number
        self.df = df


class Grid:
    def __init__(self,n=3):
        self.n = n
        c = n*n
        self.grid = [Cell()]*c


    def grid_print(self):
        grid=[]
        row = [0]*self.n
        for i in range(len(self.grid)):
            row[i%self.n] = self.grid[i].number
            if(i%self.n==self.n-1):
                grid.append(row)
                print(row)
        
