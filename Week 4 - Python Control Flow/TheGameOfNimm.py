"""
File: nimm.py
--------------------
This program plays the ancient game of Nimm. 
Two players take turns removing 1 or 2 stones from a pile of 20.
The player who takes the last stone loses.
"""

def main():
    # Milestone 1: Start with 20 stones
    stones_left = 20
    
    # Milestone 2: Track whose turn it is
    # We will use 1 for Player 1 and 2 for Player 2
    player_turn = 1
    
    while stones_left > 0:
        # Display current status
        print("There are " + str(stones_left) + " stones left.")
        
        # Milestone 2: Prompt specific player
        # Note the use of straight quotes '' here
        prompt = "Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "
        remove = int(input(prompt))
        
        # Milestone 3: Validate input (must be 1 or 2)
        while remove != 1 and remove != 2:
            remove = int(input("Please enter 1 or 2: "))
            
        # Update the pile
        stones_left -= remove
        print("") # Empty print for readability between turns
        
        # Milestone 2: Switch players if the game is still going
        if stones_left > 0:
            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1
                
    # Milestone 4: Announce the winner
    # Since the last player to take a stone loses, 
    # the player whose turn it WAS is the loser.
    if player_turn == 1:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

if __name__ == '__main__':
    main()