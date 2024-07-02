// 47.4.1
let f(n:int):int =
    let mutable result = 1
    for i = 1 to n do
        result <- result * i
    result

// 47.4.2
let fibo(n:int):int = 
    if n = 0 then 0
    elif n = 1 then 1
    else
        let mutable a = 0
        let mutable b = 1
        for i = 2 to n do
            let c = a + b
            a <- b
            b <- c
        b