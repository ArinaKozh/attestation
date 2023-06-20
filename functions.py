import json
from datetime import datetime 
from datetime import time
def add():
    with open("notes.json", "r") as f:
        notes = json.load(f)
        n = len(notes)
        print("Введите заметку")
        note = input()
        notes[n+1]=[note, f'{datetime.now():%Y-%m-%d %H:%M:%S%z}']
    with open("notes.json", "w") as f:
        json.dump(notes,f)
    print("Заметка успешно добавлена")

def showall():
    with open("notes.json", "r") as f:
        notes = json.load(f)
        for key, value in sort_notes().items():
            print('id: %s note: %s  time: %s\n' % (key, value[0], value[1]))
def show(id):
    ifExists = 0
    with open("notes.json", "r") as f:
        notes = json.load(f)
        for key, value in notes.items():
            if id==key:
                ifExists = 1
                print('id: %s note: %s  time: %s\n' % (key, value[0], value[1]))
        if ifExists == 0:
            print("Такой заметки нет")

def fix(id):
    ifExists = 0
    with open("notes.json", "r") as f:
        notes = json.load(f)
        for key, value in notes.items():
            if id==key:
                ifExists = 1
                print("Введите новую заметку: ")
                note = input()
                notes[id]=[note, f'{datetime.now():%Y-%m-%d %H:%M:%S%z}']
        if ifExists == 0:
            print("Такой заметки нет")
    with open("notes.json", "w") as f:
        json.dump(notes,f)

def delete(id):
    ifExists = 0
    with open("notes.json", "r") as f:
        notes = json.load(f)
        try:
            del notes[id]
            ifExists = 1
        except:
            print("Такой заметки нет")
        for key in notes.keys():
                if int(key)>int(id):
                    key = str(int(key)-1)
        if ifExists == 0:
            print("Такой заметки нет")
    with open("notes.json", "w") as f:
        json.dump(notes,f)
def sort_notes():
    dates=[]
    sorted = {}
    with open("notes.json", "r") as f:
        notes = json.load(f)
        for value in notes.values():
            dates.append(datetime.strptime(value[1],"%Y-%m-%d %H:%M:%S"))
        dates.sort()
        for date in dates:
            for key, value in notes.items():
                if date == datetime.strptime(value[1],"%Y-%m-%d %H:%M:%S"):
                    sorted[key] = value
    return sorted