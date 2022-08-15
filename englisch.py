#import sqlite3

def database():
    #connection = sqlite3.connect('Database_english_german')
    #cursur = connection.cursor()
    #return cursur
    pass

def new_vocabulary():
    while True:
        german = str(input("Please write a german word in this line: "))
        english = str(input("Please write a english word in this line: "))
        try:
            return [german, english]
        except ValueError:
            print("Please write this words again!")

def get_id():
    pass

#def new_voc_init(new_vocabulary):
#    for x, y in enumerate(new_vocabulary):
#        print(f"{x+1}. {y}")

if __name__ == "__main__":
    print(x for x, y in enumerate(new_vocabulary()))

#cursur.execute()