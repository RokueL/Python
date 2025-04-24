from random import randint


class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} : 유닛이 생성되었습니다.")

    def move(self, location):
        print("[지상 이동 유닛]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} 이(가) {damage} 의 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} 의 현재 체력은 {self.hp} 이(가) 남았습니다.")
        if self.hp <= 0:
            print(f"{self.name} 이(가) 파괴되었습니다.")

class AttackUnit(Unit):
    def __init__(self,name,hp,damage,speed):
        Unit.__init__(self,name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} 유닛이 {location} 방향으로 공격합니다. 공격력 : {self.damage}")

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,location):
        print(f"{self.name} : {location} 방향으로 날아갑니다. 속도 : {self.flying_speed}")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self,name,hp,damage, flying_speed):
        AttackUnit.__init__(self,name,hp,damage,0)
        Flyable.__init__(self,flying_speed)


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,5,2)

    def steampack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"체력이 부족하여 사용할 수 없습니다.")

class Tank(AttackUnit):
    seize_develope = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크",120,20,1)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_develope == False:
            return

        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다")
            self.damage = 40
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드를 해제합니다")
            self.damage = 20
            self.seize_mode = False

class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,10,2)
        self.clocked = False

    def clocking(self):
        if self.clocked == False:
            print(f"{self.name} : 클로킹 모드로 전환합니다.")
            self.clocked = True
        else :
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.clocked = False

def GameStart():
    print("[알림 : 게임을 시작합니다]")
def GameOver():
    print("[알림 : 게임을 종료합니다.]")

GameStart()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_develope = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.steampack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))

GameOver()
