student1={
    "name":"neha",
    "age":21,
    "collage":"vijyaraje"
}
print(student1)
print(student1["name"])
student1["age"]=25
print(student1)
del student1["collage"]
print(student1)
print(student1.keys())
print(student1.values())
student2={
    "collage":"hindu collage",
    "email":"webssss.com"
}
student1.update(student2)
print(student1)
student1.clear()
print(student1)
del student1
# yaha error throgh hoga because yaha student1 name ki koi dictionary nhi hai 
print(student1)