class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 이(가) 생성되었습니다.")
        print(f"체력 {hp} 공격력{damage}\n")

wraith1 = Unit("레이스",70,5)
print(f"유닛 이름 : {wraith1.name}\t공격력 : {wraith1.damage}")

wraith2 = Unit("레이스",70,5)
wraith2.clocking = True



if wraith2.clocking == True:
    print(f"{wraith2.name} 는 현재 클로킹 상태입니다")