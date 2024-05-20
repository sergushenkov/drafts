from functools import reduce

# oksana = [10, 1, 20, 2]  # [10, 1, 20, 2]
oksana = [15,1,25,2,30,3,10,5]

odometer = lambda x, y: [x[0], x[1], y] if len(x) == 2 else [x[0] + x[2]*(y-x[1]), y]

print(reduce(odometer, oksana, [0, 0])[0])