def main():
    try:
        sum1 = int(input("Enter first number: "))
    except:
        print("Enter a number!")

    try:
        sum2 = int(input("Enter second number: "))
    except:
        print("Enter a number!")
    choice(sum1,sum2)

def choice(sum1,sum2):
    print("Choice")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. square")
    try:
        chc = int(input("Enter your choice: "))
    except:
        print("Enter a 1-5")
    if chc == 1:
        print(plus(sum1,sum2))
    if chc == 2:
        print(minus(sum1,sum2))
    if chc == 3:
        print(multiplication(sum1,sum2))
    if chc == 4:
        print(division(sum1,sum2))
    if chc == 5:
        print(square(sum1,sum2))



def plus(sum1, sum2):
    sum3 = sum1 + sum2
    return f"{sum1} + {sum2} = {sum3}"

def minus(sum1, sum2):
    sum3 = sum1 - sum2
    return f"{sum1} - {sum2} = {sum3}"

def multiplication(sum1, sum2):
    sum3 = sum1 * sum2
    return f"{sum1} * {sum2} = {sum3}"

def division(sum1, sum2):
    sum3 = sum1 / sum2
    return f"{sum1} / {sum2} = {sum3}"

def square(sum1, sum2):
    sum3 = sum1 ** sum2
    return f"{sum1}^{sum2} = {sum3}"


if __name__ == "__main__":
    main()