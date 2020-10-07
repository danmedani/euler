use prime_tools;

fn main() {
	println!("is_u64_prime(1504170715041707) {:?}", prime_tools::is_u64_prime(1504170715041707));
	println!("is_u64_prime(4503599627370517) {:?}", prime_tools::is_u64_prime(4503599627370517));
	
	let euler: i64 = 1504170715041707;
	let modulo: i64 = 4503599627370517;
	let M: i64 = modulo % euler;

	let mut lowest: i64 = 1504170715041707;
	let mut sum: i64 = 1504170715041707 + 8912517754604;
	let mut val: i64 = 8912517754604;
	loop {
		let next = match val > M {
			true => (val - M) % euler,
			_ => (val - M) + euler
		};
		let diff = next - val;
		val = match next > euler {
			true => (next - euler) % diff,
			_ => diff - ((euler - next) % diff)
		};
		// println!("val = {:?}, next = {:?}, M = {:?}, diff = {:?}", val, next, M, diff);

		if val < lowest {
			lowest = val;
			sum += val;
			println!("{:?}, {:?}", val, sum	);
		}
	}
}
