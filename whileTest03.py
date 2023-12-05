
print("제가 생각한 숫자를 맞춰 보세요")

MyNum = 7

while True:
    num = input("1~10 사이의 숫자를 입력하세요:")
    num = int(num) # 문자를 정수로 변환
    if MyNum == num:
        print("축하합니다. 정답입니다.!")
        break  # While문 종료 !






