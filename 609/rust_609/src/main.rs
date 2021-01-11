use prime_tools;
use bit_vec::BitVec;
use std::collections::HashMap;

const MAX: u64 = 100_000_000;
const MOD: u64 = 1_000_000_007;

fn get_prime_map(primes: &Vec<u64>) -> BitVec<u32> {
	let mut prime_map = BitVec::from_elem(MAX as usize + 1, false);
	for prime in primes {
		prime_map.set(*prime as usize, true);
	}
	prime_map
}

fn get_prime_sequence_map(primes: &Vec<u64>) -> HashMap<u64, u64> {
	let mut sequence_map = HashMap::new();
	let mut prime_count = 0;
	let mut key = 2;
	for prime in primes {
		while key < *prime {
			sequence_map.insert(key, prime_count);
			key += 1;
		}
		prime_count += 1;
	}
	while key <= MAX {
		sequence_map.insert(key, prime_count);
		key += 1;
	}
	sequence_map
}

fn get_non_prime_count_sequence_map(sequence_map: &HashMap<u64, u64>, prime_map: &BitVec<u32>) -> HashMap<u64, u64> {
	let mut non_prime_count_map = HashMap::new();
	non_prime_count_map.insert(1, 1);
	for i in 2..=MAX {
		let non_prime_count = if prime_map[i as usize] { non_prime_count_map[&sequence_map[&i]] } else { non_prime_count_map[&sequence_map[&i]] + 1 };
		non_prime_count_map.insert(i, non_prime_count);
	}
	non_prime_count_map
}

fn P(
	n: u64, 
	non_prime_count_map: &HashMap<u64, u64>, 
	sequence_map: &HashMap<u64, u64>,
	prime_map: &BitVec<u32>
) -> u64 {
	let mut counts = HashMap::new();
	for u0 in 2..=n {
		let mut sequence_stack = Vec::new();
		let mut u = u0;
		while u > 1 {
			sequence_stack.push(u);
			u = sequence_map[&u];
		}

		// full length
		*counts.entry(non_prime_count_map[&u0]).or_insert(0) += 1;

		// partial lengths
		let mut tail_count = 1;
		while sequence_stack.len() >= 2 {
			*counts.entry(non_prime_count_map[&u0] - tail_count).or_insert(0) += 1;
			let bottom_val = sequence_stack.pop().unwrap();
			tail_count += if prime_map[bottom_val as usize] { 0 } else { 1 };
		}
	}

	let mut product = 1;
	for (_, val) in counts {
		product = (product * val) % MOD;
	}
	product
}

fn main() {
	let primes = prime_tools::get_primes_less_than_x(MAX as u32 + 1).iter().map(|&x| x as u64).collect();
	let prime_map = get_prime_map(&primes);
	let sequence_map = get_prime_sequence_map(&primes);
	let non_prime_count_map = get_non_prime_count_sequence_map(&sequence_map, &prime_map);

	println!("{:?}", P(MAX, &non_prime_count_map, &sequence_map, &prime_map));


}







