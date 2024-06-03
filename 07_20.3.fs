// 20.3.1
let vat n x = 0.01 * (100.0 + float n) * float x

// 20.3.2
let unvat n x = float x * 100.0 / (100.0 + float n)

// 20.3.3
let rec min f = 
  let rec min_r f n =
    if f n = 0 then n 
    else min_r f (n + 1)
  min_r f 1
