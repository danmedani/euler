use std::thread;
use std::sync::mpsc;

fn m(n: u64) -> u64 {
	let mut a = n - 1;
	while a * a % n != a {
		a = a - 1;
	}
	return a;
}

fn main() {
    println!("Hello, world!");

    let (tx, rx) = mpsc::channel();
    let thread_count = 32;
    for thread_number in 0..thread_count {
    	let txx = mpsc::Sender::clone(&tx);
    	thread::spawn(move || {
			println!("Thread {} begin", thread_number);
			let mut the_sum: u64 = 0;
		    for n in 1..=10_000_000 {
		    	if n % thread_count == thread_number {
		    		the_sum += m(n);

		    		if (n - thread_number) % 10_000 == 0 {
			    		println!("thread {}: n = {}", thread_number, n);
			    	}
		    	}
		    }

		    txx.send(the_sum).unwrap();

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
