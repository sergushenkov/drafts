from cleaner_10_api import api

code = '100 move -90 turn soap set start 50 move stop'
api(code)
print(api.cleaner_state)