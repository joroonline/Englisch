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
        do = self.command.split(" ")
        for i in range(len(do)):
            if do[1] == "help":
                return do[1]
            if do[1] == "delete":
                get.delete_vocabulary()
            if do[1] == "new":
                get.new_vocabulary()
            if do[1] == "start":
                get.start_questions()

    def help(self):
        return "Prefix"

    def delete_vocabulary(self):
        pass

    def new_vocabulary(self):
        pass

    def start_questions(self):
        pass

get = Commands()
print(get.get_command())
print(get.init_command())