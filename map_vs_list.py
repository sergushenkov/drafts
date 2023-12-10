str_keys = '55 66 77'
numbers = [66, 22, 77, 44, 55, 33]

keys = map(int, str_keys.split(' '))

for _ in range(2):
    cnt = 0
    for key in keys:
        if key in numbers:
            cnt += 1
    print(f'в списке есть {cnt} ключей')

print(type(keys))