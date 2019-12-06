# -*- coding: utf-8 -*-
"""
Bisection method of finding real roots (f(x)=0) of a function f(x)
Two main restrictions:
    1) Somehow the interval for searching of roots should be specified ([a,b])4
    2) The function of interest should be somehow specified
TODO for future: GUI specification of input parameters for algebraic function or even function itself
Developed in the Spyder IDE
@author: ssklykov
"""
# %% Import section
from AlgebraicFunctionEx import fVal as f
from FuncPlotting import plotMyExampleFunc
# %% Primitive interaction with user - asking for input lower and higher borders of a searching interval
# The IPython console is used for reading and typing of input values...
# For testing the feature of the primitive prompting of an user for input values, this module should be imported
if __name__ == "main":
    try:
        a = float(input("Enter the lower border of a searching interval: "))
    except ValueError:
        print("Wrong input value - the lower border")
    try:
        b = float(input("Enter the higher border of a searching interval: "))
    except ValueError:
        print("Wrong input value - the lower border")
else:
    a = -2; b = 3  # Testing values along with test function


# %% Plotting of function
nValues = 500  # For plotting the function under revision
nFunc = 1  # Number of an function from examples
plotMyExampleFunc(f,nFunc,a,b,nValues) # calling related function for plotting

# %% Bisection method implementation
def Bisection(func,nFunc:int,a:float,b:float,epsilon:float,digitRound:int,showIteration:bool):
    # Epsilon - Presicion of equality the interesting function f(x) ~= 0
    # DigitRound - number of digits for rounding calculations (in some dependence to Epsilon)
    # nFunc - number of a predefined function
    i = 0  # For calculation of a number of iteration steps
    if (func(a,nFunc)*func(b,nFunc)<0):
        xMiddle = (a+b)/2  # The middle point in interval [a,b]
        while (abs(func(xMiddle,nFunc)) > epsilon):
            if (func(xMiddle,nFunc)*func(a,nFunc) < 0):
               b = xMiddle # [a,b] => [a,xMiddle] - the bisection operation
            elif (func(xMiddle,nFunc)*func(b,nFunc) < 0):
                a = xMiddle
            else:
                print("Apparantly, there is more than real 1 root or no roots...")
                return None
            # The row below is for showing iteration process
            if showIteration: i += 1; print("Iteration step #",i,"Root approximation is: ",round(xMiddle,digitRound+1))
            xMiddle = (a+b)/2  # For allowing iteration ad test next approximation to the root
        return float(round(xMiddle,digitRound)) # In the end of while cycle
    else:
        print("There is no real roots between input a and b or more than 1 real root")
        return None


# %% Testing of implemented methods
xRoot = Bisection(f,nFunc,a,b,0.01,2,True)
print("The calculated real root is",xRoot)
