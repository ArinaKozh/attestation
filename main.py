
import functions
while True:
    print("Введите команду: ")
    command = input()
    if command == "add":
        functions.add()
    if command == "showall":
        functions.showall()
    if command == "show":
        print("Введите id заметки: ")
        functions.show(input())
    if command == "fix":
        print("Введите id заметки: ")
        functions.fix(input())
    if command == "delete":
        print("Введите id заметки: ")
        functions.delete(input())
    if command == "stop":
        break    



