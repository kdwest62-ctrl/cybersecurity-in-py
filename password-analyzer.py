import string

def length(p):
    if len(p) >= 8:
        return "Length: OK"
    else:
        lack = 8 - len(p)
        return f"Password only has {len(p)} characters. Add {lack} or more"
def upper_lower(p):
    upper = []
    lower = []
    for item in p:
        if item in string.ascii_uppercase:
            upper.append(item)
    for item in p:
        if item in string.ascii_lowercase:
            lower.append(item)
    if len(upper) > 0:
        if len(lower) > 0:
            return "Uppercase and Lowercase: OK"
        else:
            return "Add at least 1 lowercase letter"
    elif len(lower) > 0:
        if len(upper) > 0:
            return "Uppercase and Lowercase: OK"
        else:
            return "Add at least 1 uppercase letter"
    else:
        return "Password needs to have at least 1 uppercase and 1 lowercase letter"
def digits(p):
    digit = []
    for item in p:
        if item in string.digits:
            digit.append(item)
    if len(digit) > 0:
        return "Digits: OK"
    else:
        return "Password needs to have at least 1 digit"
def punctuation(p):
    punctuate = []
    for item in p:
        if item in string.punctuation:
            punctuate.append(item)
    if len(punctuate) > 0:
        return "Punctuation: OK"
    else:
        return "Password needs to have at least 1 punctuation"
password = input("Input password: ")
print(f"{length(password)}\n{upper_lower(password)}\n{digits(password)}\n{punctuation(password)}")
