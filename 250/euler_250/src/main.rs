use std::collections::HashMap;


fn power_mod(val: u32, exponent: u32, modulus: u32) -> u32 {
	let mut answer = 1;
	for _ in 0..exponent {
		answer = (answer * val) % modulus;
	}
	answer
}

fn power_mod_fast(val: u32, exponent: u32, modulus: u32) -> u32 {
	let mut values_seen = HashMap::new();
	let mut answer = 1;
	let mut index = 1;
	let mut saw_duplicate = false;

	while index < exponent + 1 {
		answer = (answer * val) % modulus;

		if saw_duplicate {
			index += 1;
		} else {
			match values_seen.get(&answer) {
				None => {
					values_seen.insert(answer, index);
					index += 1;
				},
				Some(last_index) => {
					let delta = index - last_index;

					if delta == 0 {
						return 0
					}
					index = ( (val - last_index) / delta ) * delta + last_index + 1;
					saw_duplicate = true;
				}
			}			
		}
	}

	answer
}


fn main() {
    println!("Hello, world!");

    for i in 1..10000 {
    	let p_m = power_mod(i, i, 1000);
    	let p_m_f = power_mod_fast(i, i, 1000);
    	if p_m != p_m_f {
    		println!("NOT EQUAL! {} == {}", p_m, p_m_f);
    	}
    }
}
