#name = "유닛1"
#hp = 40
#damage = 5
#
#print(f"{name} 이(가) 생성되었습니다.")
#print(f"체력 {hp} 공격력{damage}\n")
#
#name2 = "유닛2"
#hp2 = 120
#damage2 = 40
#
#
#print(f"{name2} 이(가) 생성되었습니다.")
#print(f"체력 {hp2} 공격력{damage2}\n")
#
#def attack(name, location,damage):
#    print(f"{name} 이(가) {location} 바향으로 공격합니다. [공격력 : {damage}]")
#
#attack(name,"1시",damage)
#attack(name2,"12시",damage2)
#
#
#name3 = "유닛3"
#hp3 = 150
#damage2 = 60

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 이(가) 생성되었습니다.")
        print(f"체력 {hp} 공격력{damage}\n")


marine1 = Unit("마린",40,5)
tank1 = Unit("탱크",120,20)
tank2 = Unit("탱크",150,30)