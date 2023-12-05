# import operator
#
# import random
#
# print(random.random()) #0.0~1.0 사이의 수중 난수
# print(random.randient(1,45)) # 1~45사이의 임의의 정수가 반환
list1=[1,2,3,4,5,6,7,8,9,10]
random.choice(list1) # List 원소중에서 랜덤으로 1개반환
random.sample(list1, 6)
print(sorted(list1))
print(sorted(list1, key=operator.itemgetter(1)))
# 리스트 원소내의 인덱스가 1인 원소의 오름차순으로 정렬

dic1=[{"이름":"홍길동","나이":12, "학년":3},{"이름":"김유신","나이":23, "학년":2},{"이름":"성춘향","나이":17, "학년":1}]
print(sorted(dic1, key=operator.itemgetter("나이")))