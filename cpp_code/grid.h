#ifndef GRID_H
#define GRID_H

#include <iostream>
#include <stdlib.h>
#include <ctime>
#include "cell.h"

class Grid{
  private:
    size_t n_;
    size_t cellCount_;
    std::vector<Cell> v_;

    // Private memnber functions
    void copy(const Grid &g);

  public:

    // Constructor, Assignment Operator, Destructor
    Grid(size_t n){
      n_ = n;
      cellCount_ = n*n;
      for(int i=0; i<cellCount_; i++){
        Cell c(i);
        v_.push_back(c);
      }
    }
    // TODO
    //Grid(std::vector<Cell> v)

    Grid(const Grid &g){this->copy(g);}
    //~Grid();

    size_t get_n(){return n_;}
    size_t get_cell_value(int c);
    size_t get_cell_df(int c);

    //void set_cell(size_t val, size_t row, size_t col=0);
    //bool can_move(std::string move, size_t currentLoc);
    //bool is_hamiltonian();
    //Grid flip_iso();
    //Grid rot90();
    //Grid mirror();


};

void Grid::copy(const Grid &g){
  n_ = g.n_;
  cellCount_ = g.cellCount_;
  v_ = g.v_;
}

size_t Grid::get_cell_value(int c){
  return v_[c].get_value();
}

size_t Grid::get_cell_df(int c){
  return v_[c].get_df();
}

/*
void Grid::set_cell(size_t val, size_t row, size_t col){
  //TODO
}

bool Grid::can_move(std::string move, size_t currentLoc){
  //TODO
}

bool Grid::is_hamiltonian(){
  //TODO
}

Grid Grid::flip_iso(){
  //Todo
}

Grid Grid::rot90(){
  //TODO
}

Grid Grid::mirror(){
  //TODO
}
*/

/* TODO
std::ostream& operator<< (std::ostream& ostr, Grid const& g){
  std::string stringToPrint;
  for(int i=0; i<=g.v_.size(); i++){
    if(i%g.get_n() == g.get_n()-1){
      stringToPrint +=
    }
    else{

    }
  }
  ostr << ;
  return ostr;
}
*/


#endif // GRID_H
