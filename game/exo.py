userName = input ("Votre nom : ")

print(userName)

age = input('votre âge: ')

def isNum (value: str) -> bool:
    try:
        int(value)
        return True
    except:
        return False

while not isNum (age) :
    age = input('votre âge (numérique): ')

