#SECTION - ENCAPSULATION - ACCESS MODIFIERS

#< Encapsulation is for security reason.
#< For some variables, we don't want the user to see or use it.

#ANCHOR - Definition
"""
class MyClass():

  #< Class variables
  var1 = "Jung"
  var2 = "Nguyen"

  #< Public variables
  def __init__(self, ex1, ex2, ex3):
    self.ex1 = ex1
    self.ex2 = ex2
    self.ex3 = ex3
  
  #< Protected variables (One underscore)
  def __init__(self, _ex1, _ex2, _ex3):
    self._ex1 = _ex1
    self._ex2 = _ex2
    self._ex3 = _ex3
  
  #< Private variables (Add 2 underscores)
  def __init__(self, _ex1, _ex2, _ex3):
    self.__ex1 = _ex1 
    self.__ex2 = _ex2
    self.__ex3 = _ex3
  
  #< Use getter to access private variables
  @property
  def get_private(self):
    return self.__ex1

obj = MyClass(1, 2, 3)
print(obj.ex1)        # access public variables
print(obj._ex1)       # access protected variables
print(obj.get_private)  # access private variables
"""
#!SECTION

#SECTION - POLYMORPHISM & DECORATORS

#ANCHOR - POLYMORPHISM
"""
#< Same methods but in different classes
#< Same functionality, same action but different implementation.

class api_fetch():

  def fetch(self):
    print("Fetching data from API...")

class database_fetch:

  def fetch(self):
    print("Fetching data from Database...")

class s3_fetch:

  def fetch(self):
    print("Fetching data from S3...") 

obj = database_fetch()
obj.fetch()
"""

#ANCHOR - DECORATORS
"""
#< Decorator = “wrapper” cho function
#< Giúp thêm logic mà không sửa code gốc
#< Dùng cú pháp @decorator_name

def my_decorator(func):
  def mainfunc(*args, **kwargs):    # arguments of any type
    print("Before calling the function")
    response = func(*args, **kwargs)
    print("After calling the function")
    return response
  
  return mainfunc

@my_decorator
def fetch_data(url:str, path:str):
  return (f"Fetching data from {url} and saving to {path}")

response = fetch_data("https://api.example.com/data", "/tmp/data.json")
print(response)
"""
#!SECTION

#SECTION - PYDANTIC For Schema Validation

#ANCHOR - Pydantic
"""
#< Pydantic = validate + parse data
#< Schema = định nghĩa cấu trúc dữ liệu
#< Giúp code an toàn, rõ ràng, ít bug hơn

from pydantic import BaseModel

class employee_schema(BaseModel):
  name: str
  id: int
  department: str

obj = employee_schema(name="Jung", id=1, department="Data")     # direct
print(obj)

obj1 = employee_schema(**{"name": "Jung", "id": "1", "department": "Data"})     # unpack dict (**)
print(obj1)
"""

#ANCHOR - Coercion vs Strict types
"""
from pydantic import BaseModel ,StrictInt

#! Coercion (ép kiểu linh hoạt)
#> Tự động convert dữ liệu sang kiểu mong muốn nếu có thể
#> VD: khai báo age: int nhưng nếu input age: "25" thì vẫn tự  convert sang int
class student_info(BaseModel):
  name: str
  age: int

student = student_info(**{"name": "Jung", "age": "21"})
print(student)

#! Strict type (kiểu nghiêm ngặt)
#> Không cho phép ép kiểu
#> VD: khai báo age: StrictInt, input age: "25" sẽ lỗi
class student_info(BaseModel):
  name: str
  age: StrictInt

student1 = student_info(**{"name": "Jung", "age": "21"})
print(student1)
"""

#ANCHOR - Field
"""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal          # to use special data types

class employee_schema(BaseModel):

  name: str = Field(..., min_length=3, max_length=50)     # '...' means required
  age: int = Field(..., gt=18, lt=65)
  email: EmailStr = Field(..., description="Employee's email address")
  department: Optional[str] = None
  gender: Literal["Male", "Female", "Other"] = Field(..., description="Employee's gender")

emp = employee_schema(name="Jung", age=21, email="abc@gmail.com", department="IT", gender="Male")
print(emp)
"""
#!SECTION

#ANCHOR - Serialization 
"""
#< Quá trình chuyển object (Python) → format có thể lưu trữ hoặc truyền đi (JSON, string, bytes…)

import json

data = {
  "name": "Jung",
  "age": 21
}
json_str = json.dumps(data)        # serialize
print(json_str)
"""

#ANCHOR - Deserialization (JSON -> object)
"""
import json

data = {
  "name": "Jung",
  "age": 21
}
json_str = json.dumps(data)
data1 = json.loads(json_str)
print(data1)
"""

#ANCHOR - Async/Await
"""
import asyncio

async def main():         #< tạo coroutine
  print("Hello")
  await asyncio.sleep(3)      #< "chờ" coroutine hoàn thành
  print("Word")

asyncio.run(main())
"""

#ANCHOR - Multiple Coroutines With Gather
"""
import asyncio

async def api_call(url:str ,delay:int):
  print(f"Fetching data from: {url}")
  await asyncio.sleep(delay)
  print(f"Data fetched from {url}")

async def main():
  #< Creating Tasks with gather
  tasks = await asyncio.gather(
    api_call("http://api1.com", 2),
    api_call("http://api2.com", 3),
    api_call("http://api3.com", 1)
  )
  print("All API calls completed")

asyncio.run(main())
"""

#SECTION - APIs

#ANCHOR - GET
"""
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

#< Status Code
print(response.status_code)

#< Response Body
print(response.json())

#< Parse JSON response
data = response.json()
json_data = json.dumps((data), indent=2)      #> format JSON cho dễ đọc, xuống dòng, thụt vào 2 dấu cách mỗi cấp
print(json_data)
"""

#ANCHOR - POST
"""
import requests

url = "https://jsonplaceholder.typicode.com/posts"

#< Method 1: Using JSON parameter
data = {
  "title": "foo",
  "body": "bar",
  "userID": 1
}
response = requests.post(url, json=data)

#< Method 2: Using Form Data 
form_data = {
  "title": "xyz",
  "body": "abc",
  "userID": 1
}
response = requests.post(url, data=form_data)
"""

#ANCHOR - Query Parameters
"""
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

params = {
  "userId": 1
}

response = requests.get(url, params=params)

json_str = json.dumps(response.json(), indent=2)        #< response.json(): JSON → Python object

print(json_str)
"""
#!SECTION


#SECTION - Headers & Authentication

#ANCHOR - Headers
"""
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
  "User-Agent": "Python",
  "Content-Type": "application/json",
  "Custom-Header": "CustomValue"
}

response = requests.get(url, headers=headers)
print(response.status_code)
"""

#ANCHOR - Authentication
"""
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

#! Authentication JWT
headers = {
  "Authorization": f"Bearer {token}",
  "Content-Type": "application/json",
}

#! API Key Authentication
headers = {
  "X-API-Key": "your_api_key_here",
}

#! Basic Authentication
from requests.auth import HTTPBasicAuth

response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
"""
#!SECTION

#SECTION - PyTest 

#< PyTest = công cụ test Python
#< Dễ viết (assert), tự động phát hiện test

#ANCHOR - PyTest

def weather_check(temp:float)->str:         #> input:float, returns (->) string
  if temp < 0:
    return "It's freezing outside!"
  elif temp < 15:
    return "It's a bit chilly!"
  elif temp < 25:
    return "The weather is pleasant."
  else:
    return "It's hot outside!"


#!SECTION

