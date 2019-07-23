fn main() {
	// let max_num: u64 = 1000000;
	let max_num: u64 = 100000000000000000;

    let mut fibs = Vec::new();
    fibs.push(1);
    fibs.push(2);
    while fibs[fibs.len()-1] < max_num as u64 {
    	fibs.push(fibs[fibs.len()-1] + fibs[fibs.len()-2]);
    }

    let mut sums = Vec::new();
    sums.push(1);
    sums.push(2);

    for index in 2..fibs.len() {
    	let new_sum = sums[index-1] + sums[index-2] + fibs[index-2] - 1;
    	sums.push(new_sum);
    }

    println!("sum_zeck = {}", sum_zeck(max_num-1, &fibs, &sums));
}

fn sum_zeck(number: u64, fibs: &Vec<u64>, sums: &Vec<u64>) -> u64 {
	let mut i = 0;
	while fibs[i] < number {
		i += 1;
	}
	if fibs[i] == number {
		return sums[i];
	}
	i = i - 1;
	return sums[i] + (number - fibs[i]) + sum_zeck(number - fibs[i], fibs, sums);
}
