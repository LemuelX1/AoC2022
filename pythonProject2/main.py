file1 = open('RPS.txt', 'r')

options = file1.readlines()
# value is the value of each value
value = {
    "Y": [2, "paper"],
    "X": [1, "rock"],
    "Z": [3, "scissors"],
    "A": [1, "rock"],
    "B": [2, "paper"],
    "C": [3, "scissors"]
}
# rpsmath is the array made to make the final math of the rps solutions
rpsmath = []

for x in options:
    x = x.split()
    if x[0] == 'B':
        rpsmath.append(value["B"])


print(rpsmath)