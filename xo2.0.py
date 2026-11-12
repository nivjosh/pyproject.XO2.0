board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_move(board, player):
  while True:
      choice = input("(Enter your choice: (between 1 and 9): )")
      if not choice.isdigit():
          print("Invalid choice please enter a number only")
          continue
      choice = int(choice)
      if choice < 1 or choice > 9:
          print("Invalid choice please enter a number between 1-9 only")
          continue
      row = (choice - 1) // 3
      col = (choice - 1) % 3
      if board[row][col] != " ":
          print("this spot is already taken , please choose another spot ")
          continue
      return row, col
def win_check(board, player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True
while True:
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    current_player = "X"
    while True:
      print_board(board)
      row, col = player_move(board, current_player)
      board[row][col] = current_player
      if win_check(board, current_player):
          print(current_player ,"You won!")
          break
      if is_draw(board):
          print_board(board)
          print("Draw")
          break
      if current_player == "X":
          current_player = "O"
      else:
          current_player = "X"
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print('game over')
        break
