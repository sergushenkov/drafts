# Ваш секретный пароль
SECRET = "секретный пароль"


class Error:
    def __init__(self):
        pass


err = Error()

# Если ввести форматную строку '{error.__init__.__globals__[SECRET]}'
# , она может считать данные из общего словаря:
user_input = input("Введите свой текст:")

print("Ваш текст:")
print(user_input.format(error=err))

# Вывод: 'секретный пароль'
