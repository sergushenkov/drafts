// 16.1
let notDivisible = function
  | (x, y) -> y % x = 0

// 16.2
let rec checkDivisible = function
  | (x, y) when y >= x * x -> not(y % x = 0) && checkDivisible(x + 1, y)
  | _ -> true

let prime = function
  | 1|2|3 -> true
  | n -> checkDivisible(2, n)