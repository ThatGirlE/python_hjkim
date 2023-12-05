score1 = 90
score2 = 80
score3 = 70

score_list = [90,80,70]  ## 리스트 자료형
list1 = ["Kor","Jap","USA"]
list2 = [90,"kor",10.5]

print(score_list)
print(score_list[2])
print(score_list[0] + score_list[2])

list3 = [10,20,30, [1,2,3]]

print(list3[2])
print(list3[3])
print(list3[3][1])

list4 = [1,2,3,4,5,6,7]
print(list4[2:5])

list5 = [1,2,3]
list6 = [9,8,0]

print(list5 + list6)  # 리스트끼리 + 연산을 행하면 두 리스트가 병합
print(list5*3)

list5 = [1,2,3,4,5,6,7]

list5[2] = 30  ## 특정 리스트 값 수정하기
print(list5)

del list5[5]  #원소 '6'이 삭제
print(list5)

del list5[1:3] #원소 '2', '30'이 삭제
print(list5)







