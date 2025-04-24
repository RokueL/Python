chicken = 10
orderNum = 1

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg


while True:
    try:
        print(f"남은 치킨 : {chicken}")
        order = int(input("몇 마리 주문하실?"))
        if(order > chicken):
            print("수량이 부족합니다")
        elif order <= 0:
            raise ValueError
        else:
            if chicken > 0:
                chicken -= order
                print(f"조리중....")
                print(f"조리 완료 되었습니다. 주문번호 : {orderNum}")
                orderNum += 1
                print(f"현재 남은 치킨 : {chicken}\n")
                if chicken == 0:
                    print("재고 소진으로 판매를 종료합니다")
                    break
            else:
                print("현재 남은 치킨이 없습니다.")
                raise SoldOutError("다음에 이용 부탁드립니다.")

    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
    except SoldOutError as err:
        print(err)
        break

