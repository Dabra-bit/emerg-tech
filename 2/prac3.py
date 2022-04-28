import re

def validateEmail(s):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, s)

mtxt = input("Introduzca el email: ")
if validateEmail(mtxt):
    print("Es email")
else:
    print("No es email")