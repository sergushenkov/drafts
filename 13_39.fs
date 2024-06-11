// 39.1
let rmodd lst =
    let rec rmodd_rec (lst, res) =
        if lst = [] || List.tail lst = [] then res
        else rmodd_rec (List.tail (List.tail lst), res @ [List.head (List.tail lst)])
    rmodd_rec (lst, [])

// 39.2
let del_even lst = 
    let rec del_even_rec (lst, res) =
        if lst = [] then res
        elif (List.head lst) % 2 = 1 then  del_even_rec (List.tail lst, res @ [List.head lst])
        else del_even_rec (List.tail lst, res)
    del_even_rec (lst, [])

// 39.3
let multiplicity x xs =
    let rec multiplicity (x, xs, cnt) =
        let h::t = xs
        let delta = if x = h then 1 else 0
        if t = [] then cnt + delta
        else multiplicity (x, t, cnt + delta)
    if xs = [] then 0 
    else multiplicity (x, xs, 0)

// 39.4
let split lst =
    let rec split_rec (lst, res1, res2) = 
        if lst = [] then (res1, res2)
        elif (List.tail lst) = [] then ((res1 @ [List.head lst]), res2)
        else split_rec (List.tail (List.tail lst), (res1 @ [List.head lst]), (res2 @ [List.head (List.tail lst)]))
    split_rec (lst, [], [])

// 39.5
exception NotEqualLength

let zip (lst1, lst2) =
    let rec zip_rec (lst1, lst2, res) =
        if (lst1 = [] && lst2 > []) || (lst2 = [] && lst1 > []) then raise NotEqualLength
        elif lst1 = [] && lst2 = [] then res
        else  zip_rec (List.tail lst1, List.tail lst2, res @ [(List.head lst1, List.head lst2)])
    zip_rec (lst1, lst2, [])
