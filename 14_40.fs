// 40.1
let rec sum (p, xs) = 
  let rec sum_r(p, xs, acc) =
    if xs = [] then acc
    elif p (List.head xs) then sum_r(p, List.tail xs, acc + List.head xs)
    else sum_r(p, List.tail xs, acc)
  sum_r(p, xs, 0)

// 40.2.1
let rec count (xs, n) = ...

// 40.2.2
let rec insert (xs, n) = ...

// 40.2.3
let rec intersect (xs1, xs2) = ...

// 40.2.4
let rec plus (xs1, xs2) = ...

// 40.2.5
let rec minus (xs1, xs2) = ...

// 40.3.1
let rec smallest = ...

// 40.3.2
let rec delete (n, xs) = ...

// 40.3.3
let rec sort = ...

// 40.4
let rec revrev = ...