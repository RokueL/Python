gun = 10

def chekcpoint(soliders):
    global gun
    gun -= soliders
    print(f"현재 총의 수량은 {soliders}정입니다.")

#print(f"현재 총 : {gun}정")
#chekcpoint(3)
#print(f"현재 총 : {gun}정")

def chekcpoint_return(gun, soliders):
    gun -= soliders
    print(f"현재 총의 수량은 {gun}정입니다.")
    return gun

print(f"현재 총 : {gun}정")
gun = chekcpoint_return(gun, 4)
print(f"현재 총 : {gun}정")
