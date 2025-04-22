import pickle
#profile_file = open("profile.pickle","wb")
#profile = {"이름":"김철수"," 나이":"30","취미":["축구","기타","코딩"]}
#print(profile)
#pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
#profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)

profile_file.close()