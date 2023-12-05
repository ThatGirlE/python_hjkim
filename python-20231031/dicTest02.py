dic1 = {"이름":"홍길동", "점수":[90,80,60]}

dic1["나이"] = 30  # dic1의 원소 추가 "나이": 30
print(dic1)

del dic1["이름"]
print(dic1)

dic2 = {"이름":"홍길동", "나이":27, "나이":30}
print(dic2)
print(dic2["나이"])

#dic3 = {["나이", "이름"]:"홍길동"}  # key 값은 리스트처럼 여러개의 값으로 설정 안됨
dic4 = {"이름":"홍길동","나이":27, "직업":"회사원"}
print(dic4.keys())
print(dic4.values())

keyList=list(dic4.keys())  #딕셔너리에서 key만 추출하여 리스트로 변경
valueList=list(dic4.values())  #딕셔너리에서 value만 추출하여 리스트로 변경

print(keyList)

print(dic4.items())
kvList=list(dic4.items())   #[('이름', '홍길동'), ('나이', 27), ('직업','회사원')
dic4.clear()
print(dic4)  ## 모든 딕셔너리 원소 삭제

list2 = []

dic5={"이름":"홍길동", "나이":27, "직업":"회사원"}
print("나이" in dic5)  #key값이 딕셔너리 내에 존재하면 True 아니면 False가 출력

print(dic5.get("이름"))  #dic5["이름"]
print(dic5.get("이름"))  #해당되는 key값이 존재하지 않으면 None
print(dic5["이름22"]) #해당되는 key값이 존재하지 않으면 Error!







