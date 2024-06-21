// 40.1
let sum (p, xs) = 
    let rec sum_r(p, xs, acc) =
        if xs = [] then acc
        elif p (List.head xs) then sum_r(p, List.tail xs, acc + List.head xs)
        else sum_r(p, List.tail xs, acc)
    sum_r(p, xs, 0)

// 40.2.1
let count (xs, n) = 
    let rec count_r(xs, n, cnt) =
        if xs = [] || (List.head xs) > n then cnt
        elif (List.head xs) = n then count_r(List.tail xs, n, cnt + 1)
        else count_r(List.tail xs, n, cnt)
    count_r(xs, n, 0)

// 40.2.2
let insert (xs, n) =
    let rec insert_r (xs, n, xs_new) =
        if xs = [] then List.append xs_new [n]
        elif (List.head xs) > n then List.concat [ xs_new; [n]; xs ]
        else insert_r (List.tail xs, n, List.append xs_new [List.head xs])
    insert_r (xs, n, [])

// 40.2.3
let intersect (xs1, xs2) = 
    let rec intersect_r (xs1, xs2, xs) = 
        if (List.head xs1) = (List.head xs2) then intersect_r (List.tail xs1, List.tail xs2, List.append xs [List.head xs1])
        elif xs1 = [] || xs2 = [] then xs
        elif xs = [] && (List.head xs1) > (List.head xs2) then intersect_r (xs1, List.tail xs2, xs)
        elif xs = [] && (List.head xs1) < (List.head xs2) then intersect_r (List.tail xs1, xs2, xs)
        elif (List.head xs1) = (List.head xs) then intersect_r (List.tail xs1, xs2, List.append xs [List.head xs1])
        elif (List.head xs2) = (List.head xs) then intersect_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        elif (List.head xs1) > (List.head xs2) then intersect_r (xs1, List.tail xs2, xs)
        else intersect_r (List.tail xs1, xs2, xs)  
    intersect_r (xs1, xs2, [])

// 40.2.4
let plus (xs1, xs2) =
    let rec plus_r (xs1, xs2, xs) =
        if xs1 = [] then List.append xs xs2
        elif xs2 = [] then List.append xs xs1
        elif (List.head xs1) = (List.head xs2) then plus_r (List.tail xs1, List.tail xs2, List.append xs [List.head xs1])
        elif xs = [] && (List.head xs1) > (List.head xs2) then plus_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        elif xs = [] && (List.head xs1) < (List.head xs2) then plus_r (List.tail xs1, xs2, List.append xs [List.head xs1])
        elif (List.head xs1) = (List.head xs) then plus_r (List.tail xs1, xs2, List.append xs [List.head xs1])
        elif (List.head xs2) = (List.head xs) then plus_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        elif (List.head xs1) > (List.head xs2) then plus_r (xs1, List.tail xs2, List.append xs [List.head xs2])
        else plus_r (List.tail xs1, xs2, List.append xs [List.head xs1])     
    plus_r (xs1, xs2, [])

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


  

    

    