The Hangman game is a classic word-guessing game that challenges players to identify a hidden word one letter at a time.
The game is designed to be both educational and entertaining, improving vocabulary and spelling skills.
Players are given a series of blanks representing the letters in the word, and they must guess letters to fill in the blanks.
Incorrect guesses lead to the drawing of a "hangman," a stick figure that is incrementally drawn with each wrong guess. 

import random
list=['sainath','dinesh','karthik','rushil','ganesh','tharun','pavan','ram']
word=random.choice(list)
hangs=['''
       =====|
       |    |
       |    |
       O    |
            |
            |
          ===== 
       ''','''
       =====|
       |    |
       |    |
       O    |
       |    |
            |
          ===== 
       ''','''
       =====|
       |    |
       |    |
       O    |
       |\   |
            |
          ===== 
       ''','''
       =====|
       |    |
       |    |
       O    |
      /|\   |
            |
          ===== 
       ''','''
       =====|
       |    |
       |    |
       O    |
      /|\   |
      /     |
          ===== 
       ''','''
       =====|
       |    |
       |    |
       O    |
      /|\   |
      / \   |
          ===== 
       '''
]
display=[]
for i in range(len(word)):
   display.append('_')
print(display)
game_on=True
lifes=-1
while game_on:
   guess=input('choose a letter:').lower()
   if guess in word:
      for i in range(len(word)):
         if guess == word[i]:
            display[i]=guess
      print(display)
   else:
      lifes+=1
      print(hangs[lifes])
   if lifes == 5:
      game_on=False
      print('YOU LOSE')
   if '_' not in display:
     game_on=False
      print('YOU WIN')
