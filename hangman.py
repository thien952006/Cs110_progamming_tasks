# Author   : Xuan Thien Bui
# Email    : xuanthienbui@umass.edu
# Spire ID : 34750117


import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")
def print_revealed_phrase(word, letter_list):
  for i in range(len(word)-1):
    if(word[i].isalpha()==True):
      if(word[i] in letter_list):
        print(word[i].upper(), end='')
      else:
        print('_', end='')
    else:
      print(word[i], end='')
  if(word[len(word)-1].isalpha()==True):
    if(word[len(word)-1] in letter_list):
      print(word[len(word)-1])
    else:
      print('_')
  else:
    print(word[len(word)-1])
def get_letter(letter_list):
  while True:
    letter=input("Please enter a letter: ")
    if(letter.isalpha()==False or len(letter)>1):
      print(f"\"{letter}\" is not a letter!")
    elif(letter.isalpha()==True and letter.upper() in letter_list):
      print(f"\"{letter.upper()}\" has already been guessed!")
    elif(letter.isalpha()==True and letter.upper() not in letter_list):
      letter_list.append(letter.upper())
      return letter.upper()
def won(word, letter_list):
  change=1
  for i in range(len(word)):
    if(word[i].isalpha()==True and word[i] not in letter_list):
      change=0
  if(change==1):
    return True
  else:
    return False
def play_game():
  phrase=make_phrase()
  misses=0
  guesses=[]
  print("*** Welcome to Hangman ***")
  print_gallows(misses)
  while(misses<6):
    print_revealed_phrase(phrase,guesses)
    print(f"Letters guessed: {guesses}")
    letter=get_letter(guesses)
    guesses.sort()
    if(letter not in phrase):
      misses+=1
      print_gallows(misses)
    else:
      if (won(phrase,guesses)==True):
        print_revealed_phrase(phrase,guesses)
        print("Congratulations!")
        break  
  if(misses==6):
    print("Game Over!")
    print(f"Solution was: {phrase}")
      
    
  








      