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
def length_check(p):
    return 8 <= len(p) <= 16

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
def no_pass(p):
    return "pass" not in p


#Must not contain the phrase "qwerty"
def no_qwerty(p):
    return "qwerty" not in p.lower() 

#Must not contain the phrase "123"
def no_123(p):
    return "123" not in p

#Running a check for all requirements
if numbers(password) and characters(password) and upperCase(password) and lowerCase(password) and length_check(password) and no_qwerty(password) and no_123(password):
    print("Success!")
else:
    incorrect()