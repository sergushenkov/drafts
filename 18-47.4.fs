// 47.4.1
let factorial n =
    let mutable result = 1
    for i = 1 to n do
        result <- result * i
    result

// 47.4.2
let fibo n = 
    if n = 1 then 0
    elif n = 2 then 1
    else
        let mutable a = 0
        let mutable b = 1
        for i = 3 to n do
            let c = a + b
            a <- b
            b <- c
        b
