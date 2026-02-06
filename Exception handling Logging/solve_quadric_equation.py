import cmath

def solve_quadric_equation(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        d = (b**2) - (4*a*c)
        x1 = (-b-cmath.sqrt(d))/(2*a)
        x2 = (-b+cmath.sqrt(d))/(2*a)

        return f"The solution are x1={x1} and x2={x2}"

    except ZeroDivisionError:
        return "Zero Division Error"
    except (ValueError, TypeError):
        return "Could not convert string to float"


print(solve_quadric_equation(1, 5, 6)) #The solution are x1=(-3+0j) and x2=(-2+0j)
print(solve_quadric_equation(1, 3, -4)) #The solution are x1=(-4+0j) and x2=(1+0j)
print(solve_quadric_equation(0, 5, 9)) #Zero Division Error
print(solve_quadric_equation("a", 3, 1)) #Could not convert string to float