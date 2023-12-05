score = 0

while True:
    score = score + 1
    print(score)
    if score == 100:
        break

a = 0
list1 = []
while a < 10:
    a = a + 1
    if a % 2 == 0: # 짝수를 판별하는 조건
        continue # 재실행되므로 짝수가 출력되지 않음
    list1.append(a) # 홀수 출력됨

print(list1)

score = 0
while True:
    score = score + 1
    print(score)
    if score == 100:
        break

