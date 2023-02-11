import random 

def random_number_game():
  # Welcome message for the game
  print('Welcome to the game. Please follow the instructions carefully')
  print('Enter lower and upper limit. Both are inclusive')
  print('\nYou have 6 tries to guess the number')

  # Input for lower limit from the user
  lower_limit = int(input('Enter lower limit : '))
  # Input for upper limit from the user
  upper_limit = int(input('Enter upper limit : '))

  # Check if upper limit is less than lower limit
  if upper_limit < lower_limit:
      print('Entered limits are not correct')
      # If upper limit is less than lower limit, ask for new upper limit
      upper_limit = int(input('Enter upper limit : '))
      # Ask for new lower limit
      lower_limit = int(input('Enter lower limit : '))

  # Check if difference between limits is less than 7
  if upper_limit - lower_limit < 7:
      print('Difference between limits should be more than 6')
      # If difference between limits is less than 7, ask for new lower limit
      lower_limit = int(input('Enter lower limit : '))
      # Ask for new upper limit
      upper_limit = int(input('Enter upper limit : '))
          
  # Generate random number between lower limit and upper limit (inclusive)
  ans  = random.randrange(lower_limit,upper_limit+1)
  
  # Loop for maximum 6 tries
  for i in range(6):
      # User input for guessing the number
      user_input = int(input('Guess the number : '))
      # Check if the number is greater than user's guess
      if user_input < ans :
          print('The number is greater than your guess')
      # Check if the number is smaller than user's guess
      elif user_input > ans :
          print('The number is smaller than your guess')
      # If user's guess is correct, print message and break loop
      else:
          print('you have guessed in',(i+1),'tries')
          print('you have guessed the number correctly')  
          break
  # If user couldn't guess the number in 6 tries
  else:
    print("You couldn't guess the number correctly. ")
    print('Number was', ans)

# Call the game function
random_number_game()
