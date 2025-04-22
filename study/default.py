#def profile(name,age,main_lang):
#    print("이름 : {0}\t 나이 : {1}\t 사용 언어 : {2}"\
#          .format(name,age,main_lang))
#
#profile("김종국",53,"Java")
#profile("유상무",49,"C#")

def profile(name,age = 17,main_lang ="Java"):
    print("이름 : {0}\t 나이 : {1}\t 사용 언어 : {2}"\
          .format(name,age,main_lang))

profile("김태우")
