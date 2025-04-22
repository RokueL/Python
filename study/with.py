import pickle

#with open("profile.pickle","rb") as profile_file: # 따로 닫아줄 필요가 없다
#    profile = pickle.load(profile_file)
#    print(profile)

#with open("study.txt","w",encoding="utf8") as study_file:
#    study_file.write("파이썬 공부중")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())