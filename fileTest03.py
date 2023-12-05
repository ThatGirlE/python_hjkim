# f = open("연습.txt","r", encoding="utf-8")

with open("연습.txt","r", encoding="utf-8") as f:
    result = f.read() #불러온 파일의 내용을 모두 읽어오기
    # with 블럭을 벗어나면 자동으로 f.close() 실행됨

print(result)


