from random import *

myMinTime = 5
myMaxTime = 15
count = 0

for people in range(50):
    distanceTime = random.randint(5,50)
    if distanceTime > myMinTime and distanceTime < myMaxTime:
        print(f"[0] {people}번쨰 손님 (소요시간 : {distanceTime})")
        count += 1
    else:
        print(f"[ ] {people}번쨰 손님 (소요시간 : {distanceTime})")

print(f"총 탑승 승객 : {count}분")
