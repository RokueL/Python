#
#stringMessage = """
#반갑습니다,
#예 뭐 그렇게 되었습니다
#"""

#print(stringMessage)
#print('반가워요 %d살입니다'%20)
#print('반가워요 %s살입니다'%"스무")
#print('반가워요 %c살입니다'%"세")
#print('반가워요 {}살입니다'.format(20))
#print('반가워요 {}살입니다. 사실 {}살입니다.'.format(20,67))
#print('반가워요 {0}살입니다. 사실 {1}살입니다.'.format(20,67))
#print('반가워요 {1}살입니다. 사실 {0}살입니다.'.format(20,67))
#print('반가워요 {age}살입니다. 사실 {realAge}살입니다.'.format(age = 20, realAge = 67))
#print('반가워요 {age}살입니다. 사실 {realAge}살입니다.'.format(age = 20, realAge = 67))

#age = 20
#sAge = "스무"
#print(f'반가워요 {age}살입니다. 사실 {sAge}살입니다.')



#print("저는 '돼지'입니다")
#print("저는 \"돼지\"입니다")
#print("C:\\Python313\\python.exe")
#print("Red Apple\rPine")

#print("Red Apple\bPine")
#print("Red Apple\tPine")

url = 'http://naver.com'
my_str = url.replace("http://","") # naver.com
my_str = my_str[:my_str.index(".")]  # naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"


print(password)