use std::collections::HashMap;
use prime_tools;
use math::round;
use cache_macro::cache;
use lru_cache::LruCache;

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

#[cache(LruCache : LruCache::new(10000))]
#[cache_cfg(ignore_args = digit_counts, three_digit_list, modulus, prime_factor_map)]
#[cache_cfg(thread_local)]
fn variations(
	digit_counts: &HashMap<u32, u32>, 
	three_digit_list: &Vec<u32>,
	drop_value: u32, 
	modulus: u64,
	highest_allowed_val: u32,
	prime_factor_map: &HashMap<u32, HashMap<u32, u32>>
) -> u64 {
	if drop_value == 0 {
		return 25_026;
	}
	let mut variation_count: u64 = 0;

	let mut three_digit_index = 0;
	while three_digit_list[three_digit_index] < highest_allowed_val {
		let last_three = three_digit_list[three_digit_index];
		
		let mut count_digits = 1;
		let mut digit_product = count_digits * last_three;
		
		while digit_product <= drop_value && count_digits <= digit_counts[&last_three] {
			let dropped_value = drop_value - digit_product;
			let multiplier = choose_mod(
				digit_counts[&last_three], 
				count_digits,
				MOD_VAL,
				prime_factor_map
			);

			variation_count = (
				variation_count + (
					multiplier * variations(
						digit_counts,
						three_digit_list,
						dropped_value,
						modulus,
						last_three,
						prime_factor_map
					)
				)
			) % modulus;

			count_digits += 1;
			digit_product = count_digits * last_three;
		}
		three_digit_index += 1;
	}
	variation_count
}

#[cache(LruCache : LruCache::new(10000))]
#[cache_cfg(ignore_args = prime_factor_map)]
#[cache_cfg(thread_local)]
fn choose_mod(n: u32, k: u32, modulus: u64, prime_factor_map: &HashMap<u32, HashMap<u32, u32>>) -> u64 {
	let k = if k < (n-k) { n-k } else { k };
	let mut numerators: Vec<u32> = ((k+1)..=n).collect();

	let mut leftover_denom: u64 = 1;
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

			if factor_count != 0 {
				//shrug
				leftover_denom = leftover_denom * (factor_count as u64 * *factor as u64);
			}
		}
	}

	// at this time, the denominator has been whacked
	let mut final_answer = 1;
	for num in numerators.iter() {
		final_answer = (final_answer * *num as u64) % modulus;
	}

	final_answer / leftover_denom
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

fn get_factor_map(max_val: u32) -> HashMap<u32, HashMap<u32, u32>> {
	let mut factor_map = HashMap::new();
    let primes = prime_tools::get_primes_less_than_x(
    	round::ceil((max_val as f64).sqrt(), 1) as u32
	);
    for i in 1..=max_val {
    	factor_map.insert(
    		i, 
    		prime_tools::get_prime_factors_with_counts(i, &primes)
    	);
    }
    factor_map
}

// iterate through 250, 500, ..., 300M?
// hash results from variations based on drop_value
fn main() {
    println!("Hello, world!");
    // Ignore 0... it comes up 25,025 times (+ 1 for nothing!)
	// The number that appears that most is `125` with 6,257 appearences
    let digit_counts = get_digit_counts();
    let factor_map = get_factor_map(7000);
    let mut three_digit_list = Vec::new();
    for (key, val) in digit_counts.iter() {
    	three_digit_list.push(*key);
    }
    three_digit_list.sort();

    let vars = variations(
    	&digit_counts,
    	&three_digit_list,
    	250,
    	MOD_VAL,
    	251,
    	&factor_map
    );
    println!("var = {}", vars);
    let vars = variations(
    	&digit_counts,
    	&three_digit_list,
    	500,
    	MOD_VAL,
    	501,
    	&factor_map
    );
    println!("var = {}", vars);
    let vars = variations(
    	&digit_counts,
    	&three_digit_list,
    	750,
    	MOD_VAL,
    	751,
    	&factor_map
    );
    println!("var = {}", vars);
    // println!("251 choose 243 = {}", choose_mod(251, 8, MOD_VAL, &factor_map))
	
}




