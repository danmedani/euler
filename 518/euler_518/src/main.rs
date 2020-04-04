use std::collections::HashMap;
use prime_tools;
use std::thread;
use std::sync::mpsc;



fn main() {
    let (tx, rx) = mpsc::channel();
    let thread_count = 10;
    for thread_number in 0..thread_count {
    	let txx = mpsc::Sender::clone(&tx);
    	thread::spawn(move || {
    		let primes_u32 = prime_tools::get_primes_less_than_x(100_000_000);
		    let primes: Vec<u64> = primes_u32.into_iter().map(|prime| prime as u64).collect();

		    let mut prime_map = HashMap::new();
		    for prime in &primes {
		    	prime_map.insert(prime, true);
		    }
		    println!("{:?}", prime_map.len());

		    let prime_length = primes.len();
		    let max_prime = primes[prime_length - 1];
    		let mut prime_sum = 0;
    		let mut count_processed = 0;
    		for prime_a_index in 0..prime_length {
    			if prime_a_index % thread_count == thread_number {
    				for prime_b_index in (prime_a_index+1)..prime_length {
			    		let next_val = (primes[prime_b_index] + 1) * (primes[prime_b_index] + 1);
			    		if (next_val / (primes[prime_a_index] + 1)) > ( 2 * max_prime ) {
							break;
						}
			    		if next_val % (primes[prime_a_index] + 1) == 0 {
			    			let possible_next = (next_val / (primes[prime_a_index] + 1)) - 1;
			    			if possible_next > max_prime {
			    				break;
			    			}
			    			match prime_map.get(&possible_next) {
			    				Some(val) => prime_sum += primes[prime_a_index] +
			    					primes[prime_b_index] +
			    					possible_next,
			    				None => ()
			    			}
			    		}
			    	}
			    	count_processed += 1;
			    	if count_processed % 100 == 0 {
						println!("prime {:?}", primes[prime_a_index]);
			    	}
    			}
		    }
    		txx.send(prime_sum).unwrap();
    	});
    }
    thread::spawn(move || { tx.send(0); });

    let mut total_sum = 0;
    for received_count in rx {
	    println!("Got: {}", received_count);
	    total_sum += received_count;
	}

    println!("total_sum = {:?}", total_sum);
}

