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

#SECTION - EXCEPTION HANDLING

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
"""
#< enumerate() = index + value trong cùng 1 loop
my_list = [100, 200, 300, 400, 500]

for index, value in enumerate(my_list):      # store tuple for each iterations
    print(f"Index: {index} - Value: {value}")
"""

#SECTION OOP

#ANCHOR - Python Standard for Variable
"""
_name_var -> biến nội bộ (private-ish)
name_var -> interface bên ngoài (property)
"""

#SECTION - CLASSES & OBJECTS

#ANCHOR - Class Fundamentals
"""
class Employee():

  #< Defined Attributes
  _emp_name = "Jung"
  _emp_department = "IT"

  #< Methods using defined attributes
  def info(self):       #> self = this 
    print(f"Employee {self._emp_name} works for {self._emp_department}")

#< Create an object(instance) and use it
emp1 = Employee()

#< Using the class's attributes
print(f"Hi. My name is {emp1._emp_name}. I'm currently working at {emp1._emp_department} department")

#< Using the class's methods
emp1.info()     # Python tự truyền self khi gọi từ instance
"""

#ANCHOR - Constructor 
"""
#< Constructor always runs when we create new object

class Employee():

  #< Constant class attributes
  company_name = "XYZ"

  #< Defining constructor using instance attributes which are subject to the objects
  def __init__(self, employee_name, employee_dept):
    self.employee_name = employee_name
    self.employee_dept = employee_dept
  
  #< Methods using dynamic attributes
  def info(self):
    print(f"Employee {self.employee_name} works at {self.employee_dept} dept")

emp1 = Employee("Jung", "IT")     # dynamic attributes
emp1.info()

emp2 = Employee("Nguyen", "HR")
emp2.info()
"""

#ANCHOR - Instance Methods
"""
#< Used to take outer parameters to perform methods

class Employee():

  def __init__(self, emp_name, emp_dept):
    self.emp_name = emp_name
    self.emp_dept = emp_dept
  
  def info(self):
    print(f"Employee {self.emp_name} works at {self.emp_dept} department!")

emp1 = Employee("Jung", "Data")
emp1.info()
"""

#ANCHOR - Static Methods
"""
#< Used to perform basic stuffs that are irrelevant or indirectly linked to other things within the same class

class Employee():

  #< Static methods not realate to any class's attributes, class's methods,... -> Doesn't need self 
  @staticmethod           #> tell Python this is static method
  def addition(x, y):
    print(x + y)

emp1 = Employee("_", "_")
emp1.addition(6, 7)
"""

#ANCHOR - Class Methods
"""
#< Used to interact directly with the class's attributes 
#< Used "cls" instead of "self" for not confusing 

class Employee():

  company_name = "XYZ"          #> class attribute

  #< change the class attribute must use class.attribute = new_value
  def changes(self, new_company):
    Employee.company_name = new_company       

  #> tell Python only this method interacts with the class's attributes
  @classmethod       
  def changesInClass(cls, new_company):
    cls.company_name = new_company      #< now Python knows "cls" is for the class, not object 

emp1 = Employee()
emp1.changesInClass("New Company")
print(emp1.company_name)
"""

#ANCHOR - Getters & Setters (Concept)
"""
#< Getters: Return the values (Get the values)
#< Setters: Set the instance attributes

class Employee():
  
  def __init__(self, emp_name, emp_dept):
    self.emp_name = emp_name
    self.emp_dept = emp_dept

  #< Getter
  def showInfo(self):
    print(f"Employee Name: {self.emp_name}")
    print(f"Employee Department: {self.emp_dept}")

  #< Setter
  def setInfo(self, new_emp, new_dept):
    self.emp_name = new_emp
    self.emp_dept = new_dept

emp1 = Employee("Jung", "Data")
emp1.showInfo()

emp1.setInfo("JungNg", "DataEngineer")
emp1.showInfo()
"""

#ANCHOR - Getters & Setters (In Python)
"""
#< Getter returns a tuple, so we past in Setter a tuple or a list
#! Turn method to attribute

class Employee():

  def __init__(self, emp_name, emp_dept):
    self._emp_name = emp_name
    self._emp_dept = emp_dept

  #< Getter
  @property         
  def info(self):
    return self._emp_name, self._emp_dept        
  
  #< Setter: thiết kế để chỉ nhận 1 value   
  @info.setter        #> setter is same name with getter
  def info(self, new_emp):
    name, dept = new_emp        #< unpack tuple (ngầm bởi Python)
    self._emp_name = name
    self._emp_dept = dept 

emp1 = Employee("Jung", "Data")

#< Getter
name, dept = emp1.info        #< unpack return tuple
print(f"Employee {name} works at {dept}")

#< Setter
emp1.info = ("JungNg", "DataEngineer")
print(emp1.info)
"""
#!SECTION

#SECTION INHERITANCE (SINGLE, MULTILEVEL, MULTIPLE)

#ANCHOR - SINGLE
"""
#< Inherit by putting the name of the class into the params

class Company():
  def company_info(self):
    print("Company Name is: XYZ")

class Employee(Company):          # Inherits from Company class
  def employee_info(self):
    print("Employee Name is: Jung")

emp1 = Employee()

emp1.employee_info()
emp1.company_info()
"""

#ANCHOR - Inherits Attributes
"""
class Company():

  def __init__(self, _com_name):
    self._com_name = _com_name

  def company_info(self):
    print(f"Company name is {self._com_name}")

#! The class that inherits must also define the attributes from the parent class
class Employee(Company):
  
  def __init__ (self, _emp_name, _com_name):
    self._emp_name = _emp_name
    self._com_name = _com_name
  
  def emp_info(self):
    print(f"Employee name is {self._emp_name}")

emp1 = Employee("Jung", "ABC")
emp1.company_info()
"""

#ANCHOR - Inherit Methods
"""
class Company():

  def __init__(self, _com_name):
    self._com_name = _com_name

  def company_info(self):
    print(f"Company name is {self._com_name}")

#! The class that inherits must also define the attributes from the parent class
class Employee(Company):
  
  def __init__ (self, _emp_name, _com_name):
    self._emp_name = _emp_name
    self._com_name = _com_name
  
  def emp_info(self):
    print(f"Employee name is {self._emp_name}")
  
  #< Want to call the parent's function from the child class
  def company_info_child(self):
    print("This is running from the child class")
    Company.company_info(self)

emp1 = Employee("Jung", "ABC")
emp1.company_info_child()
"""

#ANCHOR - Super() Function
"""
#< The super() helps accessing the function from the parent's class (one level up - Single Level) -> (would be a mess for Multi Level)
#! Should stick to the Company.company_info(self) (suitable for any levels)

class Company():

  def __init__(self, _comp_name):
    self._comp_name = _comp_name
  
  def company_info(self):
    return self._comp_name
  
class Employee(Company):

  def __init__(self, _emp_name, _comp_name):
    self._comp_name = _comp_name
    self._emp_name = _emp_name
  
  def employee_info(self):
    return self._emp_name
  
  def company_info_child(self):
    print("This is running from the child class")
    return super().company_info()           # Company.company_info(self)

emp1 = Employee("Jung", "GeoComply")
company_name = emp1.company_info_child()
print(company_name)
"""

#ANCHOR - Pass parameters without "self."
"""
class Company():

  def __init__(self, _comp_name, _country):
    self._comp_name = _comp_name
    self._country = _country
  
  def company_info(self):
    return self._comp_name, self._country
  
class Employee(Company):

  def __init__(self, _emp_name, _comp_name, _country):
    self._emp_name = _emp_name
    
    Company.__init__(self, _comp_name, _country)        #< pass parent class's parameters here

  def employee_info(self):
    return self._emp_name

  def company_info_child(self):
    return Company.company_info(self)

emp1 = Employee("Jung", "GeoComply", "Canada")
emp_name = emp1.employee_info()
company_name, country = emp1.company_info_child()
print(f"Employee {emp_name} works for {company_name} located at {country}!")
"""

#ANCHOR - MULTIPLE
"""
class Company():
  
  def __init__(self, _comp_name):
    self._comp_name = _comp_name

  def company_info(self):
    return self._comp_name

class Country():

  def __init__(self, _country_name):
    self._country_name = _country_name
  
  def country_info(self):
    return self._country_name

class Employee(Company, Country):

  def __init__(self, _emp_name, _comp_name, _country_name):
    self._emp_name = _emp_name
  
    Company.__init__(self, _comp_name)        # Pass all the attributes
  
    Country.__init__(self, _country_name)     # Pass all the attributes
  
  def full_info(self):
    return self._emp_name, self._comp_name, self._country_name     # Child class has all the attributes from Parent class


emp1 = Employee("Jung", "GeoComply", "Canada")
name, company, country = emp1.full_info()
print(f"Employee {name} works for {company} located at {country}!")
"""

#ANCHOR - MULTI-LEVEL
"""
#< Multilevel is nested inheritance classes

class Company():
  
  def __init__(self, _comp_name):
    self._comp_name = _comp_name
  
  def company_info(self):
    return self._comp_name

class Department(Company):

  def __init__(self, _dept_name, _comp_name):
    self._dept_name = _dept_name
    Company.__init__(self, _comp_name)
  
  def comp_dept_info(self):
    return self._comp_name, self._dept_name

class Employee(Department):

  def __init__(self, _emp_name, _comp_name, _dept_name,):
    self._emp_name = _emp_name
    Department.__init__(self, _dept_name, _comp_name)       # Only needs the Department class because already inherits Company class

  def full_info(self):
    return self._emp_name, self._dept_name, self._comp_name

emp1 = Employee("Jung", "GeoComply", "Data")
name, dept, company = emp1.full_info()
print(f"Employee {name} works for {company}, position: {dept}!")
"""
#!SECTION

#SECTION MULTI-THREADING



#!SECTION


#!SECTION