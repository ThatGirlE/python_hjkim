import sympy
from fractions import Fraction

#처음에 가지고 있던 돈을 x
x = sympy.symbols("x")

# 가지고 있던 돈 x의 2/5가 1768원 -> x * (2/5)= 1760

f = sympy.Eq(x*Fraction('2/5'), 1760)

result = sympy.solve(f) # 리스트로 반환

print(result)
