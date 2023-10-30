print("input a list of numbers you wish to average, separated by spaces. Make sure these are whole number integers.")
list = input().split()
sum = 0
intlist = [int(item) for item in list]
for thing in intlist:
    sum += thing
avg = sum / len(intlist)
print(f"the average of the numbers provided is {avg}")
