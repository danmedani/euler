use std::collections::HashSet;
use std::collections::HashMap;
use prime_tools;
use math::round;
extern crate num_bigint;
extern crate num;

use num_bigint::BigUint;
use num::FromPrimitive;

const MOD_VAL: u64 = 10_000_000_000_000_000;

fn get_combos(
	value: u32,
	last_prime_index_used: usize,
	primes: &Vec<u32>,
	prime_sums: &HashMap<usize, u32>,
	value_prime_index_map: &HashMap<usize, usize>,
	combo_cache: &mut HashMap<u32, u64>,
	mod_val: &BigUint
) -> u64 {
	match combo_cache.get(&value) {
		None => (),
		Some(val) => return *val
	}

	println!("crunchin {}", value);
	match value {
		1 => return 0,
		0 => return 1,
		x => ()
	};
	// println!("last_prime_index_used = {}", last_prime_index_used);
	if last_prime_index_used == 0 {
		return 0;
	}

	let mut combo_count = BigUint::new(vec![0]);
	let mut prime_index = last_prime_index_used - 1;
	// value_prime_index_map[&(value as usize)];
	// println!("prime_index = {}", prime_index);
	// println!("prime_sums = {:?}", prime_sums);
	while prime_sums[&prime_index] >= value {
		while value < primes[prime_index] {
			prime_index = match prime_index { 0 => break, x => prime_index - 1 };
		}
		// println!(" value = {}, prime_index = {}, prime = {}", value, prime_index, primes[prime_index]);
		let combos: BigUint = FromPrimitive::from_u64(
			get_combos(
				value - primes[prime_index],
				prime_index,
				primes,
				prime_sums,
				value_prime_index_map,
				combo_cache,
				mod_val
			)
		).unwrap();

		combo_count = (combo_count + combos) % mod_val;
		prime_index = match prime_index { 0 => break, x => prime_index - 1 };
	}

	let combo_count_u64 = small_big_int_to_u64(&combo_count);
	combo_cache.insert(value, combo_count_u64);
	combo_count_u64
}

fn generate_prime_sums(primes: &Vec<u32>) -> HashMap<usize, u32> {
	let mut sum = 0;
	let mut prime_sums = HashMap::new();
	for prime_index in 0..primes.len() {
		sum += primes[prime_index];
		prime_sums.insert(prime_index, sum);
	}
	prime_sums
}

fn generate_value_prime_index_map(starting_primes: &Vec<u32>, max_prime_index_to_map: usize) -> HashMap<usize, usize> {
	let mut value: u32 = 2;
	let mut value_map = HashMap::new();

	for prime_index in 1..=max_prime_index_to_map {
		while value < starting_primes[prime_index] {
			value_map.insert(value as usize, prime_index - 1);
			value += 1;
		}
	}

	// All higher values map to the last prime.
	let highest_starter = starting_primes[starting_primes.len() - 1];
	while value <= highest_starter {
		value_map.insert(value as usize, max_prime_index_to_map);
		value += 1;
	}

	value_map
}

fn main() {
    let x = 5000;

	let mut combo_cache: HashMap<u32, u64> = HashMap::new();
    let mod_val: BigUint = FromPrimitive::from_u64(MOD_VAL).unwrap();
    let primes = prime_tools::get_primes_less_than_x(x);

    let starting_primes = prime_tools::get_primes_less_than_x(
    	primes.iter().sum::<u32>() + 1
    );
    let prime_sums = generate_prime_sums(&primes);
    let value_prime_index_map = generate_value_prime_index_map(
    	&starting_primes,
    	primes.len() - 1
    );

    let mut combo_count = BigUint::new(vec![0]);
    for starting_index in 0..starting_primes.len() {
    	let max_index_to_use = if starting_index >= primes.len() { primes.len() } else { starting_index + 1 };
    	let combos: BigUint = FromPrimitive::from_u64(
	    	get_combos(
		    	starting_primes[starting_index],
		    	max_index_to_use,
		    	&primes,
		    	&prime_sums,
		    	&value_prime_index_map,
		    	&mut combo_cache,
		    	&mod_val
		    )
	    ).unwrap();

    	combo_count = (combo_count + combos) % &mod_val;
    }
	
    println!("combination count = {}", small_big_int_to_u64(&combo_count));
}

fn small_big_int_to_u64(big_int: &BigUint) -> u64 {
	let mut result: u64 = 0;
	for digit in big_int.to_radix_be(10) {
		result = result + digit as u64;
		result = result * 10;
	}
	result / 10
}
