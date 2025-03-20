num = int(input("Enter a number: "))


def check(num):
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    return "Not divisible by 3 or 5"
  
print(check(num))