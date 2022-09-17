import random
import sqlite3
import time


def get_input():
    english = str(input("Bitte schreiben Sie ein Englisches Wort in diese Zeile: "))
    german = str(input("Bitte schreiben Sie ein Deutsches Wort in diese Zeile: "))
    try:
        return [english, german]
    except ValueError:
        print("Error! Bitte schreiben Sie diese Wörter erneut.")


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
        vocabulary = self.get_vocabulary()
        if vocabulary != None:
            count = 1
            for data in self.get_vocabulary():
                print(f'{count}: {data[0]}, {data[1]}')
                count += 1
            user = input("Bitte schreiben Sie die Englische Vokabel in diese Zeile "
                         "um diese aus der Datenbank zu entfernen: ")
            self.cusor.execute('DELETE FROM vokabeln WHERE english = ?', [user])
            self.connect.commit()
        else:
            print("Du hast keine Vokabeln in deiner Datenbank!")

    def get_vocabulary(self):
        count = 0
        get = self.cusor.execute('SELECT * FROM vokabeln')
        for data in get:
            count += 1
        if count >= 1:
            return self.cusor.execute('SELECT * FROM vokabeln')
        else:
            return None

    def start_questions(self, minutes):
        vocabulary = self.seach_vocabulary()

        if vocabulary != None:
            start = time.time()
            while round(time.time()-start) < int(minutes) * 60:
                rand = self.random_voc(vocabulary)
                if random.randint(1, 2) == 1:
                    print(vocabulary[0][rand])
                    ger = input("Bitte schreiben Sie diese Übersetzung in diese Zeile: ")
                    if ger == vocabulary[1][rand]:
                        vocabulary[2][rand] += 1
                        print("Es ist richtig :)")
                    else:
                        vocabulary[2][rand] = 0
                        print(f"Es ist Falsch! Das richtige wort wäre {vocabulary[1][rand]}")
                else:
                    print(vocabulary[1][rand])
                    en = input("Bitte schreiben Sie diese Übersetzung in diese Zeile: ")
                    if en == vocabulary[0][rand]:
                        vocabulary[2][rand] += 1
                        print("It's correct :)")
                    else:
                        vocabulary[2][rand] = 0
                        print(f"Es ist Falsch! Das richtige wort wäre {vocabulary[0][rand]}")
        else:
            print("Du hast keine Vokabeln in deiner Datenbank!")

    def seach_vocabulary(self):
        vocabulary = self.get_vocabulary()
        if vocabulary != None:
            english_list, german_list, combo_list = [], [], []
            for data in vocabulary:
                english_list.append(data[0]), german_list.append(data[1]), combo_list.append(data[2])
            return english_list, german_list, combo_list
        else:
            return None

    def random_voc(self, vocabulary):
        count = 0
        for i in vocabulary:
            count += 1

        while True:
            rand = random.randint(0, count-1)
            combo = vocabulary[2][rand]
            if combo >= 10:
                vocabulary[2][rand] = 10
                combo = 10
            if random.randint(0,combo) == combo:
                return rand

    def list_vocabulary(self):
        vocabulary = self.get_vocabulary()
        if vocabulary != None:
            count = 1
            for data in vocabulary:
                print(f'{count}: {data[0]}, {data[1]}')
                count += 1
        else:
            print("Du hast keine Vokabeln in deiner Datenbank!")


if __name__ == "__main__":
    get = Vocabulary()
    # get.init_vocabulary()
    vocabulary = get.get_vocabulary()
    get.start_questions(1)
