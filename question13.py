# from heapq import nlargest
# # my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }

# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest) 

my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
i=0
highest=[]
while(i<3):
    max=0
    for x,y in my_dict.items():
        if y>max:
            max=y
    for x,y in my_dict.items():
        if y == max:
            highest.append(x)
            my_dict.pop(x)
            break
    i=i+1
print(highest)
    
    