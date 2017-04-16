use std::collections::HashMap;

fn main() {
  let mut map = HashMap::new();
  for i in 2..30000 {
    for j in 2..30000 {
      let val:u64 = (i * i * i) + (j * j);
      if is_palin(val) {
        if map.contains_key(&val) {
          *map.get_mut(&val).unwrap() += 1;
        } else {
          map.insert(val, 1);
        }
      }
    }
  }

  for (key, val) in &map {
    if *val == 4 {
      println!("Found a 4! {}:{}", key, val);
    }
  }
}

fn is_palin(mum: u64) -> bool {
  let mut high_exp = 1;
  let low_exp = 10;
  while high_exp < mum {
    high_exp = high_exp * 10;
  }
  high_exp = high_exp / 10;
 
  let mut num = mum;
  while high_exp > 2 {
    if (num % low_exp) != (num / high_exp) {
      return false;
    }

    num = num - ((num / high_exp) * high_exp);
    num = num / 10;

    high_exp = high_exp / 100;
  }

  return true;
}
