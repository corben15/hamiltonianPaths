#include <iostream>
#include <stdlib.h>
#include <vector>
#include <set>
#include <ctime>
#include <cmath>
#include <ctime>m
#include "grid.h"


using namespace std;

vector<int> generateStartList(int n){

  vector<int> startVector;
  int halfN = ceil(float(n)/2);

  int startIndex = 0;
  int endIndex = halfN;
  int rowlength = halfN;

  for(int i=0; i<halfN; i++){
    for(int j=0; j<rowlength; j++ ){
      startVector.push_back(startIndex + j);
    }
    endIndex = endIndex + n;
    rowlength -= 1;
    startIndex = endIndex - rowlength;
  }
  return startVector;
}

void enumerateAllRecursive(Grid g, set<Grid> pathSet, int prevLoc, int currentLoc){
  cout << "TODO" << endl;
}

int main(){

  int n=3;
  cout << "Enter a grid Size: " << endl;
  cin >> n;
  cout << endl;

  vector<int> v = generateStartList(n);
  for(int i=0; i<v.size(); i++){
    cout << v[i] << endl;
  }
}
