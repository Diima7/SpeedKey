import os, time, keyboard, sqlite3
from pathlib import Path

class main():
    def __init__(self):
        databasecheck = Path('database.db')
        dbcheck = False
        if databasecheck.is_file():
            dbcheck = True
        

        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        if dbcheck == False:
            self.c.execute('CREATE TABLE keys(key text, script text)')

        scriptdir = Path("/scripts")
        if scriptdir.is_dir():
            self.start()
        else:
            os.system('mkdir scripts')
            self.start()

    

    def createScript(self):
        while True:
            name = input('Name of the Script?\n')
            checker = Path("/scripts/" + name + ".py")
            if checker.is_file():
                print("Already exists")
            else:
                break
        while True:
            firstkey = ""
            os.system("clear")
            time.sleep(0.5)
            print('Press and release your desired shortcut')
            shortcut = keyboard.read_hotkey()
            print('Shortcut selected:', shortcut)
            print('Name: {}\nKey: {}\nIs everything right ? (y)es/(n)o'.format(name,shortcut))
            x = input("-->").lower()
            if not x == "n" or x == "no":
                open('scripts/' + name + '.py', 'w+')
                self.c.execute("INSERT INTO keys VALUES ('{}','{}')".format(shortcut, name))
                self.conn.commit()
                break
                 

    def start(self):
        while True:
            os.system("clear")
            print("1. Create Script\n2. Delete Script\n3. Exit\n")
            x = input("-->")
            
            if int(x) == 1:
                self.createScript()
            elif int(x) == 2:
                pass
            elif int(x) == 3:
                self.conn.close()
                break



main()
