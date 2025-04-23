
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 이동 유닛]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]")

class AttackUnit(Unit):
    def __init__(self,name,hp,damage, speed):
        Unit.__init__(self,name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} 유닛이 {location} 방향으로 공격합니다. 공격력 : {self.damage}")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 의 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 이(가) 남았습니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,location):
        print(f"{self.name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self,name,hp,damage, flying_speed):
        AttackUnit.__init__(self,name,hp,damage, 0)
        Flyable.__init__(self,flying_speed)

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

def GameStart():
    print("[게임 시작]")

def GameEnd():
    pass

supply_depot = BuildingUnit("SCV",40,"1시")

GameStart()
GameEnd()