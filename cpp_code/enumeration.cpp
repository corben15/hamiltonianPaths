#include <iostream>
#include <stdlib.h>
#include <vector>
#include <set>
#include <ctime>
#include <cmath>
#include <ctime>
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

int gcd(int a, int b) {
   if (b == 0)
   return a;
   return gcd(b, a % b);
}

size_t computeLCM0fArray();

size_t cycleLength(Grid g1, Grid g2){
  //TODO
}

//TODO
void enumerateAllRecursive(Grid g, set<Grid> pathSet, int prevLoc, int currentLoc){
  cout << "Hi"<< endl;

  // Take step/Set cell

  // Check if the grid is solved

  // Step right

  // Step down

  // Step Left

  // Step up
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
