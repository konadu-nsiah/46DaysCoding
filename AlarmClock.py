from datetime import datetime
from playsound import playsound
import pygame
import  time
# Takes user input for time
alarm = input('Enter the time for your alarm in dd-mm-yyyy HH:MM:SS \n')
#converts user input to datetime object

# now takes the current datetime


print('setting up alarm ...')
pygame.init()

while True:
    new = datetime.strptime(alarm,"%d-%m-%Y %H:%M:%S")
    print(new)
    now = datetime.now()
    print(now)
 
    # alarm rings if the user input is equal to the current datetime.
    if(now >=new):
            print('WAKE UP!!!!!')
            pygame.mixer.music.load('02. Beautiful Day.mp3')
            pygame.mixer.music.play()
            break
        # the loop sleeps for the seconds before the user input is equal to the current datetime
    time.sleep(60)
    