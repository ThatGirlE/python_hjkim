import datetime

dayTest="2023-11-28"
day1=datetime.date(2023,11,28)
day2=datetime.date(2024,2,23)

print(day1)

print(type(day1))

diff=day2-day1
print(diff.days)
print(day2.weekday()) #요일을 숫자로 반환 ->0월요일 1화요일.... 6일요일

print(datetime.datetime.now()) # 현재시간 불러오기
print(datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S"))





