User = {"장세현":"JSH", "김수환":"KSH"}
fruit = "사과"

if("장세현" in User):
    print("장세현 있음")
else:
    print("없어")

if fruit == "사과":
    print("사과")
else:
    print("아님")

temp = int(input("수를 입력하시오"))
if temp > 0:
    print("0 초과")
else:
    print("0 이하")