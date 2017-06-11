import sqlite3
from prettytable import PrettyTable
from colorama import init,Fore,Style

def getAll():
    con = sqlite3.connect("hero.db")
    cursor = con.execute("select * from heros")

    x = PrettyTable(['id','title','name','passivity','Q','W','E','R'])
    x.align['name'] = 'l'
    x.padding_width = 1
    for row in cursor:
        x.add_row([row[0],row[1],row[2],row[3],row[5],row[7],row[9],row[11]])

    init(autoreset=True)
    print Fore.RED + Style.BRIGHT+ 'Heros'
    print x



if __name__ == "__main__":
    getAll()