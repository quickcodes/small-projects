import random

str = input("Enter the sentence: ")
str = str.replace(".", " .")
lst = str.split()
new_str = ""
new_list = []
for word in lst:
    if len(word) == 3:
        char1 = word[1]
        char2 = word[2]
        word = word.replace(word[1], char2)
        word = word[:2]
        word = word + char1
    new_list = [char for char in word[1:-1]]
    random.shuffle(new_list)
    new_list.append(word[-1])
    new_list.insert(0, word[0])
    new_str += ''.join(new_list)
    new_str += " "
new_str = new_str.replace(" ..", ".")
print("\nOutput: ")
print(new_str)
input()

