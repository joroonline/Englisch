import sqlite3
from time import time
from random import randint


def get_input():
    english = str(input("Please write a english word in this line: "))
    german = str(input("Please write a german word in this line: "))
    try:
        return [english, german]
    except ValueError:
        print("Error! Please write this word again.")


class Vocabulary:
    def __init__(self):
        self.connect = sqlite3.connect('Database_englisch_german')
        self.cusor = self.connect.cursor()
        self.combo = 0
        self.english = ""
        self.german = ""
        self.vocabulary = None

    def init_vocabulary(self):
        if self.vocabulary is None:
            self.vocabulary = get_input()
        for s in range(len(self.vocabulary)):
            self.english = self.vocabulary[0]
            self.german = self.vocabulary[1]
        self.cusor.execute('INSERT INTO vokabeln (english, german, combo) VALUES (?, ?, ?)',
                           [self.english, self.german, self.combo])
        self.connect.commit()

    def delete_vocabulary(self):
        count = 1
        for data in self.get_vocabulary():
            print(f'{count}: {data[0]}, {data[1]}')
            count += 1
        if self.get_vocabulary() is not None:
            print("True")
            user = input("Please write the english vocabulary that you'll remove: ")
            self.cusor.execute('DELETE FROM vokabeln WHERE english = ?', [user])
            self.connect.commit()
        else:
            print("You doesn't have any vocabulary in your database!")

    def get_vocabulary(self):
        return self.cusor.execute('SELECT * FROM vokabeln')

    def start_questions(self, time, vocabulary):
        if vocabulary is not False:
            english = vocabulary[0]
            german = vocabulary[1]
            combo = vocabulary[2]

    def seach_vocabulary(self):
        english_list = []
        german_list = []
        combo_list = []
        for data in self.get_vocabulary():
            english_list.append(data[0])
            german_list.append(data[1])
            combo_list.append(data[2])
        return english_list, german_list, combo_list

    def create_unit(self):
        pass


if __name__ == "__main__":
    get = Vocabulary()
    # get.init_vocabulary()
    print(get.seach_vocabulary())
