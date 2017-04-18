extern crate bit_vec;

use bit_vec::BitVec;

fn main() {
	let max_num = 100000000;
	
	let prime_map = get_prime_map(max_num);
	let primes = get_primes(&prime_map, max_num);
	println!("len primes == {}", primes.len());

	let mut s:u64 = 0;
	for i in 2.. 1 + max_num as i32 {
		if i % 1000000 == 0 {
			println!("{} %", i);
		}
		let phi_i = phi(i, &get_prime_factors(i, &primes, &prime_map, max_num));
		s = s + (i - phi_i) as u64;
	}
	println!("ans = {}", s * 6);
}

fn get_prime_factors(n: i32, primes: &Vec<i32>, prime_map: &BitVec, max_num: usize) -> Vec<i32> {
	let mut x = n;
	let mut factors = Vec::new();
	let mut i:usize = 0;
	while !prime_map[x as usize] && x > 1 {
		while i < max_num {	
			if x % primes[i] == 0 {
				factors.push(primes[i]);
		        while x % primes[i] == 0 {
		        	x /= primes[i];
		        }
		        i += 1;
		        break;
			}
			i += 1;
		}
	}
	if x > 1 {
		factors.push(x);	
	}
	factors
}

fn get_prime_map(max_num: usize) -> BitVec {
	let mut prime_map = BitVec::from_elem(max_num+1, true);
	prime_map.set(0, false);
	prime_map.set(1, false);
	for i in 2.. 2 + (max_num as f64).sqrt() as usize {
		if prime_map[i] {
			for j in i.. {
				if i * j > max_num {
					break;
				}
				prime_map.set(i * j, false);
			}
		}
	}
	prime_map
}

fn get_primes(prime_map: &BitVec, max_num: usize) -> Vec<i32> {
	let mut primes = Vec::with_capacity(max_num);
	for i in 0..max_num as usize {
		if prime_map[i] {
			primes.push(i as i32);
		}
	}
	primes
}

fn phi(n: i32, prime_factors: &Vec<i32>) -> i32 {
	let mut res: f64 = 1.0;
	res *= n as f64;

	for i in 0..prime_factors.len() as usize {
		res *= 1_f64 - (1_f64 / prime_factors[i] as f64);
	}
	
	return res as i32;
}

