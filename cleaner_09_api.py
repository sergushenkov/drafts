import pure_robot

class RobotApi:

    def setup(self, f_make, f_transfer):
        self.f_make = f_make
        self.f_transfer = f_transfer

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)

        self.cleaner_state = self.f_make(
            transfer_to_cleaner,
            command, 
            self.cleaner_state
        ) 

    def __call__(self, command):
        return self.make(command)


def transfer_to_cleaner(message):
    print (message)


api = RobotApi()    
api.setup(pure_robot.make, transfer_to_cleaner)
# api.setup(pure_robot.make_2, transfer_to_cleaner)
