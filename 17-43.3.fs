let try_find key map =
    Map.tryPick (fun k v -> if k = key then Some v else None) map