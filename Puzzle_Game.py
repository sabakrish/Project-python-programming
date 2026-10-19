# Puzzle game example: shuffle the numbers 1-9, swap tiles until sorted.
import random

SOLVED = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_puzzle(puzzle):
    """Print the puzzle as a 3x3 grid."""
    for i in range(0, len(puzzle), 3):
        print(' | '.join(puzzle[i:i + 3]))
        print('-' * 9)


def is_solved(puzzle):
    """Return True if the puzzle is back in order."""
    return puzzle == SOLVED


def play():
    pieces = SOLVED.copy()
    random.shuffle(pieces)  # shuffle the pieces to create a random puzzle

    print("Here is your shuffled puzzle:")
    display_puzzle(pieces)

    while True:
        move = input("Enter two positions to swap (1-9) or 'q' to quit: ")
        if move.lower() == 'q':
            print("Thanks for playing!")
            break
        try:
            pos1, pos2 = map(int, move.split())  # positions to swap
            if pos1 < 1 or pos1 > 9 or pos2 < 1 or pos2 > 9:
                print("Invalid positions. Please enter numbers between 1 and 9.")
                continue

            pieces[pos1 - 1], pieces[pos2 - 1] = pieces[pos2 - 1], pieces[pos1 - 1]
            display_puzzle(pieces)

            if is_solved(pieces):
                print("Congratulations! You've solved the puzzle!")
                break
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")


if __name__ == "__main__":
    play()
