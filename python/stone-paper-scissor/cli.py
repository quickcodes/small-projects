import random
def gameWin(comp , you):
    if comp == you:
        return None

    elif comp == 'st':
        if you == 'pa':
            return True
        elif you == 'sc':
            return False

    elif comp == 'pa':
        if you == 'sc':
            return True
        elif you == 'st':
            return False

    elif comp == 'sc':
        if you == 'st':
            return True
        elif you == 'pa':
            return False

def frog():
    print(''' _______
    < Hello! >
     -------
         \\
          \\
              oO)-.                       .-(Oo
             /__  _\                     /_  __\\
             \  \(  |     ()~()         |  )/  /
              \__|\ |    (-___-)        | /|__/
              '  '--'    ==`-'==        '--'  '
            /
           /
     ------- ''')

def daemon():
    print(''' _______
< Na tum jite na ham! Tie hogya >
 -------
   \         ,        ,
    \       /(        )`
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\\
           / /   | `    \\
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \\
<----|====O)))==) \) /====
<----'    `--' `.__,' \\
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \\
      `--{__________)        \/   ''')

def milkman():
    print(''' _______
< Ham jit gye saheb! Try again >
 -------
 \     ____________
  \    |__________|
      /           /\\
     /           /  \\
    /___________/___/|
    |          |     |
    |  ==\ /== |     |
    |   O   O  | \ \ |
    |     <    |  \ \|
   /|          |   \ \\
  / |  \_____/ |   / /
 / /|          |  / /|
/||\|          | /||\/
    -------------|
        | |    | |
       <__/    \__>''')

def dragon():
    print(''' _______
< Badhai ho tum jite ho dragon ka baccha!... >
 -------
      \                    / \  //\..
       \    |\___/|      /   \//  \\\..
            /0  0  \__  /    //  | \ \..
           /     /  \/_/    //   |  \  \..
           @_^_@'/   \/_   //    |   \   \..
           //_^_/     \/_ //     |    \    \..
        ( //) |        \///      |     \     \..
      ( / /) _|_ /   )  //       |      \     _\..
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \\\\..
 (( /// ))      `.   {            }                   /      \  \\\\..
  (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
             ///.----..>        \             _ -~             `.  ^-`  ^-_
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                  /.-~''')


while True:
    randNo = random.randint(1, 3)
    # print(randNo)
    if randNo == 1:
        comp = 'st'
    elif randNo == 2:
        comp = 'pa'
    elif randNo == 3:
        comp = 'sc'

    # print("\nYour's Turn: Stone(st) Paper(pa) scissors(sc) ? ")
    frog()
    you = input(" < Tumhari bari: Stone(st) Paper(pa) scissors(sc) ? > ")
    a = gameWin(comp, you)
    print(f"\n\nApne chuna < {you} >")
    print(f" Or computer ne chuna < {comp} >")

    if a == None:
        # print("\nThe game is tie! 👍🏻 ")
        daemon()
    elif a:
        # print("\nHurrah....You Win a cow ! 🤘🏻 👌🏻 👍🏻 ")
        dragon()

    else:
        # print("You lose!")
        milkman()

    print("\n\n\n< Maidan m utarne k leye koi si key press kre >")
    print(" < Mu chup k bhagne k leye 'n' dabaye > ")
    i = input("--> ")
    if (i == 'n'):
        break



