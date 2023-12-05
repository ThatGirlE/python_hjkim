import mod1
import sys
import numpy


from mod1 import sub, sum

import mod2


print(mod1.sum(10,20))
print(mod1.sub(100,200))
sum(100,200)

print(mod2.PI) # import된 모듈에 정의되어 있는 변수를 가져와서 사용 가능

m1=mod2.Math() #import된 모듈에 정의되어 있는 클래스로 객체를 선언한 후에 가능
print(m1.solv(10))



