User = {"장세현":"JSH", "김수환":"KSH"}

print(User["장세현"])
print(User.get("장세현"))

if("장세현" in User):
    print("장세현 있음")
else:
    print("없어")

print(User.keys())
print(User.values())
print(User.items())

del User["김수환"]
print(User)