// 40.1
let sum (p : int -> bool, xs : int list) : int= 
    let rec sum_r(p, xs, acc) =
        if xs = [] then acc
        elif p (List.head xs) then sum_r(p, List.tail xs, acc + List.head xs)
        else sum_r(p, List.tail xs, acc)
    sum_r(p, xs, 0)

// 40.2.1
let count (xs : int list, n : int) : int = 
    let rec count_r(xs, n, cnt) =
        if xs = [] || (List.head xs) > n then cnt
        elif (List.head xs) = n then count_r(List.tail xs, n, cnt + 1)
        else count_r(List.tail xs, n, cnt)
    count_r(xs, n, 0)

// 40.2.2
let insert (xs : int list, n : int) : int list=
    let rec insert_r (xs, n, xs_new) =
        if xs = [] then List.append xs_new [n]
        elif (List.head xs) > n then List.concat [ xs_new; [n]; xs ]
        else insert_r (List.tail xs, n, List.append xs_new [List.head xs])
    insert_r (xs, n, [])

// 40.2.3
let intersect (xs1 : int list, xs2 : int list) : int list = 
    let rec intersect_r (xs1, xs2, xs) = 
        if xs1 = [] || xs2 = [] then xs
        elif (List.head xs1) = (List.head xs2) then intersect_r (List.tail xs1, List.tail xs2, List.append xs [List.head xs1])
        elif xs = [] && (List.head xs1) > (List.head xs2) then intersect_r (xs1, List.tail xs2, xs)
        elif xs = [] && (List.head xs1) < (List.head xs2) then intersect_r (List.tail xs1, xs2, xs)
        elif (List.head xs1) = (List.head xs) then intersect_r (List.tail xs1, xs2, List.append xs [List.head xs1])
        elif (List.head xs2) = (List.head xs) then intersect_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        elif (List.head xs1) > (List.head xs2) then intersect_r (xs1, List.tail xs2, xs)
        else intersect_r (List.tail xs1, xs2, xs)  
    intersect_r (xs1, xs2, [])

// 40.2.4
let plus (xs1 : int list, xs2 : int list) : int list=
    let rec plus_r (xs1, xs2, xs) =
        if xs1 = [] then List.append xs xs2
        elif xs2 = [] then List.append xs xs1
        elif (List.head xs1) = (List.head xs2) then plus_r (List.tail xs1, List.tail xs2, List.append xs [List.head xs1; List.head xs2])
        elif xs = [] && (List.head xs1) > (List.head xs2) then plus_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        elif xs = [] && (List.head xs1) < (List.head xs2) then plus_r (List.tail xs1, xs2, List.append xs [List.head xs1])
        elif (List.head xs1) = (List.head xs) then plus_r (List.tail xs1, xs2, List.append xs [List.head xs1])
        elif (List.head xs2) = (List.head xs) then plus_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        elif (List.head xs1) > (List.head xs2) then plus_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        else plus_r (List.tail xs1, xs2, List.append xs [List.head xs1])     
    plus_r (xs1, xs2, [])

// 40.2.5
let minus (xs1 : int list, xs2 : int list) : int list= 
    let rec minus_r (xs1, xs2, rez) = 
        if xs2 = [] then List.append rez xs1
        elif xs1 = [] then rez
        elif (List.head xs1) = (List.head xs2) then  minus_r (List.tail xs1, List.tail xs2, rez)
        elif (List.head xs1) < (List.head xs2) then  minus_r (List.tail xs1, xs2, List.append rez [List.head xs1])
        else minus_r (xs1, List.tail xs2, rez)
    minus_r (xs1, xs2, [])

// 40.3.1
let smallest (xs : int list) : int option =
    let rec smallest (xs, rez) =
        if xs = [] then Some(rez)
        elif List.head xs < rez then smallest (List.tail xs, List.head xs)
        else smallest (List.tail xs, rez)
    smallest (List.tail xs, List.head xs)  

// 40.3.2
let delete (n : int, xs : int list) : int list =
    let rec delete_r (n, xs, rez) =
        if xs = [] then rez
        elif (List.head xs) = n then List.append rez (List.tail xs)
        else delete_r (n, List.tail xs, List.append rez [List.head xs])
    delete_r (n, xs, [])

// 40.3.3
let sort (xs : int list) : int list=
    let rec sort_r (xs, rez) =
        if xs = [] then rez
        else
            let n = smallest xs
            sort_r (delete (n.Value, xs), (List.append rez [n.Value]))
    sort_r (xs, [])

// 40.4
let revrev(xs) =
    let rec rev_r (xs, rez) =
        if xs = [] then rez
        else rev_r (List.tail xs, List.append [List.head xs] rez)

    let rec rev_rev_r (xs, rez) =
        if xs = [] then rez
        else rev_r (List.tail xs, List.append [ rev_r (List.head xs, []) ] rez)
    rev_rev_r (xs, [])


  

    

    