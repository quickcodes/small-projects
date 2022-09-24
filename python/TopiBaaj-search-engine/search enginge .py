# Automated google map
# You dont need to type anything here just simply copy any thing and run this program even you don't to paste here just run the program that's it

import webbrowser  # to open webbrowser
import sys    #  get text form terminal
import pyperclip   # get text from clipboard
if len(sys.argv) > 1:     # if file of text is more than a file it means it will return more than 1
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

# print(address)
print('''Hey what you wanna do .
1. Search it on google
2. search it on google map 
3. search it on instagram 
4. Search it on facebook
5. Search it on Youtube
6. Search it on any other plateform 
''')

num = (input("Enter here: "))
try:
    if num == '1':
        webbrowser.open('https://www.google.com/search?q=' + address)
    elif num == '2':
        webbrowser.open('https://www.google.com/maps/place/' + address)
    elif num == '3':
        webbrowser.open('https://www.instagram.com/' + address)
    elif num == '4':
        webbrowser.open('https://www.facebook.com/' + address)
    elif num == '5':
        webbrowser.open('https://www.youtube.com/results?search_query=' + address)
    elif num == '6':
        url = input("enter the name of URL: ")
        webbrowser.open(f'https://www.{url}.com/' + address)
    else:
        print("Pagal h kya ")
except KeyboardInterrupt:
    print("Marna h kya terko saale")