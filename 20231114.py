# 1. 3개의 정수값을 입력 받아 짝수인지 홀수인지 판별하여 출력하는 함수를 작성하시오.
# 함수의 이름은 evenOrOdd로 작성
#
# 예) evenOrOdd(3, 10, 50)
#
# 3은 홀수입니다
# 10은 짝수입니다
# 50은 짝수입니다.

# def evenOrOdd(a,b,c):
#     if a % 2 == 0:
#         print(f"{a}짝수입니다.")
#
#     else:
#         print(f"{a}홀수입니다.")
#     if b % 2 == 0:
#         print(f"{b}짝수입니다.")
#
#     else:
#         print(f"{b}홀수입니다.")
#
#     if c % 2 == 0:
#         print(f"{c}짝수입니다.")
#
#     else:
#         print(f"{c}홀수입니다.")


# def evenOrOdd2(a,b,c):
#     ilist=list([a,b,c])  # [3,10,50]
#     for i in ilist:
#         if i % 2 == 0:
#             print(f"{i}짝수입니다.")
#         else:
#             print(f"{i}는 홀수입니다.")
#
# evenOrOdd2(3,10,50)

# 2. 아래 리스트를 입력받아 짝수만 포함하는 리스트를 반환하는 함수를 작성하시오.
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# 함수 이름은 evenList
# 예) list2 = evenList(list1)
# 출력>
# [2, 4, 6, 8]

# def evenList(sampleList):
#     resultList = []
#     for i in sampleList:
#         if i % 2 == 0:
#             resultList.append(i)
#     return resultList
# list1 = [1,2,3,4,5,6,7,8]
# print(evenList(list1))
# list2 = [1,5,8,9,12,15,42,65,70]
# print(evenList(list2))
#


# 3. 입력된 문자열을 역순으로 출력하는 함수를 작성하시오.
# 함수이름은 reversePrint
# 예) reversePrint("hello")
# 출력> olleh

# str="hello"

# def reversePrint1(str):
#     resultStr = ""
#     for i in str:
#         resultStr = i + resultStr
#
#     return resultStr
#
# print(reversePrint1("hello"))

# def reversePrint1(str):
#     resultStr = ""
#     for i in str:
#         resultStr = i + resultStr
#
#     return resultStr
#
# print(reversePrint1("hello"))


# def reversePrint2(str):
#     for i in range(0,5,2):
#         print(str[i])
#
# reversePrint2("hello")



# def reversePrint3(str):
#     for i in range(4,-1,-1):
#         print(str[i])
#
# reversePrint3("hello")
#
#
# def reversePrint4(str):
#     for i in range(len(str)-1,-1,-1):
#         print(str[i], end="")
#
# reversePrint4("helloworld")



