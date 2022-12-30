
# file1 is txt reader
file1 = open('Calories.txt', 'r')

# lines is  an array with the lines in the txt
lines = file1.readlines()

# labels is an array to keep track of a group's value
# Blanks are in group 0
labels = []
group = 1
# num is an array of nums
num = []
# x is a string
for x in lines:
    if x == '\n':
        labels.append(0)
        num.append(0)
        group += 1
    else:
        labels.append(group)
        num.append(int(x))
print(num)
print(labels)
# math is an array with the nums
math = []
# sums is an array with the final addition of nums
sums = []
for n, l in zip(num, labels):
    if n != 0:
        math.append(n)
    else:
        sums.append(sum(math))
        math = []
print(sums)
cgn = [-1, -1, -1]
for y in sums:
    if y > min(cgn):
        cgn.remove(min(cgn))
        cgn.append(y)

print(sum(cgn))





