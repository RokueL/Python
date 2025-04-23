class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name, hp)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} 유닛이 {location} 방향으로 공격합니다. 공격력 : {self.damage}")

    def damaged(self, damage):
        print(f"{self.name} 이(가) {damage} 의 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} 의 현재 체력은 {self.hp} 이(가) 남았습니다.")
        if self.hp <= 0:
            print(f"{self.name} 이(가) 파괴되었습니다.")

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,location):
        print(f"{self.name} : {location} 방향으로 날아갑니다. 속도 : {self.flying_speed}")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self,name,hp,damage, flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)

valkyrie = FlyableAttackUnit("valkyrie",70,5, 5)
valkyrie.fly("3시")

