#score_file = open("score.txt","w", encoding="utf-8") # w = write 덮어쓰기
#print("수학 : 0",file=score_file)
#print("영어 : 30",file=score_file)
#print("코딩 : 90",file=score_file)
#score_file.close()

#score_file = open("score.txt","a", encoding="utf-8") # a = append 이어쓰기
#score_file.write("과학 : 40")
#score_file.write("\n사회 : 80")
#score_file.close()

#score_file = open("score.txt","r", encoding="utf-8") # r = read 불러오기
#print(score_file.read())
#score_file.close()

#score_file = open("score.txt","r", encoding="utf-8")
#print(score_file.readline(),end="") # 줄별로 읽기 한 줄 읽고 커서는 다음 줄
#print(score_file.readline(),end="") # 줄별로 읽기 한 줄 읽고 커서는 다음 줄
#print(score_file.readline(),end="") # 줄별로 읽기 한 줄 읽고 커서는 다음 줄
#print(score_file.readline(),end="") # 줄별로 읽기 한 줄 읽고 커서는 다음 줄
#print(score_file.readline(),end="") # 줄별로 읽기 한 줄 읽고 커서는 다음 줄
#score_file.close()

#score_file = open("score.txt","r", encoding="utf-8")
#while True:
#    line = score_file.readline()
#    if not line:
#        break
#    else:
#        print(line,end="")

#for line in score_file:
#    print(line,end="")
#score_file.close()

score_file = open("score.txt","r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
