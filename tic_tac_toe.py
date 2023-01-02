board = [["-" for i in range(3)] for i in range(3)]

def draw_board(board):
  for row in board:
    print(" ".join(row))

def get_move(player):
  print(f"{player}, it's your turn.")
  while True:
    try:
      col = int(input("Enter column number (0, 1, 2): "))
      row = int(input("Enter row number (0, 1, 2): "))
      if board[row][col] == "-":
        board[row][col] = player
        break
      else:
        print("That spot is already taken. Try again.")
    except ValueError:
      print("Invalid input. Try again.")
    except IndexError:
      print("Invalid position. Try again.")

def has_won(player):
  # check rows
  for row in board:
    if row == [player, player, player]:
      return True
  # check columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def main():
  draw_board(board)
  while True:
    get_move("X")
    draw_board(board)
    if has_won("X"):
      print("X has won!")
      break
    get_move("O")
    draw_board(board)
    if has_won("O"):
      print("O has won!")
      break

main()
