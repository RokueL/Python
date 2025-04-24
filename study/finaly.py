class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 나누기 계산기")
    num1 = int(input("1st Num"))
    num2 = int(input("1st Num"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값 : {num1,num2}")
    print(f"{num1} / {num2} = {num1/num2}")


except ValueError:
    print("잘못된 값 입력 한자리 수만 입력하시오")
except BigNumberError as err:
    print("에러임 하나만 입력하셈")
    print(err)
except Exception as err:
    print(err)
finally:
    print("이용해주셔서 감사")