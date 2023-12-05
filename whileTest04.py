# 1~10 사이의 숫자 중 홀수만 출력하는 프로그램을 작성하시오.
i = 0

while i < 10:
    i = i + 1
    if i % 2 == 0: # 짝수 찾기 조건
        continue    # continue 문이 실행되면 continue 문 다음에 나오는 문장들은 실행x
                    # 그리고 다시 while문의 조건문이 실행됨
    print(i)

i = 0

while i < 10:
    i = i + 1
    if i % 2 != 0: # 홀수 찾기 조건, i % 2 == 1
        print(i)

