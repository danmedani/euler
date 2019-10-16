use std::collections::HashMap;
use prime_tools;

const MOD_VAL: u64 = 10_000_000_000_000_000;

fn power_mod(val: u32, exponent: u32, modulus: u32) -> u32 {
	let mut answer = 1;
	for _ in 0..exponent {
		answer = (answer * val) % modulus;
	}
	answer
}

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


fn variations(
	counts: &HashMap<u32, u32>, 
	three_digit_list: &Vec<u32>,
	drop_value: u32, 
	modulus: u32,
	highest_allowed_val: u32
) -> u64 {
	let mut variation_count: u64 = 0;

	let mut three_digit_index = 0;
	while three_digit_list[three_digit_index] < highest_allowed_val {
		let last_three = three_digit_list[three_digit_index];
		
		let mut count_digits = 1;
		let mut digit_product = count_digits * last_three;
		
		while digit_product <= drop_value && count_digits <= counts[&last_three] {
			let dropped_value = drop_value - digit_product;
			let multiplier = choose(
				counts[&last_three] as u64, 
				count_digits as u64
			);

			variation_count = (
				variation_count + (
					multiplier * variations(
						counts,
						three_digit_list,
						dropped_value,
						modulus,
						last_three
					)
				)
			) % modulus as u64;

			count_digits += 1;
			digit_product = count_digits * last_three;
		}

		three_digit_index += 1;
	}

	variation_count
}


fn choose(n: u64, k: u64) -> u64 {
	let s = if k < (n-k) { n-k } else { k };
	let mut numerator = 1;
	let mut num_val = n;

	while num_val > s {
		numerator = numerator * num_val;
		num_val -= 1;
	}

	let mut denominator = 1;
	let mut denom_val = 1;
	let top_val = n - s;
	while denom_val <= top_val {
		denominator = denominator * denom_val;
		denom_val += 1;
	}

	numerator / denominator
}


fn choose_mod(n: u32, k: u32, modulus: u32, prime_factor_map: HashMap<u32, HashMap<u32, u32>>) -> u32 {
	// n! / k! * (n-k)!
	let k = if k < (n-k) { n-k } else { k };

	// = n * (n-1) * (n-2) * ... * k + 1
	//   /
	//   1 * 2 * 3 * ... * n-k 
	let mut numerators: Vec<u32> = ((k+1)..n).collect();
	// let mut numerator_map = HashMap::new();
	for denominator in 1..=(n-k) {
		let denominator_prime_factors = prime_factor_map.get(&denominator).unwrap();

		for (factor, count) in denominator_prime_factors.iter() {
			let mut factor_count = count.clone();

			for index in 0..numerators.len() {
				if numerators[index] % factor == 0 {
					factor_count = factor_count - 1;
					numerators[index] = numerators[index] / factor; 
				}

				if factor_count == 0 {
					break;
				}
			}
		}
	}

	// at this time, the denominator has been whacked
	let mut final_answer = 1;
	for num in numerators.iter() {
		final_answer = (final_answer * num) % modulus;
	}

	final_answer
}

// grab digit counts for [1^1%1000, 2^2%1000, 3^3%1000, ..., 250250^250250%1000]
// Ignore 0... it comes up 25,025 times
// The number that appears that most is `125` with 6,257 appearences
fn get_digit_counts() -> HashMap<u32, u32> {
	let vec: Vec<u32> = (1..=250250).collect();
	let vec: Vec<u32> = vec.into_iter().map(|x| power_mod_fast(x, x, 1000)).collect();

	let mut digit_counts = HashMap::new();
	for val in vec.iter() {
		if *val != 0 {
			// 0 is special... 
			let digit_count = digit_counts.entry(*val).or_insert(0);
			*digit_count += 1;
		}
	}

	digit_counts
}

// fix choose
// iterate through 250, 500, ..., 300M?
// create hashmap
// get keys, sort, put in vec
// hash results from variations based on drop_value
fn main() {
    println!("Hello, world!");
    println!("52 choose 5 = {}", choose(52, 5));

    let digit_counts = get_digit_counts();

    let mut factor_map = HashMap::new();
    let primes = prime_tools::get_primes_less_than_x(80);
    for i in 1..=6257 {
    	factor_map.insert(
    		i, 
    		prime_tools::get_prime_factors_with_counts(i, &primes)
    	);
    }
    println!("factor_map = {:#?}", factor_map.get(&6000).unwrap());
    println!("52 choose 5 = {}", choose_mod(52, 5, 1000, factor_map));
	// largest count of digits (aside from 0) is 6257
}




