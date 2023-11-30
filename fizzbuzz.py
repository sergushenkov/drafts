"""
Реализуйте классическую FizzBuzz без условных операторов
Надо вывести значения от 1 до N.
Если число делится на 3 и на 5, выводите FizzBuzz; если число делится на 3, выводите Fizz; 
если число делится на 5, выводите Buzz; иначе выводите само число. 
https://code.joejag.com/2017/revealing-design.html - решение"""

def fizz_buzz(n):
    keys = {0: 'FizzBuzz', 3: 'Fizz', 5: 'Buzz', 6: 'Fizz', 9: 'Fizz', 10: 'Buzz', 12: 'Fizz'}
    return [keys.get(x % 15, x) for x in range(1, n+1)]


assert fizz_buzz(1) == [1]
assert fizz_buzz(2) == [1, 2]
assert fizz_buzz(3) == [1, 2, 'Fizz']
assert fizz_buzz(4) == [1, 2, 'Fizz', 4]
assert fizz_buzz(5) == [1, 2, 'Fizz', 4, 'Buzz']
assert fizz_buzz(20) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
print('ok')