a = 10 # a-> 정수형
print(type(a))

list1 =[10,20,30,40] # 리스트 자료구조
tuple1 = (10,20,30) # 튜플 자료구조 > 수정x, 삭제x, 순서변경x
dic1 = {'이름':'홍길동','나이':27, '직업':'회사원'} #딕셔너리 >인덱스
print(dic1['나이'])

list2 = [{'이름':'홍길동', '나이':27, '직업':'회사원'},{'이름':'홍길동', '나이':27, '직업':'회사원'}]
print(list2[0]['이름'])

set1=set([10,20,20, 30, 30, 30]) # 집합 자료구조-> 중복 허용x
print(set1)

setList=list(set1)
print(setList)




