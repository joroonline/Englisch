import sqlite3, random

class Vocabulary():

    def get_input(self):
        self.english = str(input("Please write a english word in this line: "))
        self.german = str(input("Please write a german word in this line: "))
        try:
            return [self.english, self.german]
        except ValueError:
            print("Error! Please write this word again.")

    def __init__(self):
        self.connect = sqlite3.connect('Database_englisch_german')
        self.cusor = self.connect.cursor()
        self.combo = 0
        self.id  = 0

    def init_vocabulary(self, vocabulary=None):
        if vocabulary is None:
            vocabulary = get.get_input()
        for s in range(len(vocabulary)):
            self.english = vocabulary[0]
            self.german = vocabulary[1]
        self.cusor.execute('INSERT INTO vokabeln (english, german, combo) VALUES (?, ?, ?)', [self.english, self.german, self.combo])
        self.connect.commit()
        self.connect.close()

    def delete_vocabulary(self):
        for data in self.get_vocabulary():
            print(f'ID {data[0]}: {data[1]}, {data[2]}')
        if self.get_vocabulary() is None:
            user = input("Please write the id from the vocabulary that you'll remove: ")
            self.cusor.execute('DELETE FROM vokabeln WHERE id = ?', [user])
            self.connect.commit()
            self.connect.close()
        else:
            print("None")

    def get_vocabulary(self):
        return self.cusor.execute('SELECT * FROM vokabeln')

    def serch_id(self):
        self.id_list = []
        for id in get.get_vocabulary():
            self.id_list.append(id[0])
        return random.randint(0, self.id_list[-1])

    def seach_vocabulary(self):
        pass


get = Vocabulary()
#get.init_vocabulary()
#_list = []
#for dsatz in get.get_vocabulary():
#    _list.append(dsatz[0])
#print(_list)
#print(get.serch_id())
#get.connect.commit()
#get.connect.close()
get.delete_vocabulary()


def delete_vocabulary(self):
    for data in self.get_vocabulary():
        print(f'ID {data[0]}: {data[1]}, {data[2]}')
    if self.get_vocabulary() is None:
        user = input("Please write the id from the vocabulary that you'll remove: ")
        self.cusor.execute('DELETE FROM vokabeln WHERE id = ?', [user])
        self.connect.commit()
        self.connect.close()
    else:
        print("None")