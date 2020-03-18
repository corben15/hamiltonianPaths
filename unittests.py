import unittest
import random
from grid import *


class TestGridMethods(unittest.TestCase):
    # Test the initialization of the grid is working correctly
    def test_grid_init_int(self):
        print()
        gridSize = random.randint(2,10)
        grid = Grid(gridSize)
        #grid.grid_print()
        #grid.grif_print_df()

    def test_grid_init_list(self):
        print()
        gridSize = random.randint(2,10)
        gridList = list(range(1,gridSize**2+1))
        grid = Grid(gridList)
        #grid.grid_print()
        #grid.grif_print_df()

    # Tests the cells in the grid are set to the correct value
    def test_set_cell_value(self):
        print()
        #print("Set Cell Value Test")
        gridSize = random.randint(2,10)
        grid1 = Grid(gridSize)

        # Set cells by Row and Column
        for i in range(grid1.n):
            for j in range(grid1.n):
                grid1.set_cell(i*grid1.n+j,i,j)

        # Set cells by index
        grid2 = Grid(gridSize)
        for i in range(grid2.cellCount):
            grid2.set_cell(i,i)
        assert(grid1.grid[grid1.cellCount-1].number == grid2.grid[grid2.cellCount-1].number)

    def test_set_cell_df(self):
        print()
        grid4 = Grid(4)

        # Test Upper Left
        grid4.set_cell(1,0)
        assert(grid4.grid[0].number == 1)
        assert(grid4.grid[0].df == 0)

        # Test Upper Middle
        grid4.set_cell(3,2)
        assert(grid4.grid[2].number == 3)
        assert(grid4.grid[2].df == 0)


        # Test Upper Right
        grid4.set_cell(4,3)
        assert(grid4.grid[3].number == 4)
        assert(grid4.grid[3].df == 0)

        # Test Middle Left
        grid4.set_cell(5,4)
        assert(grid4.grid[4].number == 5)
        assert(grid4.grid[4].df == 0)


        # Test Middle Middle
        grid4.set_cell(6,5)
        assert(grid4.grid[5].number == 6)
        assert(grid4.grid[5].df == 0)

        # Test Middle Right
        grid4.set_cell(8,7)
        assert(grid4.grid[7].number == 8)
        assert(grid4.grid[7].df == 0)


        # Test Bottom Left
        grid4.set_cell(13,12)
        assert(grid4.grid[12].number == 13)
        assert(grid4.grid[12].df == 0)


        # Test Bottom Middle
        grid4.set_cell(15,14)
        assert(grid4.grid[14].number == 15)
        assert(grid4.grid[14].df == 0)

        # Test Bottom Right
        grid4.set_cell(16,15)
        assert(grid4.grid[15].number == 16)
        assert(grid4.grid[15].df == 0)

    def test_is_hamiltonian(self):
        print()
        # Test "S" shape
        list_3_correct = [1,2,3,6,5,4,7,8,9]
        list_3_incorrect = [1,2,3,4,5,6,7,8,9]

        grid_3_correct = Grid(list_3_correct)
        grid_3_incorrect = Grid(list_3_incorrect)
        assert(grid_3_correct.is_hamiltonian() == True)
        assert(grid_3_incorrect.is_hamiltonian() == False)

        # Test "Spiral" shape
        grid_3_spiral = Grid([5,4,3,6,1,2,7,8,9])
        assert(grid_3_spiral.is_hamiltonian() == True)
        # Test "Dog Leg" shape
        grid_3_dogleg = Grid([1,2,9,4,3,8,5,6,7])
        assert(grid_3_dogleg.is_hamiltonian() == True)










if __name__ == '__main__':
    print()
    unittest.main()
