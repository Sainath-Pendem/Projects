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
lifes=6
while game_on:
   guess=input('choose a letter:').lower()
   if guess in word:
      for i in range(len(word)):
         if guess == word[i]:
            display[i]=guess
      print(display)
   else:
      lifes-=1
      print(hangs[lifes])
   if lifes == 0:
      game_on=False
      print('YOU LOSE')
   if '_' not in display:
     game_on=False
      print('YOU WIN')
