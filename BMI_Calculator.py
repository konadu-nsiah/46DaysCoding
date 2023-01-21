# In this code we are going to create an algorithm for finding the Body Mass Weight for user and to indicate whether the individual is uderweight, heathly or overweight.
print('Welcome to your BMI Calculator!')
Weight = int(input('Kindly enter your weight in kg \n'))
Length = int(input('Enter your height in cm \n'))
length =Length / 100
Area = length * length
BMI = Weight / Area
if BMI <= 16:
    print("You're underweight")
elif BMI <= 24.9:
    print("You're healthy")
elif BMI >= 25.0:
    print("You're overweight")