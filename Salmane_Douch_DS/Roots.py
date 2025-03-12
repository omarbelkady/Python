import math
import cmath
def roots(a, b,c):
    disc=b*b-(4*a*c)
    if(disc<0):
        ans1=(-b+cmath.sqrt((b**2)-(4*a*c)))/(2*a)
        ans2=(-b-cmath.sqrt((b**2)-(4*a*c)))/(2*a)
        return(f"The 2 non-real roots are: {ans1} and {ans2}")
    else:
        ans1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
        ans2=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
        return("The two roots are: "+str(ans1)+" and "+str(ans2))
print(roots(1,-3,2))
print(roots(1, 2, 5))