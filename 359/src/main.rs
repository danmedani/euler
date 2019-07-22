extern crate bit_vec;
#[macro_use] extern crate cached;

use std::collections::HashMap;
use bit_vec::BitVec;
use std::convert::TryInto;

fn main() {
	let max_num = 100000000;
	
	let prime_map = get_prime_map(max_num);
	let primes = get_primes(&prime_map, max_num);
	println!("len primes == {}", primes.len());
	
	let mut s:u64 = 0;
	for i in 2.. 1 + max_num as i32 {
		if i % 1000000 == 0 {
			println!("o man {}", i);
		}
		let counts = get_prime_factor_counts(i, &primes, &prime_map, max_num);
		let smallest_num = get_smallest_num(i, &counts);
		s = s + smallest_num as u64;
	}
	println!("ans = {}", s);
}

fn get_smallest_num(value: i32, factors: &HashMap<i32, i32>) -> i32 {
	let mut maximillion = -1;
	for (factor, count) in factors {
		let min = get_min(*factor, *count);
		if min > maximillion {
			maximillion = min;
		}
	}
	return maximillion;
}

fn get_min(number: i32, count: i32) -> i32 {
	if count <= number {
		return count * number;
	}
	return get_hard_min(number, count);
}

cached!{
	GET_HARD_MIN;
	fn get_hard_min(number: i32, count: i32) -> i32 = {
		let max_min:i32 = number * count;
		let mut num_array: [i32; 200] = [0; 200];
		let mut exp: i32 = 1;
		while number.pow(exp.try_into().unwrap()) <= max_min {
			let mut index: i32 = number.pow(exp.try_into().unwrap());
			while index <= max_min {
				num_array[index as usize] += 1;
				index += number.pow(exp.try_into().unwrap());
			}
			exp += 1;
		}
		let mut hard_min: i32 = 0;
		let mut count_so_far: i32 = 0;
		while count_so_far < count {
			count_so_far += num_array[hard_min as usize];
			hard_min += 1;
		}
		return hard_min - 1;
	}
}

fn get_prime_factor_counts(n: i32, primes: &Vec<i32>, prime_map: &BitVec, max_num: usize) -> HashMap<i32, i32> {
	let mut x = n;
	let mut factor_counts = HashMap::new();
	let mut i:usize = 0;
	while !prime_map[x as usize] && x > 1 {
		while i < max_num {	
			if x % primes[i] == 0 {
		        while x % primes[i] == 0 {
		        	if !factor_counts.contains_key(&primes[i]) {
						factor_counts.insert(primes[i], 1);
					} else {
						*factor_counts.get_mut(&primes[i]).unwrap() += 1;
					}
		        	x /= primes[i];
		        }
		        i += 1;
				break;
		    }
			i += 1;
		}
	}
	if x > 1 {
		factor_counts.insert(x, 1);	
	}
	factor_counts
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
