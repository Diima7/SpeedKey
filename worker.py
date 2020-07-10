import sqlite3, time, os
import keyboard
conn = sqlite3.connect('database.db')
c = conn.cursor()
data = []
for row in c.execute('SELECT * FROM keys'):
    print(row[0], row[1])
    keyboard.add_hotkey(row[0], lambda : os.system("python3 scripts/" + row[1] + ".py"))
    data.append(row)
keyboard.wait('esc')
