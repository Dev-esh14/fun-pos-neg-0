"""John would like to create a function to check whether given number is
positive or negative or neutral. Help him to write an independent function
and pass different inputs to the function and check its behaviour"""

def number(a):
    if a>0:
        print("the number is positive")
    elif a<0:
        print("the number is negative")  
    else:
        print("the number is zero")

number(-5)
number(0)
number(7)

"""
OUTPUT:
the number is negative
the number is zero
the number is positive
"""