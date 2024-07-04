// 49.5.1
let even_seq = Seq.initInfinite (fun i -> (i + 1) * 2)

// 49.5.2
let fac_seq = 
    let factorial n =
        let rec f x a =
            if x <= 1 then a
            else f (x - 1) (a * x)
        f n 1
    Seq.initInfinite (fun i -> i + 1)
    |> Seq.map factorial
    
// 49.5.3
let seq_seq = Seq.initInfinite (fun i -> if i % 2 = 0 then i / 2 else -(i + 1) / 2)