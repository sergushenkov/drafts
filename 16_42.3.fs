let rec allSubsets n k =
    if k = 0 then [[]]
    elif n = k then [List.init k ((+) 1)]
    else (allSubsets (n - 1) k) @ List.map (fun subset -> n :: subset) (allSubsets (n - 1) (k - 1))