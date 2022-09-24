from tkinter import *
from tkinter import filedialog
from PIL import Image

# importing png image file
def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

# png image colors >> RGBA ( 'A' shows alpha = transparency )
# jpg image colors >> RGB ( so we want to remove transparency )
# then save it
def convertToJPG():
    global im1
    rbg = im1.convert('RGB')
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    rbg.save(export_file_path)
# Now simply call this two functions from button

# Creating tkinter window
root = Tk()
root.geometry("300x250")
root.title("Quick codes")  # give it your fav name
# set icon
# create object of image
image = PhotoImage(file = 'mrbn.png')   # make sure file is save in same folder
root.iconphoto(False, image)

# create canvas
canvas1 = Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack(fill="both")

# Make label
label1 = Label(root, text='File conversion tool', bg='azure3', fg='black')
# Give same bg color for transparency
label1.config(font="helvetica 20")
canvas1.create_window(150,60,window=label1)

# first button to import file
button_PNG = Button(text=" Import PNG file", bg='royalblue', fg='white', font='helvetica 15 bold', command=getPNG)
canvas1.create_window(150, 120, window=button_PNG)

# second button to export file
button_JPG = Button(text=" Export JPG file", bg='royalblue', fg='white', font='helvetica 12 bold', command=convertToJPG)
canvas1.create_window(150, 180, window=button_JPG)

# end of loop
root.mainloop()

