key = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]
dic={}
i=0
while(i<len(key)):
    j=0
    while(j<=i):
        dic[key[i]]=value[j]
        value.remove(value[j])
        j=j+3
    i=i+1
print(dic)