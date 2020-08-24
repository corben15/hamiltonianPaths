#include <iostream>
#include <stdlib.h>
#include <vector>
#include <set>
#include <ctime>
#include <cmath>
#include <ctime>
#include "grid.h"


using namespace std;


void cell_constructor_test(){
  cout << "Cell Contrunctor Test" << endl;
  Cell test_cell(3,4);
}

void cell_outstream_test(){
  cout << "Cell Outstream Test" << endl;
  Cell c(3,4);
  cout << c << endl;
}


void grid_constructor_test(){
  cout << "Grid Constructor Test" << endl;
}

int main(){

  // Cell Class Tests
  cout << "Cell Class Tests:\n" << endl;
  cell_constructor_test();
  cell_outstream_test();

  cout << "\n" << endl;

  // Grid Class Tests
  cout << "Grid Class Tests:\n" << endl;

  cout << "\n" << endl;

}
