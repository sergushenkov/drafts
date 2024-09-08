import cleaner_07_api as cleaner_api

# главная программа
code = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

cleaner_state = cleaner_api.init(x=0.0, y=0.0, angle=0, state='WATER')
for command in code:
    cleaner_state = cleaner_api.action(command, cleaner_state)

print(
    cleaner_api.get_x(cleaner_state),
    cleaner_api.get_y(cleaner_state),
    cleaner_api.get_angle(cleaner_state),
    cleaner_api.get_state(cleaner_state),
)
