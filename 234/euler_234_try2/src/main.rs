use std::collections::HashMap;

fn main() {
	let top_val = 999_966_663_334 as u64;
	let top_prime = 2 * ((top_val as f64).sqrt() as u32);
	let primes: Vec<u64> = prime_tools::get_primes_less_than_x(top_prime).into_iter().map(
		|prime| prime as u64
	).collect();
    
	let mut left_prime_index = 0;
	let mut right_prime_index = 1;

	let mut total_sum = 0;

	while right_prime_index < primes.len() {
		let left_prime = primes[left_prime_index];
		let right_prime = primes[right_prime_index];
		let left_prime_squared = left_prime * left_prime;
		let right_prime_squared = right_prime * right_prime;

		let mut factors = HashMap::new();
		let mut left_factor = left_prime_squared + left_prime;
		while left_factor < right_prime_squared {
			factors.insert(left_factor, true);
			left_factor += left_prime;
		}
		let mut right_factor = right_prime_squared - right_prime;
		while right_factor > left_prime_squared {
			match factors.get(&right_factor) {
				Some(_) => {
					factors.remove(&right_factor);
				},
				None => {
					factors.insert(right_factor, true);
				}
			}
			right_factor -= right_prime;
		}
		for (val, _) in &factors {
			if *val as u64 <= top_val {
				total_sum += val;
			}
		}

		left_prime_index += 1;
		right_prime_index += 1;
	}
	println!("total_sum = {:?}", total_sum);
}