use std::cmp;

fn convert_triple(n: u64, m: u64, c: u64) -> (u64, u64, u64) {
	let a = (m * m) - (n * n);
	let b = 2 * m * n;
	return (a, b, c * c);
}

fn generate_pairs(max_c: u64) -> Vec<(u64, u64, u64)> {
	let mut pairs: Vec<(u64, u64, u64)> = Vec::new();

	let mut n = 1;
	let mut m = 2;
	loop {
		loop {
			let v1 = (m * m) - (n * n);
			let v2 = 2 * m * n;
			let a = cmp::min(v1, v2);
			let b = cmp::max(v1, v2);
			let c = (m * m) + (n * n);

			if c > max_c {
				if m == n + 1 {
					return pairs;
				}
				break;
			}

			pairs.push(convert_triple(a, b, c));
			m += 2;
		}

		n += 1;
		m = n + 1;
	}
}

fn is_product_super_perfect(a: u64, b: u64) -> bool {
	// 2 * 3 = 6
	// 2 * 2 * 7 = 28

	if (a % 7 > 0) && (b % 7 > 0) {
		return false;
	}
	if (a % 3 > 0) && (b % 3 > 0) {
		return false;
	}

	let mod_val = match a % 2 == 0 {
		true => a,
		_ => b
	};
	if mod_val % 8 == 0 {
		return true;
	}

	return false;
}



fn main() {
	let mut count_not_super_perfect = 0;

	for (a, b, _) in generate_pairs(100_000_000) {
		if !is_product_super_perfect(a, b) {
			count_not_super_perfect += 1;
		}
	}

	println!("count_not_super_perfect = {:?}", count_not_super_perfect);
}

