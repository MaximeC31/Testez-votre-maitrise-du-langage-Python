def square(number):
    if not isinstance(number, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return number * number


print(square(4))
print(square("abc"))
