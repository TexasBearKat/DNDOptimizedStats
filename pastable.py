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

# Above: function.py   Below: main.py

# Variable Init
print("For info: read the README.md")
target = ValueErrorCheck("Target")
count = ValueErrorCheck("Count")
least = ValueErrorCheck("Least")

optimal = False
itercount = 0
# Main loop
while not optimal:
    itercount += 1
    # Add 1 to the iteration count, and if iteration count is divisible by 10k, print itercount
    if itercount % 10000 == 0:
        print(f"Working: Iteration {itercount}")
    # Variable init again
    counter = 0
    good_enuf = True
    # Make stats
    statblock = getStatBlock()
    # Check stats to see if good enough
    for item in statblock:
        if item >= target:
            counter += 1
        if item < least:
            good_enuf = False
    # If good enough, end loop
    if counter >= count and good_enuf:
        optimal = True
# Print stats and itercount
print(f"Found {statblock} at {itercount} iterations")

