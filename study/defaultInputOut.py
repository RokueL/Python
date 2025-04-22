#import sys
#print("파이선","자바", file=sys.stdout)  # 표준 처리 Debug.Log
#print("파이선","자바", file=sys.stderr)  # 에러 처리 Debug.LogError

#print("파이선","자바",sep=' , ', end='?') # sep = 사이에 분리 넣어주기 end = 다음 줄 뭐해줄지
#print("\n뭐가 더 잼슴?")

#scores = {"수학":0, "영어":20, "코딩":90}
#for subject, score in scores.items():
#    #print(f"{subject} : {score}")
#    print(f"{subject.ljust(8)} : {str(score).rjust(4)}",)  # str에서만 사용되는 거 왼쪽 정렬 오른쪽 정렬

#for number in range(1,21):
#    print(f"대기번호 :{str(number).zfill(3)}")  # 001 002 이렇게 나옴

answer = input("아무 값을 입력하세요 : ") # 저장 시 무조건 str
print(f"입력하신 값은 {answer} 입니다")