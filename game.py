import random
import time
import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Rategame by Ben Winter")

clear = lambda: os.system('cls')
leer = " "
strich = "----------------------------------------------------------"

def game():
    tries = 0
    done = False
    leer = " "
    resultpoints = points

    print(f"Starten sie das Spiel, indem sie eine Zahl zwischen {schwierigkeit} eingeben")
    print("----------------------------------------------------------")

    while not done:
        guess = int(input("Geben sie ihren Versuch ein: "))
        if guess == number:
            done = True
            print("-----------------END------------------")
            print("Du hast gewonnen!")
            print(leer)
            print(f"Die Nummer lautete: {number}")
        else: 
            print(" ")
            tries +=1
            resultpoints-=trypoints
            if guess > maxguess:
                print(f"Sie können nur Zahlen bis {maxguess} auswählen!")
            else:
                if guess > number:
                    print("Die Nummer ist kleiner")
                elif guess < number:
                    print("Die Nummer ist größer")

    print(f"Du brauchtest {tries} Versuche!")
    #resultpoints = points -(tries*trypoints)
    print(f"Du hast {resultpoints} Punkte erreicht!")
    print(strich)
    restart()

def restart():
    print(leer)
    ask = str(input("Möchten sie wiederholen? (Ja/Nein): "))
    if ask == "Ja" or ask == "ja":
        clear()
        print()
        menu()
        option = int(input("Bitte nennen sie ihre Auswahl: "))
        while option:
            if option == 0:
                print("Vielen Dank fürs spielen")
                break
            elif option == 1:
                number = random.randint(0, 1000)
                resultpoints = 0
                points = 500
                trypoints = 20
                maxguess = 1000
                schwierigkeit = "1 und 1000"
                print(leer)
                print("Sie haben die Schwierigkeit Leicht ausgewählt")
                print(strich)
                time.sleep(1)
                clear()
                game()
                pass
            elif option == 2:
                number = random.randint(0, 5000)
                resultpoints = 0
                points = 2500
                trypoints = 100
                maxguess = 5000
                schwierigkeit = "1 und 5000"
                print(leer)
                print("Sie haben die Schwierigkeit Mittel ausgewählt")
                print(strich)
                time.sleep(1)
                clear()
                game()
                pass
            elif option == 3:
                number = random.randint(0, 10000)
                resultpoints = 0
                points = 5000
                trypoints = 500
                maxguess = 10000
                schwierigkeit = "1 und 10000"
                print(leer)
                print("Sie haben die Schwierigkeit Schwer ausgewählt")
                print(strich)
                time.sleep(1)
                clear()
                game()
                pass
            else:
                print("Bitte nehmen sie eine Gültige Schwierigkeite")
                pass
                print()
                menu()
                option = int(input("Bitte nennen sie ihre Auswahl: "))
    elif ask == "Nein" or ask == "nein":
        print(strich)
        print("Vielen Dank fürs Spielen")
        exit()
    else:
        print(leer)
        print("Ihre Eingabe war ungültig")
        restart()



def menu():
    clear()
    print(strich)
    print("Willkommen zum Nummer Rate Spiel Menü")
    print("[1] Leicht: Zahl zwischen 1 und 1000 (500 Startpunkte)")
    print("[2] Mittel: Zahl zwischen 1 und 5000 (2500 Startpunkte)")
    print("[3] Schwer: Zahl zwischen 1 und 10000 (5000 Startpunkte)")
    print("[4] Regeln / FaQ")
    print("[0] Beenden sie das Programm")
    print(strich)

def regeln():
    print("Willkommen zu den Regeln des Ratespiels.")
    input("Drücken sie Enter, um die Regeln aufzurufen...")
    print(leer)
    print("Es gibt insgesamt 3 Spielmodi, die sich nur in der Schwierigkeit unterscheiden.")
    print("Leicht, Mittel und Schwer.")
    print("Die einzigen Unterschiede sind hierbei die Anzahl der Punkte mit denen sie starten, und die Anzahl der Punkte die bei einem Versuch abgezogen werden.")
    print(leer)
    print("Bei Leicht starten sie mit 500 Punkten und pro Versuch werden ihnen 20 Punkte abgezogen.")
    print("Bei Mittel starten sie mit 2500 Punkten (Immer die Hälfte der maximal möglichen Zahl) und es werden 100 Punkte pro Versuch abgezogen.")
    print("Bei Schwer starten sie mit 5000 Punkten und es werden pro Versuch 500 Punkte abgezogen. ")
    input("Drücken sie Enter um Fortzufahren...")
    print("Sollten ihre Punkte ausgehen, haben sie verloren.")

menu()
option = int(input("Bitte nennen sie ihre Auswahl: "))

while option:
    if option == 0:
            print("Vielen Dank fürs spielen")
            break
    elif option == 1:
        number = random.randint(0, 1000)
        resultpoints = 0
        points = 500
        trypoints = 20
        maxguess = 1000
        schwierigkeit = "1 und 1000"
        print(leer)
        print("Sie haben die Schwierigkeit Leicht ausgewählt")
        print(strich)
        time.sleep(1)
        clear()
        game()
        pass
    elif option == 2:
        number = random.randint(0, 5000)
        resultpoints = 0
        points = 2500
        trypoints = 100
        maxguess = 5000
        schwierigkeit = "1 und 5000"
        print(leer)
        print("Sie haben die Schwierigkeit Mittel ausgewählt")
        print(strich)
        time.sleep(1)
        clear()
        game()
        pass
    elif option == 3:
        number = random.randint(0, 10000)
        resultpoints = 0
        points = 5000
        trypoints = 500
        maxguess = 10000
        schwierigkeit = "1 und 10000"
        print(leer)
        print("Sie haben die Schwierigkeit Schwer ausgewählt")
        print(strich)
        time.sleep(1)
        clear()
        game()
        pass
    elif option == 4:
        clear()
        regeln()
    else:
        print("Bitte nehmen sie eine Gültige Schwierigkeite")
        pass

    print()
    menu()
    option = int(input("Bitte nennen sie ihre Auswahl: "))