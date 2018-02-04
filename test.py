import quad
from sympy import pprint,symbols

#tests

x,a,b,c = symbols('x,a,b,c')

pprint(x**2 +x)
print("quad.solve_quad(1,1,0)")
print(quad.solve_quad(1,1,0))


pprint(x**2 +x-1)
print("quad.solve_quad(1,1,-1)")
print(quad.solve_quad(1,1,-1))


pprint(2*x**2 +3*x-10)
print("quad.solve_quad(2,3,-10)")
print(quad.solve_quad(2,3,-10))

