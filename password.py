def main():
    get_password()

def get_password():
    password = input("Enter password: ")
    lenght(password)
    NoDigit(password)
    NoWord(password)
    specialChar(password)

def lenght(password):
    if len(str(password)) < 8:
        print("Password length must be at least 8 characters")
        get_password()
    else:
        print("1. Password lenght >= 8 characters✅")

def NoDigit(password):
    l = []
    for c in password:
        if c.isdigit():
            l.append(c)
    if len(l) == 0:
        print("Password have no digit")
        get_password()
    else:
        print("2. Password have a digit✅")

def NoWord(password):
    l = []
    for c in password:
        if c.isalpha():
            l.append(c)
    if len(l) == 0:
        print("Password have no word")
        get_password()
    else:
        print("3. Password have a word✅")

def specialChar(password):
    l = []
    for c in password:
        if c == "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*":
            l.append(c)
    if len(l) > 0:
        print("4. Password have a special character❌")
        get_password()
    else:
        print("4. Password have no special character✅")

if __name__ == "__main__":
    main()