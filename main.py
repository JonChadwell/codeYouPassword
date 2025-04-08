#Create error message 
def incorrect():
    incorrect_pass = """This password does not meet the following requirements:
- Does not contain the phrase "pass" in any format

- Contains 8-16 characters
- Contains one of the special characters: %$#^&*!@()
- Contains at least one number 0-9
- Contains at least one capital letter
- Starts with a lowercase letter
- Does not contain the phrase "pass" in any format
- Does not contain the phrase "qwerty" in any format
- Does not contain the phrase "123"

Please enter a password that conforms to the above restrictions:"""
    print(incorrect_pass)

#Create a password
password = input("Please create a password meeting the proper criteria. ")

#Password must contain 8-16 characters


#Must contain one of the special characters %$#^&*!@()
def characters(c):
    specialCharacters = "%$#^&*!@()"
    return any(char in specialCharacters for char in c)

#Must contain at least one number 0-9
def numbers(n):
    specialNumbers = "0123456789"
    return any(num in specialNumbers for num in n)

#Must contain at least one capital letter
def upperCase(u):
    return any(char.isupper() for char in u)

#Must start with a lower case letter
def lowerCase(l):
    return any(char.islower() for char in l)

#must not contain the phrase "pass"


#Must not contain the phrase "qwerty"


#Must not contain the phrase "123"


#Running a check for all requirements
if numbers(password) and characters(password) and upperCase(password) and lowerCase(password):
    print("Success!")
else:
    incorrect()