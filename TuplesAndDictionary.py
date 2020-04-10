#Tuple
val = (1, 2, 3, 4)
print(val)

#Dictionary
dic = {"a": 2, 4: "god", "c": "hello world"}
print(dic[4])
print(dic["c"])
emptyDict = {}

emptyDict[0]= "mayuri"
emptyDict["hi"] = "prashanth"
print(emptyDict)
print("******************FOR LOOP*****************")
for i in range(10, 1, -1):
    print(i)

print("*****************WHILE LOOP*************")
i = 1
while(i<10):
    if(i==5):
        i=i+1
        continue
    if(i==9):
        break
    print(i)
    i=i+1



