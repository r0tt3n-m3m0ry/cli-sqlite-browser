try:
    import prettytable
except ImportError:
    print(''); exit()

import ssqlite3
import os

def clear_screen():
    os.system('cls') if os.name == 'nt' else os.system('clear')

clear_screen()

db = sqlite3.connect(input('Enter name of Sqlite database file (with extention): '))
sql = db.cursor()


