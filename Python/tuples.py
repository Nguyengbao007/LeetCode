# tuple = collection which is ordered and unchangeable use to group together related data
student = ("Bao",21,"male")
print(student.count("Bao"))
print(student.index("male"))
for x in student:
    print(x)
if "Bao" in student:
    print("Hello Bao")