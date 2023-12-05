from faker import Faker

f1 = Faker("ko-KR")

print(f1.name())
print(f1.address())

fakerList = []

for i in range(1,10):
    fakerList.append(f1.name())

print(fakerList)

