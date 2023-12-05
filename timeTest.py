import time

print(time.time()) # 현재시간 초로 표시

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(time.ctime()) #항상 현재 시간 반환

time.sleep(10) # 10초 일시정지

while(True):
    print("안녕하세요!!!")
    time.sleep(1)














