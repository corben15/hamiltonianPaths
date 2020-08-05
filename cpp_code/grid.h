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
    size_t n;
    size_t cellCount;
    std::vector<Cell> v;

    // Private memnber functions
    void copy(const Grid &g);

  public:

    // Constructor, Assignment Operator, Destructor
    Grid(size_t n);
    Grid(const Grid &g);
    ~Grid();

};


Grid flipIso();
Grid rot90();
Grid mirror();
size_t cycleLenth();
int gcd(int a, int b) {
   if (b == 0)
   return a;
   return gcd(b, a % b);
}
size_t computeLCM0fArray();




#endif // GRID_H
