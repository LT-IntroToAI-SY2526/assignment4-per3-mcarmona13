# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe? The hardest part was implementing the has_won method to check all 8 winning combinations(3 rows, 3 columns, 2 diagonals). I stored there combinations in a list to keep code clean.
2. Explain how you would add a computer player to the game.
 - Modify the game loop to detect if it's the computer's turn
 - Create a get_computer_move() method that returns a valid position
 - Start with random moves using random.choice()
3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

Creating a strategy:
1. Win if possible(checks all moves for immediate wins)
2. block opponent's winning move
3. Take center(pos. 4)
4. take a corner(0,2,6, or 8)
5. take an edge(1,3,5, or 7)



   
