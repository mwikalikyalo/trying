print("Tic tac toe game. The only valid inputs for this game is either x or o. Input to start playing")
def tic_tac():
  add=input()
  for x in add:
    if add=="x":
      print("o")
    elif add=="o":
      print("x")
    elif add != "x" or add!="o":
      print("Please use either x or o")
    else:
      print("This is invalid")

tic_tac()