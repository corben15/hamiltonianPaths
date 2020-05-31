#ifndef GRID_H
#define GRID_H

#include <iostream>
#include <stdlib.h>
#include <ctime>



class Cell{
  private:
    int value;
    int df;

  public:
    void set_cell(int new_value){
      value = new_value;
    }
    int get_df(){
      return df;
    }

};

class Grid{
  private:
    int n;
    int cellCount;
    std::vector<Cell> v;

  public:

}


#endif // GRID_H
