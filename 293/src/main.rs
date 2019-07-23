extern crate bit_vec;
use bit_vec::BitVec;
use std::collections::HashSet;

fn main() {
    let max_num: u64 = 1000000000;

	let prime_map = get_prime_map(max_num);
	let primes = get_primes(&prime_map, max_num);
	println!("len primes == {}", primes.len());

	let mut max_prime_index = 0;
	let mut product = 1;
	for i in 0..primes.len() {
		if product * primes[i] >= max_num {
			max_prime_index = i;
			break;
		}
		product *= primes[i];
	}

	let prime_counts: Vec<u64> = vec!(1; max_prime_index);
	let mut the_list = crunch_primes(1, max_num, &primes, 0);
	the_list.sort();
	the_list.remove(0);

	let mut pseudo_fortunates = HashSet::new();

	let mut prime_index: usize = 0; 
	for i in 0..the_list.len() {
		while primes[prime_index] < the_list[i] + 2 {
			prime_index += 1;
		}
		pseudo_fortunates.insert(primes[prime_index] - the_list[i]);
	}
	let mut sum_pseudo_fortunate: u64 = 0;
	for pseudo_fortunate in &pseudo_fortunates {
	    sum_pseudo_fortunate += pseudo_fortunate;
	}
	println!("{}", sum_pseudo_fortunate);
}

fn crunch_primes(current_product: u64, max_product: u64, primes: &Vec<u64>, current_index: usize) -> Vec<u64> {
	let mut new_list = Vec::new();

	if current_product >= max_product {
		return new_list;
	}
	new_list.push(current_product);

	let mut new_current_product = current_product;
	while new_current_product < max_product {
		new_current_product *= primes[current_index];
		let add_ons = crunch_primes(new_current_product, max_product, &primes, current_index + 1);
		new_list.extend(add_ons);
	}
	return new_list;
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





