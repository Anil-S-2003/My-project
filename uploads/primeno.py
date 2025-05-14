num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):  # Check divisors from 2 to sqrt(num)
        if num % i == 0:  
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
