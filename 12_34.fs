let upto n =
    let rec upto_rec (st, res) =
        if st < 1 then res
        elif st = 1 then st::res
        else upto_rec (st - 1, st::res)
    upto_rec (n, [])

let dnto n =
    let rec dnto_rec (st, fi, res) =
        if st > fi then res
        elif st = fi then st::res
        else dnto_rec (st + 1, fi, st::res)
    dnto_rec (1, n, [])  
    
let evenn n =
    let rec evenn_rec (st, cnt, res) =
        if cnt < 1 then res
        else evenn_rec (st - 2, cnt - 1, st::res)
    evenn_rec (2 * n, n, [])