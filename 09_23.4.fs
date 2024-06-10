// 23.4.1
let (.+.) x y = 
    let (a, b, c) = x
    let (d, e, f) = y
    let cu = (c + f) % 12
    let ag = (b + e + (c + f) / 12) % 20
    let au = (a + d + (b + e + (c + f) / 12) / 20)
    (au, ag, cu)

let (.-.) x y = 
    let (a, b, c) = x
    let (d, e, f) = y
    (a, b, c).+. (-d, -e, -f)

// 23.4.2
let (.+) x y = 
    let (a, b) = x
    let (c, d) = y
    (a + c, b + d)
let (.-) x y = 
    let (a, b) = x
    let (c, d) = y
    (a - c, b - d)
let (.*) x y = 
    let (a, b) = x
    let (c, d) = y
    (a*c - b*d, b*c + a*d)
let (./) x y = 
    let (a, b) = y
    let z = (float a/(a*a + b*b), - float b/(a*a + b*b))
    x .* z