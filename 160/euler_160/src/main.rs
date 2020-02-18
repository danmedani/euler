fn trailing_factorial(n: u64, mod_val: u64) -> u64 {
	let mut output = 1;
	let mut number_of_twos: u64 = 0;
	let mut i = 1;
	while i <= n {
		if i % 1_000_000_000 == 0 {
			println!("i = {:?}, output = {:?}", i, output);
		}
		let mut j = i;
		while j % 2 == 0 {
			j = j / 2;
			number_of_twos += 1;
		}
		while j % 5 == 0 {
			j = j / 5;
			number_of_twos -= 1;
		}
		output = (output * (j % mod_val)) % mod_val;
		i = i + 1;
	}
	while number_of_twos > 0 {
		output = (output * 2) % mod_val;
		number_of_twos -= 1;
	}
	return output % mod_val;
}

fn main() {
    println!("{:?}", trailing_factorial(1_000_000_000_000, 100000));
}
