# range 함수

print(range(0, 10)) # 0,1,2,3,4,5,6,7,8,9
for i in range(10, 50):
    print(i)

# 1~100까지의 모든 숫자의 합을 더한 값을 출력하시오 : 5050
sum = 0
for i in range(1,101): # 1터 100까지 인덱스 숫자의 갯수는 101개....
    sum = sum + i #누적식
print(sum)




