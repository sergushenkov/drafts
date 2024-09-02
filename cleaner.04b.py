from cleaner_04a import Cleaner


def transfer_to_cleaner(rez):
    print(rez)

code = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

cleaner = Cleaner(transfer_to_cleaner)
cleaner.command(code)
