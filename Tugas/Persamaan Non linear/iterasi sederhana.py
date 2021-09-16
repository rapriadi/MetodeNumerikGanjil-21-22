import math

# fungsinya adalah x^3 + 2x^2 + 10x - 20
def f(x): 
    return x**3 + (2*(x**2)) + 10*x - 20

def bisection(a,MAX_ITER):

    print("   x    |    f(x)")

    iterasi=0

    for iterasi in range(MAX_ITER):
        iterasi+=1

        # b = 3/(a-2)
        b = (10*(a-2)/(a+2))**1/2        # x = akar kuadrat dari 10(a-2)/(a+2)

        print("%.5f"%a, " | " , "%.7f"%f(b))

        if (f(b) == 0.0):
            break
        else:
            a = b
        
    print("a : ", 3.4334305029) # Masukannya
    print("hasil : ","%.9f"%a) # Hasilnya
    print("Iterasi ke: ","%d"%iterasi) # Iterasi ke-

# a=4
a=3.4334305029
MAX_ITER=15
bisection(a,MAX_ITER)