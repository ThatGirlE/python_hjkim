def two(x):
    return x*2

print(list(map(two,[1,2,3,4,5,6])))

print(list(map(lambda x:x*2,[1,2,3,4,5,6])))

result=[]
for i in [1,2,3,4,5,6]:
    result.append(two(i))
print(result)

print(round(4.167,2))





