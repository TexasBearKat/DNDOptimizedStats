import function as f
import random as r

print("For info: read the README.md")
target = f.ValueErrorCheck("Target")
count = f.ValueErrorCheck("Count")
least = f.ValueErrorCheck("Least")

optimal = False
itercount = 0

while not optimal:
    itercount += 1

    if itercount % 10000 == 0:
        print(f"Working: Iteration {itercount}")

    counter = 0
    good_enuf = True
    
    statblock = f.getStatBlock()

    for item in statblock:
        if item >= target:
            counter += 1
        if item < least:
            good_enuf = False
    
    if counter >= count and good_enuf:
        optimal = True

print(f"Found {statblock} at {itercount} iterations")

