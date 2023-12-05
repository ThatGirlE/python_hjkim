f = open("연습.txt","r", encoding="utf-8")

# result = f.read()  # 불러온 파일의 내용을 모두 읽어오기
#
# print(result)
#
# print(type(result))


for i in f:
    print(i)

f.close()