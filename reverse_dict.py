sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000
}
keys=["salary","age","name"]
dic={}
for k in ["salary","age","name"]:
    dic[k]=sampleDict[k]
print(dic)
