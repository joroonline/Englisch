#import sqlite3

def get_input():
    english = str(input("Please write a english word in this line: "))
    german = str(input("Please write a german word in this line: "))
    try:
        return [english, german]
    except ValueError:
        print("Error! Please write this word again.")

class Vocabulary():

    def __init__(self, vocabulary=None):
        if vocabulary is None:
            vocabulary = get_input()
        for s in range(len(vocabulary)):
            self.english = vocabulary[0]
            self.german = vocabulary[1]

get = Vocabulary()

print(get.german)