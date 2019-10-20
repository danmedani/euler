use std::collections::HashMap;
use prime_tools;
use math::round;
extern crate num_bigint;
extern crate num;

use num_bigint::BigUint;
use num::FromPrimitive;


const MOD_VAL: u64 = 10_000_000_000_000_000;

fn power_mod_fast(val: u32, exponent: u32, modulus: u32) -> u32 {
	let mut values_seen = HashMap::new();
	let mut answer = 1;
	let mut index = 1;
	let mut saw_duplicate = false;

	while index < exponent + 1 {
		answer = (answer * val) % modulus;

		if saw_duplicate {
			index += 1;
		} else {
			match values_seen.get(&answer) {
				None => {
					values_seen.insert(answer, index);
					index += 1;
				},
				Some(last_index) => {
					let delta = index - last_index;

					if delta == 0 {
						return 0
					}
					index = ( (val - last_index) / delta ) * delta + last_index + 1;
					saw_duplicate = true;
				}
			}			
		}
	}

	answer
}

// n in [1..25025]
// k in [0..25025]
fn hash_for_mod_cache(n: u32, k: u32) -> u32 {
	return (n * 100_000) + k;
}

// grab digit counts for [1^1%1000, 2^2%1000, 3^3%1000, ..., 250250^250250%1000]
fn get_digit_counts() -> HashMap<u32, u32> {
	let vec: Vec<u32> = (1..=250250).collect();
	let vec: Vec<u32> = vec.into_iter().map(|x| power_mod_fast(x, x, 1000)).collect();

	let mut digit_counts = HashMap::new();
	for val in vec.iter() {
		let digit_count = digit_counts.entry(*val).or_insert(0);
		*digit_count += 1;
	}

	digit_counts
}

/// Grab the keys from the three digit list and sort them.
fn get_three_digit_list(digit_counts: &HashMap<u32, u32>) -> Vec<u32> {
	let mut three_digit_list = Vec::new();
    for (key, _) in digit_counts.iter() {
    	three_digit_list.push(*key);
    }
    three_digit_list.sort();
    three_digit_list
}

/// value in [0..999]
/// level in [0..999]
fn hash_combinations(value: u32, level: usize) -> u32 {
	return (value * 10_000) + level as u32;
}


fn choose_mod(
	n: u32, 
	k: u32, 
	modulus: u64, 
	prime_factor_map: &HashMap<u32, HashMap<u32, u32>>,
	mod_cache: &mut HashMap<u32, u64>
) -> u64 {
	let k = if k < (n-k) { n-k } else { k };

	// caching
	let mod_cache_hash = hash_for_mod_cache(n, k);
	match mod_cache.get(&mod_cache_hash) {
		None => (),
		Some(val) => return *val
	}
	
	println!("choose_mod {} C {}", n, k);

	let mut numerators: Vec<u32> = ((k+1)..=n).collect();
	for denominator in 2..=(n-k) {
		// println!("denominator = {}", denominator);

		let denominator_prime_factors = prime_factor_map.get(&denominator).unwrap();
		// println!("denominator factors = {:#?}",denominator_prime_factors);

		for (factor, count) in denominator_prime_factors.iter() {
			let mut factor_count = count.clone();

			for index in 0..numerators.len() {
				// println!("numberator! {}", numerators[index]);
				while factor_count > 0 && numerators[index] % factor == 0 {
					// println!(" choppin");
					factor_count = factor_count - 1;
					numerators[index] = numerators[index] / factor;
				}

				if factor_count == 0 {
					// println!("  done with denom");
					// println!("  ");
					// println!("new numerators = {:?}", numerators);
					// println!("  ");
					break;
				}
			}

			if factor_count != 0 {
				panic!("no.. {}, {}, {}, {}", factor, factor_count, n, k);
			}
		}
	}

	// at this time, the denominator has been whacked
	let mut final_answer = BigUint::new(vec![1]);
	let big_mod: BigUint = FromPrimitive::from_u64(modulus).unwrap();
	for num in numerators.iter() {
		final_answer = (final_answer * BigUint::new(vec![*num])) % &big_mod;
	}
	let digit_answer = small_big_int_to_u64(&final_answer);

	mod_cache.insert(mod_cache_hash, digit_answer);
	digit_answer
}


fn get_factor_map(max_val: u32) -> HashMap<u32, HashMap<u32, u32>> {
	let mut factor_map = HashMap::new();
    let primes = prime_tools::get_primes_less_than_x(
    	max_val
    	// round::ceil((max_val as f64).sqrt(), 1) as u32
	);
    for i in 1..=max_val {
    	factor_map.insert(
    		i, 
    		prime_tools::get_prime_factors_with_counts(i, &primes)
    	);
    }
    factor_map
}

fn get_combinations(
	value: u32,
	level: usize,

	three_digit_list: &Vec<u32>,
	digit_counts: &HashMap<u32, u32>,
	prime_factor_map: &HashMap<u32, HashMap<u32, u32>>,

	combo_cache: &mut HashMap<u32, u64>,
	mod_cache: &mut HashMap<u32, u64>,
) -> u64 {
	let hash_val = hash_combinations(value, level);
	match combo_cache.get(&hash_val) {
		None => (),
		Some(val) => return *val
	}

	println!("crunchin {} -> {}", value, level);
	
	let mod_val: BigUint = FromPrimitive::from_u64(MOD_VAL).unwrap();

	if level == three_digit_list.len() {
		let end_of_the_line_combos = if value % 250 == 0 { 1 } else { 0 };
		combo_cache.insert(hash_val, end_of_the_line_combos);

		return end_of_the_line_combos;
	}

	let mut number_of_combinations = BigUint::new(vec![0]);
	let decide_digit = three_digit_list[level];

	for count_decide_digit in 0..=digit_counts[&decide_digit] {
		let multiplier: BigUint = FromPrimitive::from_u64(
			choose_mod(
				digit_counts[&decide_digit], // n 
				count_decide_digit, // k
				MOD_VAL,
				prime_factor_map,
				mod_cache
			)
		).unwrap();

		let combinations: BigUint = FromPrimitive::from_u64(
			get_combinations(
				(
					value + (count_decide_digit * decide_digit)
				) % 1000,
				level + 1,

				three_digit_list,
				digit_counts,
				prime_factor_map,

				combo_cache,
				mod_cache
			)
		).unwrap();

		number_of_combinations = (
			number_of_combinations + (multiplier * combinations)
		) % &mod_val;
	}

	let number_of_combinations_digits = small_big_int_to_u64(&number_of_combinations);
	combo_cache.insert(hash_val, number_of_combinations_digits);
	number_of_combinations_digits
}

fn main() {
    let digit_counts = get_digit_counts();
    let three_digit_list = get_three_digit_list(&digit_counts);
    let factor_map = get_factor_map(30000);

    // let mut digit_counts = HashMap::new();
    // digit_counts.insert(0, 1);
    // let three_digit_list = vec![0, 5];
    // digit_counts.insert(5, 3);

    let mut mod_cache = HashMap::new();
    let mut combo_cache: HashMap<u32, u64> = HashMap::new();
    
    let combinations = get_combinations(
    	0, 
    	0,

    	&three_digit_list, 
    	&digit_counts, 
    	&factor_map,

    	&mut combo_cache,
    	&mut mod_cache,
    );

    println!("combination count = {}", combinations - 1);
}

fn small_big_int_to_u64(big_int: &BigUint) -> u64 {
	let mut result: u64 = 0;
	for digit in big_int.to_radix_be(10) {
		result = result + digit as u64;
		result = result * 10;
	}
	result / 10
}

// fn main() {
// 	let factor_map = get_factor_map(30000);
// 	let mut mod_cache = HashMap::new();
// 	println!("{}", choose_mod(
// 		25025,
// 		12000, // k
// 		MOD_VAL,
// 		&factor_map,
// 		&mut mod_cache
// 	));
// }

