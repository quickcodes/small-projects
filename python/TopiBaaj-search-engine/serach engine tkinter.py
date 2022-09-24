from tkinter import *
from tkinter import messagebox as msg
import webbrowser  # to open web-browser
import sys    #  get text form terminal
import pyperclip   # get text from clipboard

global address
if len(sys.argv) > 1:     # if file of text is more than a file it means it will return more than 1
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

# main
root = Tk()

winWidth = root.winfo_reqwidth()
winHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - winWidth/2)
positionDown = int(root.winfo_screenheight()/2 - winHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))


# root.geometry("270x310") #250,250
root.resizable(0,0)
root.title("Pocket Search Pack")
# background image
root.config(bg="skyblue")

Label(text="Hey what you wanna do:", fg="blue", bg="white", font="TimesNewRoman 16", justify='center', padx=20, pady=10).grid(row=0, column=3)

num = IntVar()

def op1():
    try:

            webbrowser.open('https://www.google.com/maps/place/')
    except:
        msg.showerror(text="Marna hai kya teroko...??")

def op2():
    try:

            webbrowser.open('https://www.instagram.com/')
    except:
        msg.showerror(text="Marna hai kya teroko...??")
def op3():
    try:

            webbrowser.open('https://www.facebook.com/')
    except:
        msg.showerror(text="Marna hai kya teroko...??")

url = StringVar()

def callback(url):
    if url.isdigit():
        print(url)
        return True
    elif url == " ":
        print(url)
        return True
    else:
        print(url)
        return False

def get_val():
    # print(f"{url.get()}") # to get URL on terminal
    webbrowser.open(f'https://www.{url.get()}.com/')

def op4():
    try:
        newWin = Toplevel(root)
        newWin.title("Search Somewhere else")

        winWidth = root.winfo_reqwidth()
        winHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
        positionDown = int(root.winfo_screenheight() / 2 - winHeight / 2)
        newWin.geometry("+{}+{}".format(positionRight, positionDown))

        # newWin.geometry("350x200")
        newWin.resizable(0,0)
        newWin.config(bg="skyblue")
        Label(newWin, text="Name of other Platform: ", bg="skyblue", fg="green", font="TimesNewRoman 15 bold", highlightthickness=5, pady=5).pack()
        # url = StringVar()
        ent = Entry(newWin, textvariable=url, highlightthickness=2, justify='center', width='35', font="TimesNewRoman 12").pack(pady=5)
        Button(newWin, text="Search...", command=get_val, padx=5, pady=5, font="TimesNewRoman 14", fg="black", bg="#6495ed").pack(padx=5, pady=5)

        Button(newWin, text="Quit", command=newWin.destroy, padx=10, pady=5, font="TimesNewRoman 14", bg="#ff4500", fg="black").pack(padx=5, pady=5)

        # def get_val():
        '''
         validate entry text
         '''
        # webbrowser.open(f'https://www.{url}.com/' + address)

        newWin.mainloop()
    except:
        msg.showinfo("Error","Unable to Load...!!")
        newWin.destroy()


Button(text="Search on google map", bg="#1e90ff", fg="white", font="TimesNewRoman 14", command=op1, justify="center").grid(
    row=1, column=3, padx=5, pady=5)
Button(text="Search on instagram", bg="#6495ed", fg="black", font="TimesNewRoman 14", command=op2, justify="center").grid(
    row=2, column=3, padx=5, pady=5)
Button(text="Search on facebook", bg="#00cee1", fg="black", font="TimesNewRoman 14", command=op3, justify="center").grid(
    row=3, column=3, padx=5, pady=5)
Button(text="Search on other Platform", bg="#00cea1", fg="black", font="TimesNewRoman 14", command=op4, justify="center").grid(
    row=4, column=3, padx=5, pady=5)
Button(text="Quit", command=root.destroy, padx=10, pady=5, font="TimesNewRoman 14", bg="#20b2aa",
       fg="blue", justify='center').grid(padx=5, pady=5, row=5, column=3)

root.mainloop()

