secret_number = 7
# Using While Loop To Allow Multiple Attempts:
while True:
    guess = int(input("Enter Your Guess:"))
    if (guess > secret_number):
         print( "Too high " )
    elif( guess < secret_number):
         print ( "Too low")
    else:
         print("You've guessed it right")
         break 