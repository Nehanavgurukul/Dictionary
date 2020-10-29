dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for x in dict.values():
    for y in x:
        count=count+1
print("total values:",count)
