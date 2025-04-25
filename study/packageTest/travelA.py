class TravelAPackage:
    def detail(self):
        print("[여행 A 패키지] 어느 나라, 단돈 100만원 패키지")

if __name__ == "__main__":
    print("모듈 직접 실행")
    print("모듈 직접 실행 시 실행 됨")
    trip_a = TravelAPackage()
    trip_a.detail()
else:
    print("외부에서 모듈 호출")