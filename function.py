import random as r

def roll():
  return r.randint(1,6)
# Select a random number between 1 and 6 (rolling a d6)

def getStat():
  list = (roll(), roll(), roll(), roll())
  return sum(list) - min(list)
# See above comment, do that 4 times and make a stat with it

def getStatBlock():
  return (getStat(), getStat(), getStat(), getStat(), getStat(), getStat())
# See above comment, now do that 6 times

def ValueErrorCheck(var):
  try:
    var = int(input(f"{var}: "))
  except ValueError:
    print(f"Set to 3")
    var = 3
  return var
# Input checker that sets the value to three if something goes bad, allows you to skip inputs
