import random as r

def roll():
  return r.randint(1,6)


def getStat():
  list = (roll(), roll(), roll(), roll())
  return sum(list) - min(list)


def getStatBlock():
  return (getStat(), getStat(), getStat(), getStat(), getStat(), getStat())


def ValueErrorCheck(var):
  try:
    var = int(input(f"{var}: "))
  except ValueError:
    print(f"Set to 3")
    var = 3
  return var

  