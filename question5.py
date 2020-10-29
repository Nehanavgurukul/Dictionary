# list1=["one","two","three","four","five"]

# list2=[1,2,3,4,5,] 
# dic={}
# # for x,y in (list1):
# #     dic[x]=y
# # print(dic)
# i=0
# while(i<len(list1)):
#     j=i
#     while(j=i):
#         dic[list1[i]]=list2[j]
#         j=j+1
#     i=i+1

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
dic={}
for key in list1:
    for value in list2:
        dic[key]=value
        list2.remove(value)
        break
print(dic)