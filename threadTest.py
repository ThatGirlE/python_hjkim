import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1) #1초 딜레이
        print(f"working:{i}")

print("----------Start--------------")

threads=[]
for i in range(5):
    #long_task()
    t=threading.Thread(target=long_task) #스레드 생성
    threads.append(t)
    # threads.append()

for t in threads:
    t.start()   # 스레드를 실행

for t in threads:
    t.join() # 스레드가 종료될때까지 대기

print("-------------End-------------")




