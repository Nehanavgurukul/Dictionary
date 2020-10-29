# dic={}
# str="MISSISSIPPI"
# l=[]

# for x in str:
#     count=0
#     if(x not in l):
#         l.append(x)
#         for y in str:
#             if x==y:
#                 count=count+1
#     else:
#         for y in str:
#             if x==y:
#               count=count+1
#     dic[x]=count
# print(dic)

dic={}
str="MISSISSIPPI"
for x in str:
    count=0
    for y in str:
        if x==y:
            count=count+1
    dic[x]=count
print(dic)

            

