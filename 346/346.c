#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int getDecimalVal(int numOnes, int base) {
  int retVal = 0;

  int exponent = numOnes - 1;
  while (exponent >= 0) {
    retVal += pow(base, exponent);

    exponent --;
  }

  return retVal;
}


int main() {
  int numOnes = 1;

  // while (numOnes < 4) {
  //   for (int base = 2; base < 8; base ++) {
  //     printf("%i\n", getDecimalVal(numOnes, base));
  //   }

  //   numOnes ++;
  // }

  printf("%i\n", getDecimalVal(2, 6)); 
  
  return 0;
}

