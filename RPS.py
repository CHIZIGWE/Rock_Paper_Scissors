import random
choices = ['Rock', 'Paper', 'Scissors']

P = 'Player 1 wins' #Storing the message if the Player wins
C = 'CPU wins' #Storing the message if the CPU wins
D = 'A Draw' #Storing the message if it is a draw
P1 = input('Please make a choice ') #prompting the player to make choice
print()
CPU = random.choice(choices) #Automated mechanism to stimulate a CPU choice

print(f"Player 1 choice: {P1}\n") #To show the Player's choice for reference
print(f'CPU choice: {CPU}\n') #To show the CPU's choice for reference


if P1 == 'Rock':
    if CPU == 'Paper':
        print(C)

    elif CPU == 'Scissors':
        print(P)

    else:
        print(D)

if P1 == 'Paper':
    if CPU == 'Scissors':
        print(C)

    elif CPU == 'Rock':
        print(P)

    else:
         print(D)

if P1 == 'Scissors':
    if CPU == 'Rock':
        print(C)

    elif CPU == 'Paper':
        print(P)

    else:
        print('A Draw')
