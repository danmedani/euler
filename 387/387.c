#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define maxx 100000000000000
// #define maxx 10000

int isPrime(unsigned long long num) {
  if (num == 1) {
    return 0;
  }
  if ((num == 2) | (num == 3)) {
    return 1;
  }
  if ((num % 2 == 0) | (num % 3 == 0)) {
    return 0;
  }
  int i = 5;
  int del = 2;
  int lim = sqrt(num) + 1;

  while (i <= lim) {
    if (num % i == 0) {
      return 0;
    }

    i += del;
    del = 6 - del;
  }

  return 1;
}

int sumDigits(unsigned long long n) {
  int sum = 0;
  while (n > 0) {
    sum += (n % 10);
    n /= 10;
  }
  return sum;
}

int isHarshad(unsigned long long n) {
  return (n % sumDigits(n) == 0);
}

int isStrongHarshad(unsigned long long n) {
  return isHarshad(n) & isPrime(n / sumDigits(n));
}

void findSRTHPrimeSum(unsigned long long n, unsigned long long* sumSRTH) {
  if (n >= maxx) {
    return;
  }

  if (isHarshad(n) == 0) {
    return;
  }

  int newDig;
  if (isStrongHarshad(n) == 1) {
    for (newDig = 0; newDig < 10; newDig ++) {
      unsigned long long possPrime = (n * 10) + newDig;
      if (possPrime < maxx) {
        if (isPrime(possPrime) == 1) {
          *sumSRTH = *sumSRTH + possPrime;
        }
      }
    }
  }

  for (newDig = 0; newDig < 10; newDig ++) {
    findSRTHPrimeSum((n * 10) + newDig, sumSRTH);
  }
}

int main() {
  unsigned long long sumSRTH = 0;

  for (int dig = 1; dig < 10; dig ++) {
    findSRTHPrimeSum(dig, &sumSRTH);
  }

  printf(" %llu\n", sumSRTH);
  
  return 0;
}

