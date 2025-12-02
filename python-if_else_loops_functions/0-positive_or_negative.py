   #!/usr/bin/python3
  1 import random
  2 number = random.randint(-10, 10)
  3 if(number == 0):
  4     print(f"{number} is zero")
  5 elif (number > 0):
  6     print(f"{number} is positive")
  7 else:
  8     print(f"{number} is negative")
