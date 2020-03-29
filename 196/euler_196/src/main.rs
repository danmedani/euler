use prime_tools;
use bit_vec::BitVec;

fn get_row_start(row: u64) -> u64 {
	return (row * (row - 1) / 2) + 1;
}

fn get_row_end(row: u64) -> u64 {
	return get_row_start(row + 1) - 1;
}

fn get_val_at_pos(row: u64, col: u64) -> u64 {
	return get_row_start(row) + col;
}

fn get_neighbors(row: u64, col: u64) -> Vec<(u64, u64)> {
	let mut neighbors = Vec::new();

	neighbors.push((row + 1, col));
	neighbors.push((row + 1, col + 1));
	if col > 0 {
		neighbors.push((row + 1, col - 1));
		neighbors.push((row - 1, col - 1));
	}
	if col < row - 1 {
		neighbors.push((row - 1, col));
	}
	if col < row - 2 {
		neighbors.push((row - 1, col + 1));
	}
	neighbors
}

fn is_prime(row: u64, col: u64, start: u64, offset_prime_map: &BitVec) -> bool {
	return offset_prime_map[(get_val_at_pos(row, col) - start) as usize];
}

fn get_prime_neighbors(
	row: u64, 
	col: u64, 
	start: u64, 
	offset_prime_map: &BitVec
) -> Vec<(u64, u64)> {
	let mut prime_neighbors = Vec::new();
	for neighbor in get_neighbors(row, col) {
		if is_prime(neighbor.0, neighbor.1, start, offset_prime_map) {
			prime_neighbors.push(neighbor);
		}
	}
	prime_neighbors
}

fn get_s(row: u64) -> u64 {
	let start = get_row_start(row - 2);
	let end = get_row_end(row + 2);

	let primes = prime_tools::get_primes_less_than_x((end as f64).sqrt() as u32 + 1);

	let mut offset_prime_map = BitVec::from_elem((end - start) as usize + 1, true);
	for prime_32 in primes.iter() {
		let prime = *prime_32 as u64;
		let mut val = (start / prime) * prime;
		while val < end {
			if val >= start {
				offset_prime_map.set((val - start) as usize, false);
			}
			val = val + prime;
		}
	}

	let mut sum_primes = 0;
	let length_row = get_row_end(row) - get_row_start(row) + 1;
	for col in 0..length_row {
		if is_prime(row, col, start, &offset_prime_map) {
			let prime_neighbors = get_prime_neighbors(row, col, start, &offset_prime_map);
			if prime_neighbors.len() > 1 {
				sum_primes += get_val_at_pos(row, col);
			} else if prime_neighbors.len() == 1 {
				let secondary_prime_neighbors = get_prime_neighbors(
					prime_neighbors[0].0, 
					prime_neighbors[0].1, 
					start,
					&offset_prime_map
				);
				if secondary_prime_neighbors.len() > 1 {
					sum_primes += get_val_at_pos(row, col);
				}
			}
		}
	}
	return sum_primes;
}

fn main() {
    println!("s = {:?}", get_s(5678027) + get_s(7208785));
}

