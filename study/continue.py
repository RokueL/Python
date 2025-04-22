absent = [2,5]
gang = [19]
for student in range(1,21):
    if student in absent:
        print("{0} 결석임".format(student))
        continue
    elif student in gang:
        print("개기네 {0}는 교무실로 따라와".format(student))
        break
    else:
        print("{0} 책 읽으렴".format(student))