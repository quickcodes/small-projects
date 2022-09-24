# Random password genertor
import string
import random


if __name__ == '__main__':
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    passlen = int(input("Enter the length of password: "))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # print(s)
    random.shuffle(s)
    # print(s)
    print("".join(s[0:passlen]))   # shuffle value ko print karega
    print("".join(random.sample(s,passlen)))  # s k andar se passlen tak k random vaules nikal k dega
