#! /usr/bin/python3.10
# -*- coding: utf-8 -*-


from englisch import Vocabulary
# rich


class Commands:
    def __init__(self):
        self.vocabulary = Vocabulary()

    def get_command(self):
        command = str(input("Was wollen Sie tun? Bitte schreiben Sie dazu Ihren Command in die Zeile "
                            "(-help für mehr Informationen) -> "))
        try:
            return command
        except ValueError:
            print("Error! Bitte schreiben sie Ihren command neu in die Zeile.")

    def init_command(self):
        while True:
            _command = self.get_command()
            _return = ""

            if _command.split(' ')[0] == _command.split(' ')[0]:
                for i in range(0, len(_command), 1):
                    if i == 0:
                        if _command[0] == "-":
                            pass
                        else:
                            print(f"Error! Bitte schreibe den Prefix von '{_command[0]}' zu '-'")
                            get.get_command()
                    else:
                        _return = _return + str(_command[i])
            else:
                print("Error!")

            if _return.split(' ')[0] == "help":
                print(self.help())
            elif _return.split(' ')[0] == "delete":
                self.delete(_return)
            elif _return.split(' ')[0] == "new":
                self.new_vocabulary()
            elif _return.split(' ')[0] == "start":
                self.start_questions(_return.split(' ')[1])
            elif _return.split(' ')[0] == "list":
                self.list()
            elif _return.split(' ')[0] == "stop":
                return "Sie haben erfolgreich Ihren Vokabel-Trainer beendet!"
            else:
                print(_return)

    def help(self):
        i = """
        alle Commands:
        -help -> Printet alle Commands
        -new -> erstelle eine neue Vokabel
        -delete <vocabulary> -> Lösche eine Vokabel aus der Datenbank
        -list -> listet alle Vokabeln auf
        -start <Zeit in Minuten> -> fragt dich in diesen angegebenen 
         Minuten alle eingetragenen Vokabeln aus der Datenbank aus
        -stop -> Stoppt den Vokabeltrainer
        """
        return i

    def delete(self, command):
        if command.split(' ')[1] == "vocabulary":
            self.vocabulary.delete_vocabulary()

    def new_vocabulary(self):
        self.vocabulary.init_vocabulary()

    def start_questions(self, command):
        try:
            int(command)
            self.vocabulary.start_questions(command)
        except ValueError:
            print("Etwas ist schiefgelaufen beim starten der Fragen!")

    def test_mode(self):
        pass

    def list(self):
        self.vocabulary.list_vocabulary()


get = Commands()
print(get.init_command())
