use std::cmp;
use fraction::Fraction;
use std::thread;
use std::sync::mpsc;


fn is_geometric(a: u64, b: u64, c: u64) -> bool {
	Fraction::new(b, a) == Fraction::new(c, b)
}

fn is_perfect(n: u64) -> bool {
	let n_sq = n * n;
	let mut i = n - 1;
	while i > 0 {
		let q: u64 = n_sq / i;
		let r = n_sq % i;
		if r > 0 && is_geometric(cmp::min(i, r), cmp::max(i, r), q) {
			return true;
		}
		i = i - 1;
	}
	return false;
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
		    for n in 2..1_000_000 {
		    	if n % thread_count == thread_number {
		    		if (n - thread_number) % 10_000 == 0 {
			    		println!("thread {}: n = {}", thread_number, n);
			    	}
			    	if is_perfect(n) {
			    		println!("perfect! {} -- {}", n, n * n);
			    		the_sum += (n * n);
			    	}
		    	}
		    }

		    txx.send(the_sum).unwrap();

		});
    }
    thread::spawn(move || { tx.send(0); });

    let mut total_sum = 0;
    for received_sum in rx {
	    println!("Got: {}", received_sum);
	    total_sum += received_sum;
	}
    println!("total_sum = {}", total_sum);
}
