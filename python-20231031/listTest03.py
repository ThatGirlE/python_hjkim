list1 = [1,2,3]
list1.append(4)  # 해당 리스트의 마지막 원소로 추가
print(list1)

list2=[]  # 비어있는 리스트

list1.insert(1, 10)
# 해당 인덱스값으로 원하는 값을 insert
print(list1)

list3 = [10,20,30,40,50,30]
# del list3[2]    ## 인덱스항목, 2번인 30값을 삭제

list3.remove(30)  ## 리스트의 원소중 30과 첫번째 일치하는 원소를 삭제(처음 나오는 값만)
print(list3)

list4=[100,200,300,400,500,200]
print(list4.count(200))  ## 리스트 내의 특정값과 일치하는 원소의 갯수를 반환

print(list4.pop()) ## 리스트의 제일 마지막 원소를 반환함과 동시에 그 원소를 삭제
print(list4)

list4.extend([1000,2000])
# list4=[100,200,300,400,500,200] + [1000,2000]
print(list4)

print(list4.index(300)) ## 특정값의 인덱스값

list5 = [10,20,30]
print(list5[5])  # indexError 인덱스 범위를 벗어나..
















