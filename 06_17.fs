// 17.1
let rec pow = function
  | s, n when n = 0 -> ""
  | s, n -> s + pow(s, n - 1)

// 17.2
let isIthChar = function
    | (s, n, c) when n < String.length(s) & n >= 0 -> (s.[n] = c)
    | (s, n, c) -> 1=0

// 17.3
let rec occFromIth = function
    | s, n, c when n = String.length(s) -> 0
    | s, n, c when s.[n] = c -> 1 + occFromIth(s, n + 1, c)
    | s, n, c -> occFromIth(s, n + 1, c)


//F# Compiler for F# 4.0 (Open Source Edition)

// let a = isIthChar("abc", 0, 'a')
// let b = isIthChar("abc", 1, 'b')
// let c = isIthChar("abc", 1, 'a')
// let d = isIthChar("abc", 0, 'd')
// let e = isIthChar("abc", -1, 'c')
// let f = isIthChar("abc", 3, 'c')
// // let g = isIthChar("", 0, '')  // символ не может быть пустым
// let h = isIthChar("", 0, 'c')
// // let i = isIthChar("abc", 0, '')  // символ не может быть пустым

// printfn "%b" a  // true
// printfn "%b" b  // true
// printfn "%b" c  // false
// printfn "%b" d  // false
// printfn "%b" e  // false
// printfn "%b" f  // false
// printfn "%b" h  // false
