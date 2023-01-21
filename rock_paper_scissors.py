import random
choices = ['Rock','Paper','Scissors']
Player = False
computer = random.choice(choices)
player_score=0
cpu_score=0
while True:
    Player = input('Rok, Paper, or Scissors? \n').capitalize()
    
    if Player == computer:
        print("it's a tie")
  
        
    elif Player =='Rock':
        if computer=='Paper':
            print('you lost')
            cpu_score +=1
        else:
            print('you won')
            player_score+=1
            
    elif Player=='Paper':
        if computer=='Scissors':
            print('You lost!')
            cpu_score +=1
        else:
            print('You won!')
            player_score+=1
    elif Player=='Scissors':
        if computer=='Rock':
            print('You lost!')
            cpu_score +=1
        else :
            print("you've won!")
            player_score+=1
            
    elif Player=='End':
        print('Game over! See Scores')
        print(f"computer:{cpu_score}")
        print(f"Paper:{player_score}")    
        
        break    
        