class Commands():

    def __init__(self):
        pass

    def get_command(self):
        self.command = str(input("What would you do? Please write your command here (-help for informations) ->  "))
        try:
            return self.command
        except ValueError:
            print("Error! Please write your command again.")

    def init_command(self):
        for i in self.command:
            pass

get = Commands()
print(get.get_command())