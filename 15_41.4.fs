// 41.4.1
let list_filter f xs =
    List.foldBack (fun x acc -> if f x then x::acc else acc) xs []

// 41.4.2
let sum (p, xs) =
    List.fold (fun acc x -> if p x then acc + x else acc) 0 xs

// 41.4.3
let revrev xs =
    let rev xs = List.fold (fun head tail -> tail::head) [] xs
    List.fold (fun acc x -> (rev x) :: acc) [] xs