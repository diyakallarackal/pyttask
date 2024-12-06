def play_stick_game():
    sticks=16
    current_players=1
    while sticks>0:
        print(f"Current no of sticks:{sticks}")
        move=int(input(f"Player {current_players}, has many sticks do you want to remove? (choose 3,2,1):"))
        if move not in[1,2,3]:
            print("Invalid move")
            continue
        if move>sticks:
            print(f"Not enough sticks. you can only remove up to {sticks} ")
            continue
        sticks-=move
        if sticks==0:
            print(f"\nPlayer {current_players} removed the last stick")
            print(f"Player {current_players} loses")
        current_players=3-current_players


play_stick_game()
