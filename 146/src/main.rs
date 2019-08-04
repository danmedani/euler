fn main() {
	let mut count = 0;
	for i in 2..150000000 {
		let i_sq = i * i;
		if 
			probably_prime(i_sq+1) &&
			probably_prime(i_sq+3) &&
			probably_prime(i_sq+7) &&
			probably_prime(i_sq+9) &&
			probably_prime(i_sq+13) &&
			probably_prime(i_sq+27) {
				if 
					is_prime(i_sq+1) && 
					is_prime(i_sq+3) && 
					!is_prime(i_sq+5) && 
					is_prime(i_sq+7) && 
					is_prime(i_sq+9) && 
					!is_prime(i_sq+11) &&
					is_prime(i_sq+13) &&
					!is_prime(i_sq+15) &&
					!is_prime(i_sq+17) &&
					!is_prime(i_sq+19) &&
					!is_prime(i_sq+21) &&
					!is_prime(i_sq+23) &&
					!is_prime(i_sq+25) &&
					is_prime(i_sq+27) 
				{
				    count += i;
				    println!("found 1, {}, {}", i, count);
				}
			}
		if i % 100000 == 0 {
			println!("{}, {}", i, i_sq);
		}
	}
	println!("found {}", count);
}

fn probably_prime(x: u64) -> bool {
	if x % 2 == 0 {
		return false;
	}
	if x % 3 == 0 {
		return false;
	}
	let mut i = 5;
	let mut w = 2;
	let mut total_checks = 0;
	while i * i <= x {
		if x % i == 0 {
			return false;
		}
		i += w;
		w = 6 - w;

		total_checks = total_checks + 1;
		if total_checks > 100 {
			return true;
		}
	}
	return true;
}

fn is_prime(x: u64) -> bool {
	if x % 2 == 0 {
		return false;
	}
	if x % 3 == 0 {
		return false;
	}
	let mut i = 5;
	let mut w = 2;
	while i * i <= x {
		if x % i == 0 {
			return false;
		}
		i += w;
		w = 6 - w;
	}
	return true;
}
