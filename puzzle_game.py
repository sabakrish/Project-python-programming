# puzzle game example
import random   
# Define the puzzle pieces
pieces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# Shuffle the pieces to create a random puzzle
random.shuffle(pieces) 
# Function to display the puzzle
def display_puzzle(puzzle):
    for i in range(0, len(puzzle), 3):
        print(' | '.join(puzzle[i:i+3]))
        print('-' * 9)
# Display the shuffled puzzle
print("Here is your shuffled puzzle:")
display_puzzle(pieces)
# Function to check if the puzzle is solved
def is_solved(puzzle):
    return puzzle == ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# Main game loop
while True:
    move = input("Enter two positions to swap (1-9) or 'q' to quit: ") #
    if move.lower() == 'q':
        print("Thanks for playing!")
        break
    try:
        pos1, pos2 = map(int, move.split()) # Get positions to swap
        if pos1 < 1 or pos1 > 9 or pos2 < 1 or pos2 > 9: #
            print("Invalid positions. Please enter numbers between 1 and 9.")
            continue
        # Swap the pieces
        pieces[pos1-1], pieces[pos2-1] = pieces[pos2-1], pieces[pos1-1]
        display_puzzle(pieces)
        if is_solved(pieces): # Check if the puzzle is solved
            print("Congratulations! You've solved the puzzle!")
            break
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")
        
