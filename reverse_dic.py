sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000
}
list=[]
for x in sampleDict:
    list.append(x)
dic={}
length=len(list)-1
while(0<=length):
    dic[list[length]]=sampleDict[list[length]]
    length=length-1
print(dic)
