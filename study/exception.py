try:
    print("나누기 계산기")
    nums = []
    nums.append(int(input("1st Num")))
    nums.append(int(input("2nd Num")))
    #nums.append(nums[0]/nums[1])

    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("잘못된 값을 입력함")
except ZeroDivisionError as err:
    print(err)
except IndexError as err:
    print(err)
except Exception as err:
    print("알 수 없는 오류 발생")
    print(err)