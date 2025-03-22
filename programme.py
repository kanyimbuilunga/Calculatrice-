# Définition des fonctions pour chaque opération
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"

# Boucle pour exécuter la calculatrice en continu
while True:
    print("\n--- Calculatrice ---")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Choisissez une opération (1-5) : ")

    if choix == '5':
        print("Fin du programme.")
        break

    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))

    if choix == '1':
        print("Résultat :", addition(num1, num2))
    elif choix == '2':
        print("Résultat :", soustraction(num1, num2))
    elif choix == '3':
        print("Résultat :", multiplication(num1, num2))
    elif choix == '4':
        print("Résultat :", division(num1, num2))
    else:
        print("Choix invalide, veuillez réessayer.")