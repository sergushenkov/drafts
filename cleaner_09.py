from cleaner_09_api import api

code = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")
api(code)
print(api.cleaner_state)