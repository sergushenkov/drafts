Прошёлся по своим программам двухлетней давности - там это типично, когда много методов и функций в одной строке. 
Сейчас даже не скажу почему так писал - возможно подсознательное желание сделать поменьше строк кода.
Последние полгода-год, после знакомства с принципами clean code, проблема практически исчезла - по крайней мере примеры сходу найти не удалось.

Зачем нужно разбивать такие строки? 
1) реально легче читать код спустя год :) Разбиение строк заставляет добавить переменные с подходящими названиями - и цепочка преобразований становится гораздо понятней;
2) отлаживать в процессе тоже легче - сообщение об ошибке указывает на строку и если в строке куча операторов - иногда совсем не очевидно, что именно в этой строке произошло;

Увеличение количества строк в программе (без увеличения функционала) по большому счету ни на что не влияет - байты на носителе экономить нет смысла, а производительность кода не ухудшается

```py
# for line in foods.strip().split('\n'):
# 	if line.strip().isdigit():
# 		elf_bug.append(int(line))
		
foods_count =	foods.strip()
             .split('\n')
for line in foods_count:
    is_line_digit = line.isdigit()
	if is_line_digit:
        weight = int(line)
		elf_bug.append(weight)
			
            
# for bag in bags.split('\n'):
#     group.append(set(i for i in bag))

bags = bags.split('\n')
for bag in bags:
    things = set(bag)
    group.append(things)


# things = dict(zip(alfabet, range(1, 53)))

things = dict(
    zip(alfabet, 
        range(1, 53)
    )
)


# for i in range(int(move)):
#     stacks[int(to_stack) - 1].append(crate.pop())

move_len = int(move)
for i in range(move_len):
    x = crate.pop()
    ind = int(to_stack) - 1
	stacks[ind].append(x)
    
	
# if len(set(input[last:first])) == 14:

current_input = input[last:first]
unique_values = set(current_input)
if len(unique_values) == 14:


# if last in all_dir[''.join(pwd)] and all_dir[''.join(pwd) + last][0]:
# 	 all_dir[''.join(pwd)].remove(last)
# 	 all_dir[''.join(pwd)].append(all_dir[''.join(pwd) + last][0])

current_dir = ''.join(pwd)
if next_subdir in all_dir[current_dir] and all_dir[current_dir + next_subdir][0]:
	all_dir[current_dir].remove(next_subdir)
	all_dir[current_dir].append(all_dir[current_dir + next_subdir][0])
	
    
#if high + 1 >= grid[x][y][1] and cost + 1 < grid[x][y][2]:

is_higher = high + 1 >= grid[x][y][1]
is_more_expensive = cost + 1 < grid[x][y][2]
if is_higher and is_more_expensive:
    ...
```