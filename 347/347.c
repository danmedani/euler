#include <stdio.h>
#include <stdlib.h>
#include <math.h>

const int max_prime = 10000000;

void genPrimeMap(int maxPrime, int *primes, int* numPrimes) {
  primes[0] = 0;
  primes[1] = 0;

  int i,j;

  *numPrimes = maxPrime - 2;

  for (i = 2; i < maxPrime; i ++) {
    primes[i] = 1;
  }

  for (i = 2; i < maxPrime; i++) {
    if (primes[i] == 1) {
      j = i * 2;
      while (j < maxPrime) {
        if (primes[j] == 1) {
          primes[j] = 0;
          *numPrimes = *numPrimes - 1;
        }
        
        j = j + i;
      }
    }
  }
}

void genPrimeList(int **primes, int maxPrime, int* numPrimes) {
  int* primeMap = (int*) malloc(sizeof(int) * maxPrime);

  genPrimeMap(maxPrime, primeMap, numPrimes);

  *primes = NULL;
  *primes = (int*) malloc(sizeof(int) * *numPrimes);

  int primeI = 0;

  for (int i = 0; i < maxPrime; i ++) {
    if (primeMap[i] == 1) {
      (*primes)[primeI] = i;
      primeI ++;
    }
  }
  
} 

unsigned long long getM(unsigned long long p, unsigned long long q, unsigned long long n) {
 
  unsigned long long sqrtN = sqrt(n) + 1;
  unsigned long long maxPPow = (log(n) / log(p));
  unsigned long long maxQPow = (log(n) / log(q)); 

  // printf("maxPPow %llu\n", maxPPow);
  // printf("maxQPow %llu\n", maxQPow);

  unsigned long long largestP = pow(p, maxPPow);
  unsigned long long largestQ = pow(q, maxQPow);

  // printf("largestP %llu\n", largestP);
  // printf("largestQ %llu\n", largestQ);

  unsigned long long largest = 0;
  unsigned long long pPart = p;
  unsigned long long val;
  while (pPart <= n) {
    unsigned long long qPart = q;
    while (qPart <= n) {
      if ((pPart > sqrtN) & (qPart > sqrtN)) {
        break;
      }
      
      val = pPart * qPart;
      if (val > n) {
        break;
      }
      if (val > largest) {
        largest = val;
      }

      qPart *= q;
    }
    pPart *= p;
  }

  return largest;
}

unsigned long long getS(unsigned long long n, int *primes, int primesLength) {
  unsigned long long sumUnique = 0;
  unsigned long long m;

  for (int pI = 0; pI < primesLength; pI ++) {
    for (int qI = pI+1; qI < primesLength; qI ++) {
      unsigned long long primeA = primes[pI];
      unsigned long long primeB = primes[qI];
      unsigned long long primeMult = primeA * primeB;
      if (primeMult > n) {
        break;
      }

      m = getM(primes[pI], primes[qI], n);
      if (m > 0) {
        sumUnique = sumUnique + m;
      }
    }

    if (primes[pI] > n) {
      break;
    }
  }

  return sumUnique;
}

int main() {

  int* primes;
  int numPrimes = 0;

  genPrimeList(&primes, max_prime, &numPrimes);

  unsigned long long s = getS(10000000, primes, numPrimes);

  printf("%llu\n", s);

  return 0;
}
