#mtxt = "Hola Pinches perros Desgraciados"
mtxt = input("Ingresa la cadena de texto: ")

def isFirstUpperc(s):
    return s[0].isupper()

def getWords(s):
    return s.split()

def numOfWords(s):
    return len(getWords(s))

def reverseTxt(s):
    return s[::-1]

def lastLetterToUpperC(s):
    s2 = ""
    for i in range(len(s)):
        if s[i] == ' ':
            s2 = s2[:-1] + s[i-1].upper() + ' '
        else:
            s2 += s[i]

    s2 = s2[:-1] + s[-1].upper()

    return s2

# First
print(f"1: {isFirstUpperc(mtxt)}")

# Second
print(f"2: {numOfWords(mtxt)}")

# Third
print(f"3: {getWords(mtxt)}")

# Fourth
print(f"4: {reverseTxt(mtxt)}")

# Fifth
print(f"5: {lastLetterToUpperC(mtxt)}")