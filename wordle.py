# Author   : Xuan Thien Bui
# Email    : xuanthienbui@umass.edu
# Spire ID : 34750117


def get_guess():
    word=input("What word is this?: ")
    return (word.upper())
def print_word(word:str):
    print(word[0]+' '+word[1]+' '+word[2]+' '+word[3]+' '+word[4])
def exact_match_compare(a,b:str):
    word=""
    for i in range(5):
        if(a[i]==b[i]):
            word+= '🟢' 
        else:
            word+= '🔴'
    return word
def one_turn(word):
    guess=get_guess()
    print_word(guess)
    print(exact_match_compare(word, guess))
    if(exact_match_compare(word, guess))=='🟢🟢🟢🟢🟢':
        print("Congratulations")
        exit()

import random 
def make_solution():
    a=["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"] 
    return random.choice(a)
print(make_solution())
soln = make_solution()
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
print(f"Word was \"{soln}\", better luck next time.")



   