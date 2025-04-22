my_set = {1,2,3,3,3}
asd = {1,1,1,2,3}
print(my_set)
print(asd)

# 교집합
java = {"장세현","김철수","야도란"}
C = set(["장세현","김철수"])
print(java & C)
print(java.intersection(C))

#합집합
print(java | C)
print(java.union(C))

#차집합
print(java - C)
print(java.difference(C))

# 더하기
C.add("야도란")
print(C)

C.remove("장세현")
print(C)



