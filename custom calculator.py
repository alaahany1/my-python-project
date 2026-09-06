print("welcome to calculator application")
num1=(float(input("enter the frist number:")))
operation=(input("enter the operation (+,-,*,/,%):"))
num2=(float(input("enter the second number:")))

if operation == "+" :
    result= num1 + num2
    print(f"{num1} + {num2} ={result}" )

elif operation == "*" :
    result= num1 * num2
    print(f"{num1} * {num2} ={result}" )

elif operation == "-" :
    result= num1 - num2
    print(f"{num1} - {num2} ={result}" )

elif operation == "/" :
    if num2 != 0 :
     result= num1 / num2
     print(f"{num1} / {num2} ={result}" )
    else : print("can't division by zero")


elif operation == "%" :
    result= num1 % num2
    print(f"{num1} % {num2} ={result}" )

else :
    print("invaled operation",operation)
