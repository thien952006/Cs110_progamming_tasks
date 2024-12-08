# Author   : Xuan Thien Bui
# Email    : xuanthienbui@umass.edu
# Spire ID : 34750117
def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)
def make_empty_board(n):
  lst=[]
  for i in range(n):
    lst1=[]
    for j in range(n):
      lst1.append(' ')
    lst.append(lst1)
  return lst
def get_location(n,m):
  while True:
    r=input(f"Please enter a row index between 0 and {n-1}: ")
    c=input(f"Please enter a column index between 0 and {n-1}: ")
    if(r.isdigit()==False or c.isdigit()==False):
      print(f"({r}, {c}) is not a legal input!")
    elif(int(r)>n-1 or int(c)>n-1):
      print(f"({r}, {c}) is not a legal space!")
    elif(m[int(r)][int(c)]!=' '):
      print(f"({r}, {c}) is not an available space!")
    else:
      return int(r),int(c)
#A function supporting row_win
def check_row(row, target):
  count=0
  if(row[0]==target):
    for x in row:
      if(x== target):
        count+=1
    if(count==len(row)):
      return True
    else:
      return False
  else:
    return False
#
def row_win(n,m,player):
  res=[]
  for i in range(n):
    if(check_row(m[i],player)==True):
      res.append(1)
    else:
      res.append(0)
  if 1 in res:
    return True
  else:
    return False
#A function supporting col_win           
def check_col(board,col_ind,target):
  letter=board[0][col_ind]
  if(letter!=target):
    return False
  for row in board:
    if(row[col_ind]!=letter):
      return False
  return True
#
def col_win(n,m,player):
  res=[]
  for i in range(len(m[0])):
    if(check_col(m,i,player)==True):
      res.append(1)
    else:
      res.append(0)
  if 1 in res:
    return True
  else:
    return False
#A function supporting diag_win
def check_dia(board,target):
  if(board[0][0]!=target):
    return False
  else:
    for i in range(len(board)):
      if(board[i][i]!=board[0][0]):
        return False
    return True
#
def diag_win(n,m,player):
   if(check_dia(m,player)==True):
     return True
   else:
     return False
#A function supporting anti_diag_win
def check_anti_dia(board,target):
  x=len(board)
  if(board[x-1][0]!=target):
    return False
  else:
    for i in range(x):
      if(board[x-1-i][i]!=target):
        return False
    return True
#
def anti_diag_win(n,m,player):
  if(check_anti_dia(m,player)==True):
    return True
  else:
    return False
def has_won(n,board,player):
  if (row_win(n,board,player)==True or col_win(n,board,player)==True or diag_win(n,board,player)==True or anti_diag_win(n,board,player)==True):
    return True
  else:
    return False
def play_game(n):
  board=make_empty_board(n)
  print(f"***Welcome to {n} by {n} Tic-Tac-Toe***")
  print_board(n,board)
  i=0
  while True:
    if(i%2==0):
      player='X'
      print(f"* {player}'s turn *")
      r,c=get_location(n,board)
      board[r][c]=player
      print_board(n,board)
      if(has_won(n,board,player)==True):
        print(f"{player} wins!")
        break
    else:
      player='O'
      print(f"* {player}'s turn *")
      r,c=get_location(n,board)
      board[r][c]=player
      print_board(n,board)
      if(has_won(n,board,player)==True):
        print(f"{player} wins!")
        break
    if(i==n*n-1):
      print("Tie!")
      break
    i+=1



