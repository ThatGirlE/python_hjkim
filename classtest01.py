import self


class Calculator:
    def __init__(self, first, second):  # 생성자 or 초기화자
        self.a=first
        self.b=first

    def add(self):
        result = self.a + self.b
        return result

    def sub(self):
        result = self.a + self.b
        return result

    def mul(self):
        result = self.a * self.b
        return result

    def div(self):
        result = self.a / self.b
        return result

    def square(self): # a의 제곱이 반환되는 메서드
        result = self.a * self.a
        return result


class NewCalculator(Calculator): ## 사칙연산 + 제곱을 출력해주는 연산 추가
    def square(self):  # a의 제곱이 반환되는 메서드
        resultl=self.a*self.a
        return resultl

    def div(self): # 오버라이딩
        result=self.b/self.a
        return result

cal1 = Calculator(10,20)

print(cal1.mul())

new1 = NewCalculator(10, 20)
print(new1.square())
print(new1.div())

print(new1.mul())


#Student 클래스를 만들고 생성자로 나이(age), 학년(grade), 이름(name)을 입력받아 초기화하시오.
#클래스 > 생성자료, 변수자료, 매서드

class Student:
    def __init__(self, age, grade, name):
    self.age = age
    self.grade = grade
    self.name = name

s1= Student(21,3, "홍길동")
print(s1.name)

#아래 코드가 출력결과와 같이 동작하도록 car 클래스를 정의하시오.(생성자 사용)
# car1=Car(4, 1000)
# print(car1.tire)
# print(car1.carPrice)

class Car:
    def __init__(self, tire, carprice):
        self.tire = tire
        self.carPrice = carPrice

car1=Car(4, 1000)
print(car1.tire)
print(car1.carPrice)

class Bicycle(Car):
    # def __init__(self, tire, price, driventrain):
    #     self.tire=tire
    #     self.price=price
    #     self.driventrain=driventrain

    def __init__(self, tire, price,driventrain):
        super().__init__(tire, price) # 부모의 생성자
        self.driventrain=driventrain


bicycle1 = Bicycle(2,100,"시마노")
print(bicycle1.tire)
print(bicycle1.price)
print(bicycle1.driventrain)





































































































































































































































































































































































































































































































