#display art 
from art import logo
from art import vs
from game_data import data
import random
#score computation

#compare various inputs 
def maxmus(inputdata,value1,value2):
  maxvalue=max(value1,value2)
  if inputdata=='a':
    compvalue=value1
  elif inputdata=='b':
    compvalue=value2
  if maxvalue>compvalue:
    print("you're winning!!!")
    return True
  else:
    print("you lose!!")
    return False
#format data 
def format(sq,p,q,r):
  print(f"compare {sq}:{p},{q},from {r}")




print(logo)
#generate random value
random_a=random.choice(data)
score=0
a=True
while a:
  random_b=random.choice(data)
  if random_a==random_b:
    random_b=random.choice(data)
  #format data 
  format('A',random_a['name'],random_a['description'],random_a['country'])
  print(vs)
  format('B',random_b['name'],random_b['description'],random_b['country'])
#compare value 
##follower number 
##if to estimate user correctness
  inputdata=input("who has the most followers? type A or B ").lower()
  returnvalue=maxmus(inputdata,random_a['follower_count'],random_b['follower_count'])
#give feedback to the guess
  if returnvalue==True:
    score+=1
    print("your score=",score)
    random_a=random_b
    a=True
  else:
    a=False
    print("your final score=",score)
    
    

#score calculation
  