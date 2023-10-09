"""#python calculator
#print the options 
#ask for values to the user
#call the fucntions
#while loop continue the program until the user wants to exit"""

def add(a,b):
    answer =a+b
    print(str(a)+ " + " +str(b)+ " = " +str(answer))
    
def sub(a,b):
    answer =a-b
    print(str(a)+ " - " +str(b)+ " = " +str(answer))
    
def mul(a,b):
    answer =a*b
    print(str(a)+ " * " +str(b)+ " = " +str(answer))
    
def div(a,b):
    answer =a/b
    print(str(a)+ " / " +str(b)+ " = " +str(answer))
    
print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.division")
print("E.Exit")

choice=input("input your choice:")

if choice == "a" or choice =="A":
    print("A.Addition")
    a=int(input("input ur 1st number: "))
    b=int(input("input ur 2nd number: "))
    add(a,b)
elif choice == "b" or choice =="B":
    print("Subtration")
    a=int(input("input 1st number: "))
    b=int(input("input 2nd number: "))
    sub(a,b)
elif choice == "c" or choice =="C":
    print("Multiplication")
    a=int(input("input 1st number: "))
    b=int(input("input 2nd number: "))
    mul(a,b)
elif choice == "d" or choice =="D":
    print("Division")
    a=int(input("input 1st number: "))
    b=int(input("input 2nd number: "))
    div(a,b)
elif choice == "e" or choice =="E":
    print("Exit")
    quit()
    

    

    


