# Fonction d'addition
def addition(a, b):
    return a + b

# Fonction de soustraction
def soustraction(a, b):
    return a - b

# Fonction de multiplication
def multiplication(a, b):
    return a * b

# Fonction de division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: division par zéro!"

# Fonction principale
def calculatrice():
    print("Bienvenue dans la calculatrice!")
    while True:
        print("Veuillez sélectionner une opération:")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")
        
        choix = input("Votre choix (1/2/3/4/5): ")
        
        if choix == "5":
            print("Au revoir!")
            break
        
        num1 = float(input("Entrez le premier nombre: "))
        num2 = float(input("Entrez le deuxième nombre: "))
        
        if choix == "1":
            print("Résultat: ", addition(num1, num2))
        elif choix == "2":
            print("Résultat: ", soustraction(num1, num2))
        elif choix == "3":
            print("Résultat: ", multiplication(num1, num2))
        elif choix == "4":
            print("Résultat: ", division(num1, num2))
        else:
            print("Choix invalide. Veuillez réessayer.")

# Appel de la fonction principale
calculatrice()
