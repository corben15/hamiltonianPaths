#ifndef GRID_H
#define GRID_H

#include <iostream>
#include <stdlib.h>
#include <ctime>
#include "cell.h"
#include <math.h>


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
      int row = 0;
      int val=0;
      int df;
      for(int i=0; i<cellCount_; i++){
        if(i >= n && i%n==0){
          row +=1;
        }
        if(row == 0 || row == n-1){
          if(i%n == 0 || i%n==n-1){
            df = 2;
          }
          else{
            df = 3;
          }
        }
        else{
          if(i%n == 0 || i%n==n-1){
            df = 3;
          }
          else{
            df = 4;
          }
        }
        Cell c(val,df);
        v_.push_back(c);
      }
    }

    Grid(std::vector<int> v){
      n_ = sqrt(v.size());
      cellCount_ = v.size()*v.size();

      for(int i=0; i<v.size(); i++){
        Cell c(v[i],0);
        v_.push_back(c);
      }
    }

    Grid(const Grid &g){this->copy(g);}
    //~Grid();

    size_t get_n(){return n_;}
    size_t get_cell_value(int c);
    size_t get_cell_df(int c);

    void set_cell(size_t val, size_t *row, size_t *col);
    //bool can_move(std::string move, size_t currentLoc);
    //bool is_hamiltonian();
    //Grid flip_iso();
    //Grid rot90();
    //Grid mirror();

    void print_values();
    void print_df();
    Cell& operator[](int index);



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


void Grid::set_cell(size_t val, size_t *row, size_t *col){
  // Get index of cell to set
  if(col == NULL && row != NULL){
    size_t index = *row;
  }
  else{
    size_t index = *row * n_ + *col;
  }
  /*
  if(index > n_*n_-1){
    std::cout << "Index for setting cell is out of range" << std::endl;
    return;
  }

  */

  // Set the cell to the value and the degrees of freedom to 0
  //this->v_[index].set_cell(val);
  //this->v_[index].set_df(0);

  // Set the degree of freedom for the neighbors

}

/*
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

void Grid::print_values(){
  std::string cellCountString = std::to_string(cellCount_);
  int valueMaxLen = cellCountString.length();
  std::string stringToPrint;
  std::cout << n_ << std::endl;

  for(int i=0; i<n_*n_; i++){
    stringToPrint += std::to_string(this->v_[i].get_value());
    stringToPrint += " ";
    if(i%n_==n_-1){
      stringToPrint += "\n";
    }
  }
  std::cout << stringToPrint << std::endl;
}

void Grid::print_df(){
  std::string stringToPrint;

  for(int i=0; i<n_*n_; i++){
    stringToPrint += std::to_string(this->v_[i].get_df());
    stringToPrint += " ";
    if(i%n_==n_-1){
      stringToPrint += "\n";
    }
  }
  std::cout << stringToPrint << std::endl;
}

Cell& Grid::operator[](int index){
  return this->v_[index];
}

/*
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
