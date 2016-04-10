#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void genPrimeMap(int numPrimes, short *primes) {
  primes[0] = 0;
  primes[1] = 0;

  int i,j;

  for (i = 2; i < numPrimes; i ++) {
    primes[i] = 1;
  }

  for (i = 2; i < numPrimes; i++) {
    if (primes[i] == 1) {
      j = i * 2;
      while (j < numPrimes) {
        primes[j] = 0;
        j = j + i;
      }
    }
  }
}

void genGenMap(int numPrimes, short *gen, short *primes) {
  int i;

  gen[0] = 0;
  for (i = 1; i < numPrimes; i ++) {
    gen[i] = 1;
  }

  int sumPrimes = 0;
  int div1, halfway;
  for (i = 2; i < numPrimes; i ++) {
    if (primes[i] == 0) {
      halfway = (i - 1) / 2;
      for (div1 = i - 1; div1 > halfway; div1 --) {
        if ((div1 * (i - div1)) >= numPrimes) {
          break;
        }
        // printf("gen i  %i   %i\n", i, div1 * (i - div1));
        gen[div1 * (i - div1)] = 0;
      }
    }
  }

}

int main() {
  int numPrimes = 100000000;

  short *primes;
  primes = (short *) malloc(sizeof(short)*numPrimes);

  genPrimeMap(numPrimes, primes);

  short *gen;
  gen = (short *) malloc(sizeof(short)*numPrimes);

  genGenMap(numPrimes, gen, primes);

  unsigned long long sumGend = 0;
  for (int i = 0; i < numPrimes; i ++) {
    if (gen[i] == 1) {
      sumGend += i;
    }
  }

  printf("sumGend %llu\n", sumGend);

  free(primes);
  primes = NULL;
  free(gen);
  gen = NULL;

  return 0;
}
