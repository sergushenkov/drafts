import pure_robot as r

class RobotApi:

    def setup(self, robot, transfer):
        self.action = {
            'move': robot.move,
            'turn': robot.turn,
            'set': robot.set_state,
            'start': robot.start,
            'stop': robot.stop
        }
        self.transfer = transfer

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = r.RobotState(0.0, 0.0, 0, r.WATER)

        stack = []
        for x in command.split(' '):
            if x in self.action and stack:
                self.cleaner_state = self.action[x](self.transfer, stack.pop(), self.cleaner_state)
                continue
            if x in self.action :
                self.cleaner_state = self.action[x](self.transfer, self.cleaner_state)
                continue
            if x.lstrip("-").isdigit():
                stack.append(int(x))
                continue
            stack.append(x)

    def __call__(self, command):
        return self.make(command)


def transfer_to_cleaner(message):
    print (message)


api = RobotApi()    
api.setup(r, transfer_to_cleaner)
