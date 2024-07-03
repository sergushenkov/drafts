// 48.4.1
let rec fibo1(n:int, n1:int, n0:int):int =
    if n = 0 then n0
    elif n = 1 then n1
    elif n = 2 then n1 + n0
    else fibo1(n - 1, n0 + n1, n1)

// 48.4.2
let fibo2(n:int, с):int =
    let rec fib_r n a b с =
        match n with
        | 0 -> с a
        | 1 -> с b
        | _ -> fib_r (n - 1) b (a + b) с
    fib_r n 0 1 id

// 48.4.3
let bigList n k =
    let rec bigListHelper n acc =
        if n = 0 then acc
        else bigListHelper (n - 1) (1 :: acc)
    bigListHelper n []