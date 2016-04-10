#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void setBit(int *bits, int index) {
  int i = index / 32;
  int pos = index % 32;

  unsigned int flag = 1;
  flag = flag << pos;

  bits[i] |= flag;
}

void clearBit(int *bits, int index) {
  int i = index / 32;
  int pos = index % 32;

  unsigned int flag = 1;
  flag = ~(flag << pos);

  bits[i] &= flag;
}

int isBitSet(int *bits, int index) {
  int i = index / 32;
  int pos = index % 32;

  unsigned int flag = 1; // 000 ... 001
  flag = flag << pos;

  if (bits[i] & flag) {
    return 1;
  } else {
    return 0;
  }
}

void genPrimeMap(int numPrimes, int *primes) {
  // primes[0] = 0;
  // primes[1] = 0;
  setBit(primes, 0);
  setBit(primes, 1);

  int i,j;

  for (i = 2; i < numPrimes; i ++) {
    // primes[i] = 1;
    setBit(primes, i);
  }

  for (i = 2; i < numPrimes; i++) {
    // if (primes[i] == 1) {
    if (isBitSet(primes, i) == 1) {
      j = i * 2;
      while (j < numPrimes) {
        // primes[j] = 0;
        clearBit(primes, j);
        j = j + i;
      }
    }
  }
}

void genGenMap(int numPrimes, int *gen, int *primes) {
  int i;

  // gen[0] = 0;
  clearBit(gen, 0);
  for (i = 1; i < numPrimes; i ++) {
    // gen[i] = 1;
    setBit(gen, i);
  }

  int sumPrimes = 0;
  int div1, halfway;
  for (i = 2; i < numPrimes; i ++) {
    // if (primes[i] == 0) {
    if (isBitSet(primes, i) == 0) {
      halfway = (i - 1) / 2;
      for (div1 = i - 1; div1 > halfway; div1 --) {
        if ((div1 * (i - div1)) >= numPrimes) {
          break;
        }

        // gen[div1 * (i - div1)] = 0;
        clearBit(gen, div1 * (i - div1));
      }
    }
  }

}

int main() {
  int numPrimes = 100000000;

  int *primes;
  primes = (int *) malloc(sizeof(int)*(numPrimes / 32));

  genPrimeMap(numPrimes, primes);

  int *gen;
  gen = (int *) malloc(sizeof(int)*numPrimes);

  genGenMap(numPrimes, gen, primes);

  unsigned long long sumGend = 0;
  for (int i = 0; i < numPrimes; i ++) {
    // if (gen[i] == 1) {
    if (isBitSet(gen, i) == 1) {
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
