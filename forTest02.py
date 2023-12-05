# 리스트 내의 모든 원소의 합을 출력하는 프로그램을 작성하시오.

list = [10, 23, 5, 6, 11, 21, 99, 22]

sum = 0     #반드시 초기값 설정을 for문 밖에 해줘야 함.

for i in list:
    sum = 0
    sum = sum + i # 누적식

print(sum)

sum = 0     #반드시 초기값 설정을 for문 밖에 해줘야 함.

for i in list:
    sum = sum + i # 누적식
    print(sum)




