# Rock-Paper-Scissors-Game

This is a Rock, Paper, Scissors game played as a best-of-5 match (first to 3 wins). Here's how it works:

**Setup**
Two score counters (pp for player, cp for computer) start at 0.
The valid choices are stored in a list, and the rules are printed for the player.

**Game Loop**
The while loop keeps running as long as both scores are 2 or below — meaning neither player has reached 3 wins yet. Each round:

The computer randomly picks from the choices list.
The player types their choice (converted to lowercase).
Both choices are printed.
The result is determined by checking all possible win/loss/tie combinations:

If the computer's choice beats the player's → cp += 1, computer wins the round.
If the player's choice beats the computer's → pp += 1, player wins the round.
If both chose the same → it's a tie, no points awarded.
Anything else (e.g. a typo) triggers the error message.



End of Game
After the loop exits, the final scores are checked: whoever reached 3 wins is declared the overall winner.


End of Game
After the loop exits, the final scores are checked: whoever reached 3 wins is declared the overall winner.
