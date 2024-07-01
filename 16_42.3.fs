let rec allSubsets n k =
    if k = 0 then Set.empty.Add(Set.empty)
    elif n = k then Set.empty.Add(Set.ofList [1..n])
    else Set.union (allSubsets (n - 1) k) (Set.map (fun subset -> Set.add n subset) (allSubsets (n - 1) (k - 1)))