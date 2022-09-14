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
        count = 1
        for data in self.get_vocabulary():
            print(f'{count}: {data[0]}, {data[1]}')
            count += 1
        if self.get_vocabulary() is not None:
            print("True")
            user = input("Bitte schreiben Sie die Englische Vokabel in diese Zeile "
                         "um diese aus der Datenbank zu entfernen: ")
            self.cusor.execute('DELETE FROM vokabeln WHERE english = ?', [user])
            self.connect.commit()
        else:
            print("Du hast keine Vokabeln in deiner Datenbank!")

    def get_vocabulary(self):
        return self.cusor.execute('SELECT * FROM vokabeln')

    def start_questions(self, minutes):
        start = time.time()
        vocabulary = self.seach_vocabulary()

        while round(time.time()-start) < int(minutes) * 60:
            ger_or_en = random.randint(1,2)
            rand = random.randint(0, len(vocabulary[1])-1)
            if ger_or_en == 1:
                print(vocabulary[0][1])
                ger = input("Bitte schreiben Sie diese Übersetzung in diese Zeile: ")
                if ger == vocabulary[1][rand]:
                    print("It's correct :)")
                else:
                    print(f"Es ist Falsch! Das richtige wort wäre {vocabulary[1][rand]}")
            if ger_or_en == 2:
                print(vocabulary[1][rand])
                en = input("Bitte schreiben Sie diese Übersetzung in diese Zeile: ")
                if en == vocabulary[0][rand]:
                    print("It's correct :)")
                else:
                    print(f"Es ist Falsch! Das richtige wort wäre {vocabulary[0][rand]}")

    def seach_vocabulary(self):
        english_list, german_list, combo_list = [], [], []
        for data in self.get_vocabulary():
            english_list.append(data[0]), german_list.append(data[1]), combo_list.append(data[2])
        return english_list, german_list, combo_list

    def create_unit(self):
        pass

    def list_vocabulary(self):
        count = 1
        for data in self.get_vocabulary():
            print(f'{count}: {data[0]}, {data[1]}')
            count += 1


if __name__ == "__main__":
    get = Vocabulary()
    # get.init_vocabulary()
    print(get.seach_vocabulary())
