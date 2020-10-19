use prime_tools;
use fast_fibonacci;

fn main() {
    let primes = prime_tools::get_primes_between(100_000_000_000_000, 100_000_003_235_522);
    let mut sum_fibs = 0;
    let modulo = 1_234_567_891_011;
    
    for i in 0..100_000 {
        if i % 1000 == 0 {
            println!("{:?}, {:?}", i, sum_fibs);
        }
        sum_fibs = (sum_fibs + fast_fibonacci::fib_with_mod(primes[i], modulo)) % modulo;
    }
    println!("{:?}", sum_fibs);
}
