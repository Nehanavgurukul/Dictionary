dic={
    "ball":"grean",
    "bat":4,
    "bat":3,
    "wickets":8,
    "ball":"red",
    }
dict={}
for x,y in dic.items():
    if( x,y) not in dict:
        dict[x]=y
print(dict)
