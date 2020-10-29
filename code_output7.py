# id2 = id(rec)
# print(id1 == id2)
rec = {
"Name" : "Python", 
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}

id1 = id(rec)
print(id1)
del rec
rec = {
"Name" : "Python", 
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}
id2 = id(rec)
print(id2)
print(id1 == id2)

