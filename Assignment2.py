#a function called "factorial" that takes a single argument "n" and returns the factorial of "n"

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

result = factorial(5)
print(result)  # Output: 120
