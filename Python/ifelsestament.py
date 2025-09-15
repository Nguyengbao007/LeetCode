age=int((input("How old are you?: ")))
if age > 18:
    print("You are adult !")
elif age == 100:
    print("You are century !")
elif age<0:
    print("You haven't been born yet !")
else:
    print("You are not adult !")