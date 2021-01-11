with open('curency.txt') as f:
    lines = f.readlines()

curencyDict = {}
for line in lines:
    parsed = line.split("\t")
    curencyDict[parsed[0]] = parsed[1]

print(curencyDict)
amount = int(input("Enter Amount:\n"))
print("enter the name of curency which you want to convert")
[print(item) for item in curencyDict.keys()]
curency = input("please enter one the value: \n")
print(f"{amount} INR is equal to {amount *float(curencyDict[curency])} {curency}")