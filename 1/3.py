'''Write a program to find the simple interest.
Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)
'''
P=int(input("enter the principle amount"))
R=float(input("enter the intrest rate"))
n=float(input("enter the number of years"))
SI=(P*R*n)/100
print(SI)