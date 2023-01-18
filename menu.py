from os import system, name

def options():
    print("(1) 25-minute timer\n(2) 5-minute break\n(3) 10-minute break")

#"pause" from fitness-optimizer project, to break loop 
def pause():
  print('\n')
  global response
  response = input('Press any key to continue.')
  while True:
    break

#Clear screen from fitness-optimizer
def clear():
  #Windows clear screen
  if name == 'nt':
    _ = system('cls')
  #Linux/Mac clear screen
  else:
    _ = system('clear')
