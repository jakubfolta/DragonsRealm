import random
import time

def intro():
  print('You are in the land full of dragons.\nThere are two types of these great beasts.\n')
  time.sleep(1)
  print('Good ones and bad ones.\n')
  time.sleep(1)
  print('When you meet good ones, they will bless you with their power, share with you their gold and let you live...\n')
  time.sleep(1)
  print('However, when you meet bad ones they will kill you and rob you on sight.\n')
  time.sleep(1)

def chooseRoad():
  print('You see two roads in front of you. Which one will you choose?')
  road = input('1 or 2: ')
  print()
  return road

def checkRoad(roadNum):
  time.sleep(1)
  print('You are getting further and further...')
  time.sleep(1)
  print()
  print('Suddenly dragon jumps out on your road and...')
  time.sleep(1)
  print()
  
  friendlyDragon = random.randint(1, 2)

  if friendlyDragon == roadNum:
    print('You find out that this great lizard is a good type, so are richer and happier than ever.\nHe lets you live.')
  else:
    print('Unfortunately he eats you immediately because it was an evil one.')
  print()
  time.sleep(2)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  intro()
  road = chooseRoad()
  checkRoad(int(road))
  print('Would you like to play again?')
  playAgain = input('Type yes or no: ')
  print()

print()
print('Alright, thanks for playing, bye bye!')
time.sleep(1)
exit()
