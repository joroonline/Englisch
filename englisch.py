import sqlite3

def get_input():
    english = str(input("Please write a english word in this line: "))
    german = str(input("Please write a german word in this line: "))
    try:
        return [english, german]
    except ValueError:
        print("Error! Please write this word again.")

class Vocabulary():

    def __init__(self, vocabulary=None):
        self.connect = sqlite3.connect('Database_englisch_german')
        self.cusor = self.connect.cursor()
        self.combo = 0
        self.id  = 0
        if vocabulary is None:
            vocabulary = get_input()
        for s in range(len(vocabulary)):
            self.english = vocabulary[0]
            self.german = vocabulary[1]

    def init_vocabulary(self):
        self.cusor.execute('INSERT INTO zeitstempe (zeit) VALUES (?)', [self.english, self.german, self.combo])

    def get_vocabulary(self):
        pass

get = Vocabulary()

print(get.init_vocabulary())