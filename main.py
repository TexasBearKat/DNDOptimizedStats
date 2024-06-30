import function as f
import random as r
# Above: import packages  Below: variable init
print("For info: read the README.md")
target = f.ValueErrorCheck("Target")
count = f.ValueErrorCheck("Count")
least = f.ValueErrorCheck("Least")

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
    statblock = f.getStatBlock()
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

