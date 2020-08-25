#ifndef CELL_H
#define CELL_H

#include <iostream>
#include <stdlib.h>
#include <ctime>



class Cell{
  private:
    int value_;
    int df_;

    void create(size_t , size_t df);
    void copy( const Cell &c);

  public:
    friend class Grid;
    // Constructor, Destructor, Assignment Operator
    Cell(size_t n=0, size_t df=4){ this -> create(n,df);}
    Cell(const Cell &c){copy(c);}
    //~Cell();

    Cell& operator=(Cell const& rhs);

    void set_cell(int new_value){
      value_ = new_value;
    }
    int get_df() const{
      return df_;
    }
    int get_value() const{
      return value_;
    }

};

void Cell::create(size_t n, size_t df){
  value_ = n;
  df_ = df;
}

void Cell::copy(const Cell &c){
  value_ = c.value_;
  df_ = c.df_;
}

Cell& Cell::operator=(Cell const& rhs) {
  this->copy(rhs);
  return *this;
}

std::ostream& operator<< (std::ostream& ostr, Cell const& c){
  ostr << "Value: " << c.get_value() << " Df: " << c.get_df();
  return ostr;
}


#endif // CELL_H
