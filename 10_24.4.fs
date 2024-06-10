type TimeOfDay = { hours: int; minutes: int; f: string }

let (.>.) x y = 
  let a = if (x.f = "AM") then x.hours * 60 + x.minutes else 12 * 60 + x.hours * 60 + x.minutes
  let b = if (y.f = "AM") then y.hours * 60 + y.minutes else 12 * 60 + y.hours * 60 + y.minutes
  a > b