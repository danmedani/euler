#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

uint64_t powMod(uint64_t a, uint64_t b, uint64_t mod) {
  printf("powMod (%llu, %llu)\n", a, b);
  uint64_t result = a;
  while (b > 1) {
    result = (result * a) % mod;
    b = b - 1;
  }
  return result;
}

uint64_t dubsMod(uint64_t a, uint64_t b, uint64_t mod) {
  printf("dubsmod (%llu, %llu)\n", a, b);
  if (b == 1) {
    return a % mod;
  }
  else {
    return powMod(a, dubsMod(a, b - 1, mod) % mod, mod);
  }
}

int main() {
  printf("%llu\n", dubsMod(1777, 1855, 100000000));
  return 0;
}
