import cleaner_06_api as cleaner_api

# главная программа
cleaner_state = cleaner_api.init()

code = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

for command in code:
    cleaner_state = cleaner_api.action(command, cleaner_state)

print(
    cleaner_api.get_x(cleaner_state),
    cleaner_api.get_y(cleaner_state),
    cleaner_api.get_angle(cleaner_state),
    cleaner_api.get_state(cleaner_state),
)
