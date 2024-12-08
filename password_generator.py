from random import choices
from random import shuffle
from math import floor
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
def password_generator(length):
    upper=choices(ascii_uppercase,k=floor(length*0.25))
    lower=choices(ascii_lowercase,k=floor(length*0.25))
    numbers=choices(digits,k=floor(length*0.25))
    special=choices(punctuation, k=length-(floor(length*0.25)*3))
    upper.extend(lower)
    upper.extend(numbers)
    upper.extend(special)
    shuffle(upper)
    password=''.join(upper)
    return password
print(password_generator(int(input())))

