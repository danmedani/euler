use prime_tools;

// fn find_

fn main() {
    println!("Hello, world!");
    // 33_554_432 == sqrt(2^50)
    // let max_val = 100;
    // let max_val = 2u64.pow(50);
    let prime_squares = get_squared_primes(100);
    
    println!("{:?}", prime_squares);
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
