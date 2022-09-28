# AI-Rush-Hour
Utilized the A* Search Algorithm to guarantee the most optimal path

2 heuristic choices when running the program: blocking heuristic and a heuristic that I created 

Prints the moves needed to solve the puzzle in the least amount of steps
The calling rushhour function takes two parameters: The first parameter takes an integer: 0 or 1. 0 is to activate the blocking heuristic. 1 is to activate the heuristic that I have developed to be at least effective as the blocking heuristic. The second parameter takes the initial state of the board as an array of 6 strings. Empty spaces are represented with "-" and cars/trucks are represented by capital letters. Vehicles are represented by their own unique letters. So if a car is represented by "AA" , the letter A cannot be used to represent any other vehicles.

The puzzle called "Rush Hour" begins with a six-by-six grid of squares. Little plastic cars and trucks are distributed across the grid in such a way as to prevent one special car from moving off the grid, thereby escaping the traffic jam. The initial configuration of cars and trucks is preordained by a set of cards, each containing a different starting pattern.

Cars occupy two contiguous squares, while trucks occupy three contiguous squares. All vehicles are oriented horizontally or vertically, never on the diagonal. Vehicles that are oriented horizontally may only move horizontally; vehicles that are oriented vertically may only move vertically. Vehicles may not be lifted from the grid, and there is never any diagonal movement. Vehicles may not be partially on the grid and partially off the grid.

The special car is called the X car. We'll represent it on the grid as two contiguous squares with the letter X in them. (We'll represent all other cars and trucks with different letters of the alphabet, but the special car will always be labeled with the letter X.) The X car is always oriented horizontally on the third row from the top; otherwise, the X car could never escape.

The goal state is any configuration of cars and trucks that can be obtained through correct application of the operators, such that the X car covers the rightmost two squares of the third row from the top.

You can assume that there will never be a horizontal car blocking the X car in the third row.
