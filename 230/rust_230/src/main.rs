use fast_fibonacci;

fn calc_size(n: u64, initial_size: u64) -> u64 {
    if n < 2 {
        return initial_size;
    }
    // println!("n = {:?}", n);
    return fast_fibonacci::fib_with_mod(n + 1, 1_000_000_000_000) * initial_size;
}

fn find_n_to_cover_digit(n: u64, initial_size: u64) -> u64 {
    let mut i = 1;
    loop {
        let size = calc_size(i, initial_size);
        // println!(" size = {:?}", size);
        if size >= n {
            if size <= initial_size {
                return 0;
            }
            if size <= (2 * initial_size) {
                return 1;
            }
            while calc_size(i, initial_size) >= n {
                // println!("  size = {:?}", size);
                i -= 1;
            }
            return i + 1;
        }
        i *= 2;
    }
}


fn d(a: &String, b: &String, x: u64, initial_size: u64) -> String {
    let n = find_n_to_cover_digit(x, initial_size);

    if x <= initial_size {
        return a[(x - 1) as usize..x as usize].to_string();
    }
    if x <= (initial_size * 2) {
        return b[(x - initial_size - 1) as usize..(x - initial_size) as usize].to_string();
    }

    let size_row_below = calc_size(n - 1, initial_size);
    let x_overs = x - size_row_below;

    return d(a, b, x_overs, initial_size);
}

fn s(n: u64) -> u64 {
    (127u64 + (19 * n)) * 7u64.pow(n as u32)
}

fn main() {
    for n in 0..18 {
        println!("s({:?}) = {:?}. d = {:?}", n, s(n), d(
            &String::from("1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"), 
            &String::from("8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"), 
            s(n),
            100
        ));
    }    
}
