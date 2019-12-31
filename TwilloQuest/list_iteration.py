import sys

things = sys.argv
n = 1
for thing in things[1:]:
    print(f"{n}. {thing}\n")
    n = n + 1
