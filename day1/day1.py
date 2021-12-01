# Day 1 For Advent of Code - calmelb

#Variable Definitions
previousNo = 0
previousNoback = 0
larger = 0
datalist = []
# Text File processing
tempdata = [199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
            1,
            5555,
            23,
            24,
            -5,
            10]


inputfile = open("input.txt", "r")
filecontent = inputfile.readlines()

for element in filecontent:
    datalist.append(element.strip())

# Logic Analysis
for i in datalist:
    if previousNo != 0:
        if previousNo < i:
                # print("Larger: "+ str(i))
                # print("Smaller: "+ str(previousNo))
                # print("_______________")
            larger = larger + 1
        # else:
        #     print("Previous Comp: "+ str(previousNoback))
        #     print("Current No.: "+ str(i))
        #     print("Previous No.: "+ str(previousNo))
        #     print("_______________")
    previousNoback = previousNo
    previousNo = i

print(larger)
