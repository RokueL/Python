#def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#    print("이름 : {0} \t 나이 : {1} \t".format(name,age), end=" ")
#    print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*lang):
    print("이름 : {0} \t 나이 : {1} \t".format(name,age), end="\t")
    for language in lang:
        print(language, end=" ")
    print()

profile("김종국",52,"파이썬","C", "자바", "C#")
profile("김지혁",31,"Kotlin","Swift")
