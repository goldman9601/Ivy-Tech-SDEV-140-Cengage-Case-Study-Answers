import random#import package

print("This is a number guessing game.")#print message

print("Guess what number we thought of between 1 and 100")#print message

n = random.randrange( 100 ) + 1#defining a variable n that uses random method that holds a value  

while True:#defining a loop to input value and check value

   guess = int(input('Enter your best guess!\n'))#defining a variable guess that inputs value

   if guess == n:#defining if block that check the random number

       print("Congrats, you won!")#print message

       print("Restarting game") #print message

       n = random.randrange( 100 ) + 1 #calling random method that holds a value

   elif guess < n:#defining elif that check random number value less than inputs

       print('too low,try again')#print message

   else:#defining else block

       print('too high try again.')#print message