// 50.2.1
let fac_seq =
    let rec factorial n =
        match n with
        | 0 | 1 -> 1
        | _ -> n * factorial (n-1)
    seq { for i in 0 .. System.Int32.MaxValue do yield factorial i }

// 50.2.2
let seq_seq =
    seq {
        yield 0
        for i in 1 .. System.Int32.MaxValue do
            yield -i
            yield i
    }