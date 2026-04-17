#ANCHOR - *args
"""
#< *args (variable-length arguments): Nhận nhiều đối số không xác định sl
#< Dùng khi không biết trước sl tham số truyền vào

def my_func(*args):
  print(args, type(args))

my_func(20, 60, 70, 90, 100)        # type = tuple
"""

#ANCHOR - **kwargs
"""
#< **kwargs (keyword arguments): Nhận nhiều đối số dạng key = value
#< ** dùng để gom keyword arguments thành một dictionary.

def my_func(**kwargs):
  print(kwargs, type(kwargs))     # type = dictionary
  print(kwargs.keys())

my_func(a = 20, b = 30, c = 40)
"""

#ANCHOR - Lambda Functions
"""
x, y = map(int, input().split())
addition = lambda x, y : x + y
var = addition(x, y)
print(var)
"""

#SECTION - Exception Handling

#ANCHOR - Normal way
"""
#< try-except method
x = "10"
try:
  if (x > 10):
    print("Greater than 10")
  else:
    print("Bla bla")

except:
  print("Hey, you have an error!")  

print("Hello, World!")        # still execute because we have try-except
"""

#ANCHOR - Log out error
"""
x = "10"
try:
  if x > 10:
    print("Greater than 10")
  else:
    print("Blah Blah")

except Exception as e:        #> e is the error, using the Exception method
  print(f"Hey, you got this error: {e}")              #< print out the error as well

print("Hello, World")
"""
#!SECTION

#ANCHOR - F-string
"""
name = "Jung"
age = "20"

print(f"Hello. My name is {name}. I'm {age} years old!")

price = 123.456789
print(f"Price: {price:.2f}")        #< 2 số sau dấu phẩy
"""

#ANCHOR - Finally
"""
#< Written after the exception. Will run no matter what
x = "10"
try:
  if x > 10:
    print("Greater than 10")
  else:
    print("blah blah")

except Exception as e:
  print(f"Error: {e}")

finally:
  print("This will run no matter what")
"""

#ANCHOR - Return command
"""
def my_func(x):
  try:
    if x % 2 == 0:
      return True       #< take the exit from here. Final print won't run
  
  except Exception as e:    
    print(f"Error: {e}")

  print("Hello world")

print(my_func(4))
"""

#ANCHOR - Build/Create Error (User Error)
"""
age = 17

if age < 18:
  raise ValueError("Under 18 is not allowed")   # ValueError: sai giá trị

if age < 18:
  raise Exception("Under 18 is not allowed")    # Exception: base class cho hầu hết các lỗi trong Python
"""

#ANCHOR - Enumerate function

my_list = [100, 200, 300, 400, 500, 600]