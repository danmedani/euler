extern crate bit_vec;
use bit_vec::BitVec;
use std::collections::HashSet;

fn main() {
    let max_num: u64 = 100000000;
    let modulo: u64 = 1000000009;

	let prime_map = get_prime_map(max_num);
	let primes = get_primes(&prime_map, max_num);
	println!("len primes == {}", primes.len());
	println!("");
	let mut level = 0;
	for i in 0..primes.len() {
		let prime_count: u64 = how_many_in_factorial(max_num, primes[i]);
		let power_level: u64 = power_mod(primes[i], prime_count*2, modulo);
		let new_level: u64 = power_level * (level + 1);
		level = (level + new_level) % modulo;
	}
	println!("answer! {}", level+1);
}


fn power_mod(a: u64, exp: u64, modd: u64) -> u64 {
	let mut product = 1;
	for i in 0..exp {
		product = (product * a) % modd;
	}
	return product;
}

fn how_many_in_factorial(facto: u64, num: u64) -> u64 {
	let mut pow = 1;
	let mut answer = 0;
	let mut power = num.pow(pow);

	while power <= facto {
		answer += (facto / power);
		pow += 1;
		power = num.pow(pow);
	}
	return answer;
}

fn get_prime_map(max_num: u64) -> BitVec {
	let mut prime_map = BitVec::from_elem(max_num as usize + 1, true);
	prime_map.set(0, false);
	prime_map.set(1, false);
	for i in 2.. 2 + (max_num as f64).sqrt() as usize {
		if prime_map[i] {
			for j in i.. {
				if i * j > max_num as usize {
					break;
				}
				prime_map.set(i * j, false);
			}
		}
	}
	prime_map
}

fn get_primes(prime_map: &BitVec, max_num: u64) -> Vec<u64> {
	let mut primes = Vec::with_capacity(max_num as usize);
	for i in 0..max_num as usize {
		if prime_map[i] {
			primes.push(i as u64);
		}
	}
	primes
}
