list1=["f1","f2","f3","f4","f5"]
list2=["rinki", "pooja", "radha" ,"pary","priya"]
dict={}

i=0
while(i<len(list1)):
    j=i
    while(j<len(list2)):
        dict[list1[i]]=list2[j]
        break
    i=i+1
print(dict)