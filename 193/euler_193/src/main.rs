use prime_tools;

fn count_pairings(
	current_value: u64,
	top_val: u64, 
	prime_squares: &Vec<u64>, 
	min_index: usize, 
	choices_left: u8,
	add: bool
) {
	if choices_left == 0 {
		return top_val / current_value;
	}

	let mut current_index = min_index;
	while current_index < prime_squares.len() {
		let mut total = 0;
		match current_value.checked_mul(prime_squares[current_index]) {
			None => break,
			Some(val) => {
				total = val;
			}
		}

		total += count_pairings(
			total,
			top_val,
			prime_squares,
			current_index + 1,
			choices_left - 1,
			!add
		);
	}

	total
}

fn main() {
    println!("Hello, world!");
    // 33_554_432 == sqrt(2^50)
    // let max_val = 100;
    // let max_val = 2u64.pow(50);
    let max_val = 100;
    let prime_squares = get_squared_primes(max_val);

    let top_val = max_val - 1;
    println!("{:?}", prime_squares);

    let mut total_count = top_val;
    for squarey in prime_squares.iter() {
    	let squarey_count = top_val / squarey;
    	total_count = total_count - squarey_count;
    }

    println!("total = {}", total_count);
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
