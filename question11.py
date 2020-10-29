my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
highest=[]
for x in my_dict.values():
    for y in my_dict.values():
        if x<y:
            highest.append(y)
    break
print(highest)
    