use fast_fibonacci;
use num_bigint::BigUint;
use num::FromPrimitive;

fn calc_size_of_nth_row(n: &BigUint, initial_size: &BigUint) -> BigUint {
    let modulo: BigUint = FromPrimitive::from_u64(10_000_000_000_000_000_000).unwrap();
    let one: BigUint = FromPrimitive::from_u64(1).unwrap();
    if *n < FromPrimitive::from_u64(2).unwrap() {
        return initial_size.clone();
    }
    return fast_fibonacci::bigfib_with_mod(&(n + one), &modulo) * initial_size;
}

fn find_first_row_to_cover_digit(n: &BigUint, initial_size: &BigUint) -> BigUint {
    // todo: implement binary search
    let mut row: BigUint = FromPrimitive::from_u64(1).unwrap();
    
    let zero: BigUint = FromPrimitive::from_u64(0).unwrap();
    let one: BigUint = FromPrimitive::from_u64(1).unwrap();
    let two: BigUint = FromPrimitive::from_u64(2).unwrap();
    loop {
        let row_size: BigUint = calc_size_of_nth_row(
            &row, 
            &initial_size
        );

        if row_size >= *n {
            if row_size <= *initial_size {
                return zero; // in A
            }
            while calc_size_of_nth_row(
                &row, 
                &initial_size
            ) >= *n {
                row -= &one;
            }
            return row + &one;
        }
        row *= &two;
    }
}

fn get_digit_at_row(
    a: &String, 
    b: &String, 
    digit_index: &BigUint, 
    row: &BigUint, 
    initial_size: &BigUint
) -> String {
    let zero: BigUint = FromPrimitive::from_u64(0).unwrap();
    let one: BigUint = FromPrimitive::from_u64(1).unwrap();
    let two: BigUint = FromPrimitive::from_u64(2).unwrap();
    if row == &zero {
        return a[small_big_int_to_u64(&(digit_index - &one)) as usize..small_big_int_to_u64(&(digit_index)) as usize].to_string();
    }
    if row == &one {
        return b[small_big_int_to_u64(&(digit_index - &one)) as usize..small_big_int_to_u64(&(digit_index)) as usize].to_string();
    }

    let size_two_rows_below = calc_size_of_nth_row(&(row - &two), initial_size);
    let size_one_row_below = calc_size_of_nth_row(&(row - &one), initial_size);

    if digit_index <= &size_two_rows_below {
        return get_digit_at_row(
            a,
            b,
            digit_index,
            &(row - &two),
            initial_size
        );
    } else {
        return get_digit_at_row(
            a,
            b,
            &(digit_index - size_two_rows_below),
            &(row - &one),
            initial_size
        );
    }
}

fn get_digit(
    a: &String, 
    b: &String, 
    digit_index: &BigUint, 
    initial_size: &BigUint
) -> String {
    let lowest_row_with_digit = find_first_row_to_cover_digit(digit_index, initial_size);
    return get_digit_at_row(
        a, 
        b, 
        digit_index, 
        &lowest_row_with_digit, 
        initial_size
    );
}


fn small_big_int_to_u64(big_int: &BigUint) -> u64 {
    let mut result: u64 = 0;

    let digits = big_int.to_radix_be(10);
	for i in 0..digits.len() - 1 {
		result = result + digits[i] as u64;
		result = result * 10;
	}
	result + digits[digits.len() - 1] as u64
}

fn s(n: u64) -> u64 {
    (127u64 + (19 * n)) * 7u64.pow(n as u32)
}

fn main() {
    let mut stri = String::new();
    let mut n = 17;
    loop {
        let digit = get_digit(
            &String::from("1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"), 
            &String::from("8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"), 
            &FromPrimitive::from_u64(s(n)).unwrap(),
            &FromPrimitive::from_u64(100).unwrap(),
        );
        stri += &digit;
        if n == 0 {
            break;
        }
        n -= 1;
    }
    println!("{:?}", stri);
}
