# 리스트 컴프리헨션

a = [1,2,3,4]

result = []

for i in a:
    result.append(i*3)
print(result)

result = [i*3 for i in a] #list comprehension

print(result)
result2 = [i*3 for i in a if i%2 == 0]

print(result2)



