# Day 1 For Advent of Code - calmelb

#Variable Definitions
previousNo = 0
larger = 0
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
            263]
#TODO: Import text file

# Logic Analysis
for i in tempdata:
    if previousNo != 0:
        if previousNo < i:
            # print("Larger: "+ str(i))
            # print("Smaller: "+ str(previousNo))
            # print("_______________")
            larger = larger + 1
    previousNo = i

print(larger)
