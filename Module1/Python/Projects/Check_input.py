
#! Validate user input exercise
#< 1. Username is no more than 12 characters
#< 2. Username must not contain spaces
#< 3. Username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
  print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
  print("Your username can't contain spaces")
elif not username.isalpha():        # contains only alphabetical
  print("Your username can't contain numbers")
else:
  print(f"Welcome {username}")