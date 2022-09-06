from Englisch import englisch.Vocabulary

class Commands():

    def __init__(self):
        pass

    def get_command(self):
        self.command = str(input("What would you do? Please write your command here (-help for informations) -> "))
        try:
            return self.command
        except ValueError:
            print("Error! Please write your command again.")

    def init_command(self):
        while True:
            _command = get.get_command()
            _return = ""

            if _command.split(' ')[0] == _command.split(' ')[0]:
                for i in range(0, len(_command), 1):
                    if i == 0:
                        if _command[0] == "-":
                            pass
                        else:
                            print(f"Error! Please write your prefix from '{_command[0]}' to '-'")
                            get.get_command()
                    else:
                        _return = _return + str(_command[i])
            else:
                print("Error!")

            if _return.split(' ')[0] == "help":
                print(get.help())
            elif _return.split(' ')[0] == "delete":
                get.delete(_return)
            elif _return.split(' ')[0] == "new":
                get.new_vocabulary()
            elif _return.split(' ')[0] == "stop":
                return "You stopped the Vocabulary-trainer!"
            else:
                print(_return)

    def help(self):
        i = """
        Commands:
        -help -> print all commands
        -delete <unit/vocabulary> <name of the unit or vocabulary> -> delete a unit or vocabulary
        -stop -> stoppt die while schleife
        """
        return i

    def delete(self, command):
        if command.split(' ')[1] == "vocabulary":
            englisch.Vocabulary.delete_vocabulary()

    def new_vocabulary(self):
        englisch.Vocabulary.init_vocabulary()

    def start_questions(self):
        pass

get = Commands()
print(get.init_command())