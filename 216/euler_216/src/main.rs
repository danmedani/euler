use std::cmp;
use prime_tools;
use std::collections::HashSet;
use math::round;
extern crate num_bigint;
extern crate num;

use num::FromPrimitive;
use num_bigint::BigUint;
use std::thread;
use std::sync::mpsc;

fn t(n: u64) -> u64 {
	2 * (n * n) - 1
}

fn is_prime(t: u64, primes: &Vec<u32>) -> bool {
	let max_prime_to_check = round::ceil((t as f64).sqrt(), 1) as u32;
	let mut prime_index = 0;
	while primes[prime_index] <= max_prime_to_check {
		if t % primes[prime_index] as u64 == 0 {
			return false;
		}

		prime_index += 1;
	}
	return true;
}

fn main() {
	// sqrt(2 * (50M ** 2) - 1) == 70710678.118
	println!("Hello, world!");
	
    let (tx, rx) = mpsc::channel();

    let thread_count = 10;
    for thread_number in 0..thread_count {
    	let txx = mpsc::Sender::clone(&tx);
		thread::spawn(move || {
			println!("Thread {} begin", thread_number);
	    	let primes = prime_tools::get_primes_less_than_x(70_710_679);
	        println!("Thread {} got primes", thread_number);

	        let mut count = 0;
		    for n in 2..=50_000_000 {
		    	if n % thread_count == thread_number {
		    		let t_n = t(n);
			    	if is_prime(t_n, &primes) {
			    		count += 1;

			    		if (n - thread_number) % 10_000 == 0 {
				    		println!("thread {}: n = {}", thread_number, n);
				    	}
			    	}
		    	}
		    }
	        txx.send(count).unwrap();
	    });
    }
    thread::spawn(move || { tx.send(0); });
    

    let mut total_count = 0;
    for received_count in rx {
	    println!("Got: {}", received_count);
	    total_count += received_count;
	}
    println!("total_count = {}", total_count);
}


