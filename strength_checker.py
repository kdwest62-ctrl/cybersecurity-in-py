def check_strength(password):
    def check_length(p):
        if len(p) >= 8:
            return 1
        else:
            return 0
    def check_numbers(p):
        num = []
        for char in p:
            if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num.append(char)
        if len(num) > 0:
            return 1
        else:
            return 0
    def check_special(p):
        spec = []
        for item in p:
            if item in ['!', '@', '#', '$', '%', '^', '&', '*']:
                spec.append(item)
        if len(spec) > 0:
            return 1
        else:
            return 0
    def check_lower_upper(p):
        lower = []
        upper = []
        for element in p:
            if element.islower():
                lower.append(element)
        for element in p:
            if element.isupper():
                upper.append(element)
        if len(lower) > 0 and len(upper) > 0:
            return 1
        else:
            return 0
    strength = check_length(password) + check_numbers(password) + check_special(password) + check_lower_upper(password)
    if strength == 0 or strength == 1:
        return "weak"
    elif strength == 2 or strength == 3:
        return "medium"
    else:
        return "strong"

user_password = input("Input password: ")
print(f"Strength: {check_strength(user_password)}")
