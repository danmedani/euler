use prime_tools;

fn count_pairings(
	current_val: u64,
	top_val: u64, 
	prime_squares: &Vec<u64>, 
	min_index: usize, 
	choices_left: u32
) -> u64 {
	if choices_left == 0 {
		return top_val / current_val;
	}

	let mut current_index = min_index;
	let mut total_sum = 0;
	while current_index < prime_squares.len() {
		match current_val.checked_mul(prime_squares[current_index]) {
			None => break,
			Some(new_val) => {
				total_sum = total_sum + count_pairings(
					new_val,
					top_val,
					prime_squares,
					current_index + 1,
					choices_left - 1
				);
			}
		}

		current_index += 1;
	}

	total_sum
}

fn main() {
    println!("Hello, world!");
    // 33_554_432 == sqrt(2^50)
    // let max_val = 100;
    let max_val = 2u64.pow(50);
    // let max_val = 10000;
    let prime_squares = get_squared_primes(max_val);

    let top_val = max_val - 1;
    println!("{:?}", prime_squares.len());

    let mut total_sum = top_val;
    let mut add = false;
    let mut num_prime_squares_to_use = 1;
    while num_prime_squares_to_use < prime_squares.len() {
		let main_total = count_pairings(
    		1,
    		top_val,
    		&prime_squares,
    		0,
    		num_prime_squares_to_use as u32
    	);
    	
    	if add {
    		total_sum += main_total;
    	} else {
    		total_sum -= main_total;
    	}
    	add = !add;
    	println!("num_prime_squares_to_use = {}, add = {}, total = {}, big total = {}", num_prime_squares_to_use, add, main_total, total_sum);
    	
    	num_prime_squares_to_use += 1;
    }

    println!("big total = {}", total_sum);
}


fn get_squared_primes(max_val: u64) -> Vec<u64> {
	let primes = prime_tools::get_primes_less_than_x((max_val as f64).sqrt() as u32 + 1);
    println!("last primes = {}", primes[primes.len() - 1]);
    let mut prime_squares = Vec::new();
    for prime in primes.iter() {
    	let prime_u64 = *prime as u64;
    	match prime_u64.checked_mul(prime_u64) {
    		None => { break; },
    		Some(val) => {
    			if val > max_val {
    				break;
    			}
    			prime_squares.push(val);
    		}
    	};
    }

    prime_squares
}
