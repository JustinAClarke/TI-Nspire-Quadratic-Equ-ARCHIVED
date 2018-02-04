


from sympy import pprint,symbols,Symbol
import sys

def solve_quad(a,b,c):
    D = (b*b -4*a*c)**0.5
    x_1 = (-b-D)/(2*a)
    x_2 = (-b+D)/(2*a)
    
    return {'x1':x_1,'x2':x_2}


def print_quad(a,b,c):
    x = Symbol('x')
    #xa,xb,xc = symbols(a,b,c)
    za,zb,zc = symbols('a,b,c')
    xa = Symbol(str(a))
    xb = Symbol(str(b))
    xc = Symbol(str(c))
    pm = Symbol('±')
    m = Symbol('-')
    #print original
    #original = "{a}x**2+{b}x+{c}".format(a=a,b=b,c=c)
    original = a*x**2+b*x+c
    pprint(original)
    
    #print half working
    #working = "(-{b}+-({b}**2-4{a}{c})**1/2)/2{a}".format(a=a,b=b,c=c)
    #working = "(-{b}+-({b}**2-4{a}{c})**1/2)/2{a}".format(a=a,b=b,c=c)
    
    working = (-zb*pm*(zb*zb -4*za*zc)**0.5)/(2*za)
    working1 = (-xb + (xb*xb -4*xa*xc)**0.5)/(2*xa)
    working2 = (-xb - (xb*xb -4*xa*xc)**0.5)/(2*xa)
    #working2 = (-b-(b**2-4*a*c)**1/2)/2*a
    pprint(working)
    pprint(working1)
    pprint(working2)
    #print(pprint(working2))
    
    #print final
    final = solve_quad(a,b,c)
    x_1 = final['x1']
    x_2 = final['x2']
    print("x1 = {}".format(x_1))
    print("x2 = {}".format(x_2))

if __name__ == '__main__':
    #print("count {}".format(sys.argv))
    if len(sys.argv) != 4:
        print("usage: {} <a> <b> <c>".format(sys.argv[0]))
    else:
        #print("a{},b{},c{}".format(sys.argv[1],sys.argv[2],sys.argv[3]))
        print_quad(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
        #print(solve_quad(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
