# In this game, I will create questions and answer verfcation system (the guess_checker function).
# The player is given 3 attempts to answer each question correctly
def guess_checker(guess, answer, score):
    # Global is used here because the score has been definded outside the function and we want be modifying the score.
    still_guessing =True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score+1
            still_guessing =False
        else:
            if attempt < 2:
                guess = input('Sorry Wrong Answe, try again \n')    
                attempt = attempt + 1
                
                
            while  attempt == 3:
                print('The Correct answer is ', answer)
                print(answer)
    return score
   

score= 0
print('Guess the answer')
guess1 = input("Who is Ghana's first president? \n")
guess_checker(guess1,'Osagyefo Dr. Kwame Nkrumah', score)
guess2 = input("Which year did Ghana gain independence? \n")
guess_checker(guess2,'1957', score)
guess3 = input("Which year dd free SHS commence? \n")
guess_checker(guess3,'2017', score)
print(f'Your Score is {str(score)}')