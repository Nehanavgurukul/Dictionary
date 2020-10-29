# list=[
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ]
# list1=[]
# for items in list:
#     for x in items.values():
#         if items[x] not in list1:
#             list1.append(x)
# print(list1)

list=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
list1=[]
for items in list:
    for x in items.values():
        if x not in list1:
            list1.append(x)
print(list1)


