import random
import string
import time
import getpass


def lowerCase():
    lc = string.ascii_lowercase
    char_lst = list(lc)
    pswd = getpass.getpass("\n       Enter the password: ")
    startTime = time.time()
    print("       Cracking...")
    guess = ""
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        guess = "".join(guess)
    timetaken = round(time.time() - startTime, 3)
    print("       It took %s seconds to Crack." % timetaken)
    print("       Password is: " + guess)


def upperCase():
    uper = string.ascii_uppercase
    char_lst = list(uper)
    pswd = getpass.getpass("\n       Enter the password: ")
    startTime = time.time()
    print("       Cracking...")
    guess = ""
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        guess = "".join(guess)
    timetaken = round(time.time() - startTime, 3)
    print("       It took %s seconds to Crack." % timetaken)
    print("       Password is: " + guess)


def digits():
    digit = string.digits
    char_lst = list(digit)
    pswd = getpass.getpass("\n       Enter the password: ")
    startTime = time.time()
    print("       Cracking...")
    guess = ""
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        guess = "".join(guess)
    timetaken = round(time.time() - startTime, 3)
    print("       It took %s seconds to Crack." % timetaken)
    print("       Password is: " + guess)


def mixword():
    words = string.ascii_letters
    char_lst = list(words)
    pswd = getpass.getpass("\n       Enter the password: ")
    startTime = time.time()
    print("       Cracking...")
    guess = ""
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        guess = "".join(guess)
    timetaken = round(time.time() - startTime, 3)
    print("       It took %s seconds to Crack." % timetaken)
    print("\n       Password is: " + guess)


def wordsDigits():
    lc = string.ascii_letters
    dgt = string.digits
    char_lst = list(lc + dgt)
    pswd = getpass.getpass("\n       Enter the password: ")
    startTime = time.time()
    print("       Cracking...")
    guess = ""
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        guess = "".join(guess)
    timetaken = round(time.time() - startTime, 3)
    print("       It took %s seconds to Crack." % timetaken)
    print("       Password is: " + guess)


def fuckingCrazy():
    lc = string.printable
    char_lst = list(lc)
    pswd = getpass.getpass("\n       Enter the password: ")
    startTime = time.time()
    print("       Cracking...")
    guess = ""
    while guess != pswd:
        guess = random.sample(char_lst, k=len(pswd))
        # print(guess)
        guess = "".join(guess)
    timetaken = round(time.time() - startTime, 3)
    print("       It took %s seconds to Crack." % timetaken)
    print("       Password is: " + guess)


if __name__ == '__main__':
    end = ''
    while end != 'q':
        print()
        print("       Which type of password I want to guess")
        print('''     < Please choose the complexity of password >
        1. Lower case
        2. Upper case
        3. Digits
        4. Mix words
        5. words and Numbers
        6. Crazy
        ''')

        try:
            num = int(input("    --> "))
            if num == 1:
                lowerCase()
            elif num == 2:
                upperCase()
            elif num == 3:
                digits()
            elif num == 4:
                mixword()
            elif num == 5:
                wordsDigits()
            elif num == 6:
                fuckingCrazy()
            else:
                print("\n       < Please enter valid number >")
        except:
            print("       Ulta sidha mat type kar...")

        print("\n       Press any key to play again and 'q' for exit")
        end = input("    --> ")
        if end == 'q':
            print("       Bye Bye")
            time.sleep(2)

