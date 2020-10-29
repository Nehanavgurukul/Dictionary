my_dict = {
    'a':50, 
    'b':58, 
    'c':78,
    'd':40, 
    'e':100, 
    'f':20,
    'g':94
    }
i=0
highest=[]
while(i<3):
    max=0
    for x in my_dict.values():
        if x>max:
            max=x
    highest.append(max)
    for x,y in my_dict.items():
        if y == max:
            my_dict.pop(x)
            break
    i=i+1
print(highest)


