use std::collections::HashMap;

fn get_next_highest_prime(
	x: u64, 
	prime_map: &HashMap<u64, bool>, 
	next_highest_cache: &mut HashMap<u64, u64>
) -> u64 {
	return match prime_map.get(&x) {
		Some(_) => {
			next_highest_cache.insert(x, x);
			x
		},
		None => {
			let next_prime = get_next_highest_prime(
				x + 1,
				&prime_map,
				next_highest_cache
			);
			next_highest_cache.insert(x, next_prime);
			next_prime
		}
	}
}

fn get_next_lowest_prime(
	x: u64, 
	prime_map: &HashMap<u64, bool>, 
	next_lowest_cache: &mut HashMap<u64, u64>
) -> u64 {
	return match prime_map.get(&x) {
		Some(_) => {
			next_lowest_cache.insert(x, x);
			x
		},
		None => {
			let next_prime = get_next_lowest_prime(
				x - 1,
				&prime_map,
				next_lowest_cache
			);
			next_lowest_cache.insert(x, next_prime);
			next_prime
		}
	}
}


fn main() {
	let primes = prime_tools::get_primes_less_than_x(2000000);
	let mut prime_map = HashMap::new();
	let mut sum_semi_div = 0;
	for prime in &primes {
		prime_map.insert(*prime as u64, true);
	}
	let mut next_highest_cache = HashMap::new();
	let mut next_lowest_cache = HashMap::new();
	
	for n in 4..1_001 as u64 {
		let root_number = (n as f64).sqrt() as u64;
		let mut up_root_number = root_number;
		if root_number * root_number != n {
			up_root_number = up_root_number + 1;
		}
		let lpsq = get_next_lowest_prime(
			root_number,
			&prime_map,
			&mut next_lowest_cache
		);
		let ups = get_next_highest_prime(
			up_root_number,
			&prime_map,
			&mut next_highest_cache
		);
		
		let ups_div = n % ups == 0;
		let lpsq_div = n % lpsq == 0;
		if ups_div ^ lpsq_div {
			sum_semi_div += n;
		}

		if n % 1_000_000 == 0 {
			println!("n = {:?}", n);
		}
	}
    println!("sum_semi_div = {:?}", sum_semi_div);
}
