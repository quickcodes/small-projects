
sum = 0
while(True):
    userInput = input("Enter the price: \n")
    if(userInput != 'q'):
        operation = input("operation \n")
        if(operation == '+'):
            sum = sum+ int(userInput)
            print(f"order total so far: {sum}")
        elif(operation == '-'):
            sum = sum- int(userInput)
            print(f"order total so far: {sum}")
        elif (operation == '/'):
            sum = sum / int(userInput)
            print(f"order total so far: {sum}")
        elif (operation == '*'):
            sum = sum * int(userInput)
            print(f"order total so far: {sum}")
        else:
            print("Enter the right operation")
    else:
        print("Thanks for using our shop")
        print(f"Your total bill is {sum}")
        break
