class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 이(가) 생성되었습니다.")
        print(f"체력 {hp} 공격력{damage}\n")

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 이(가) 생성되었습니다.")
        print(f"체력 {hp} 공격력{damage}\n")

    def attack(self, location):
        print(f"{self.name} 유닛이 {location} 방향으로 공격합니다. 공격력 : {self.damage}")

    def damaged(self, damage):
        print(f"{self.name} 이(가) {damage} 의 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} 의 현재 체력은 {self.hp} 이(가) 남았습니다.")
        if self.hp <= 0:
            print(f"{self.name} 이(가) 파괴되었습니다.")

tank = AttackUnit("탱크",70,5)
tank.attack("11시")
tank.damaged(20)
tank.damaged(40)
tank.damaged(30)
