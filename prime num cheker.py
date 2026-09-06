print("_____welcome to prime number checker app_____")
num=int(input("the number you need to check:"))

def is_prime (num):
    if num < 2 :
     return False 
    for i in range (2,num):
       if num % i == 0:
        return False

    return True
if is_prime(num):
   print(f"{num} is prime number")
else :
  print(f"{num} is not prime number")
