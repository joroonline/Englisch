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
        _command = get.get_command()
        _return = ""
        for i in range(0, len(_command), 1):
            if i == 0:
                if _command[0] == "-":
                    pass
                else:
                    print(f"Error! Please write your prefix from '{_command[0]}' to '-'")
                    get.get_command()
            else:
                _return = _return + str(_command[i])

        if _return == "help":
            return get.help()
        elif _return == "delete":
            return get.delete()

    def help(self):
        i = """
        Commands:
        -help -> print all commands
        -delete <unit/vocabulary> <name of the unit or vocabulary> -> delete a unit or vocabulary
        """
        return i

    def delete(self):
        pass

    def new_vocabulary(self):
        pass

    def start_questions(self):
        pass

get = Commands()
print(get.init_command())