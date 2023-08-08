use prime_tools;
use std::collections::HashSet;

fn main() {
  let primes = prime_tools::get_primes_less_than_x(100_000_000);
  let mut prime_squares: HashSet<u64> = HashSet::new();
  
  for prime in &primes {
    let prime_squared: u64 = *prime as u64 * *prime as u64;
    if !is_palin(prime_squared) {
      prime_squares.insert(prime_squared);
    }
  }
  let mut sum_rev_prime_squares: u64 = 0;
  let mut the_count = 0;
  for prime in &primes {
    let prime_squared: u64 = *prime as u64 * *prime as u64;
    if prime_squares.contains(&reverse_number(prime_squared)) {
      sum_rev_prime_squares += prime_squared;
      the_count += 1;
      println!("got 1 {} {} {} {} {}", prime, prime_squared, reverse_number(prime_squared), the_count, sum_rev_prime_squares);
      if the_count > 49 {
        break;
      }
    }
  }

}

fn reverse_number(n: u64) -> u64 {
  let mut reversed = 0;
  let mut x = n;
  while x > 0 {
      reversed = reversed * 10 + x % 10;
      x /= 10;
  }
  reversed
}

fn is_palin(mum: u64) -> bool {
  let mut high_exp = 1;
  let low_exp = 10;
  while high_exp < mum {
    high_exp = high_exp * 10;
  }
  high_exp = high_exp / 10;
 
  let mut num = mum;
  while high_exp > 2 {
    if (num % low_exp) != (num / high_exp) {
      return false;
    }

    num = num - ((num / high_exp) * high_exp);
    num = num / 10;

    high_exp = high_exp / 100;
  }

  return true;
}

