def est_palindrome(nombre):
    """
    Cette fonction vérifie si un nombre est un palindrome.
    
    Paramètre:
    nombre (int): Le nombre à vérifier.
    
    Retourne:
    bool: True si le nombre est un palindrome, False sinon.
    """
    # Convertir le nombre en chaîne de caractères pour vérifier son inversion
    chaine = str(nombre)
    # Vérifier si la chaîne est la même lorsqu'elle est inversée
    return chaine == chaine[::-1]


def trouver_palindromes(liste):
    """
    Cette fonction prend une liste de nombres et retourne une liste contenant
    uniquement les nombres qui sont des palindromes.
    
    Paramètre:
    liste (list): La liste des nombres à analyser.
    
    Retourne:
    list: Une liste des nombres qui sont des palindromes.
    """
    # Utiliser une compréhension de liste pour filtrer les nombres palindromes
    palindromes = [nombre for nombre in liste if est_palindrome(nombre)]
    return palindromes


# Demander à l'utilisateur d'entrer une liste de nombres
print("Veuillez entrer une liste de nombres séparés par des espaces :")
entree_utilisateur = input()

# Convertir l'entrée utilisateur en une liste d'entiers
liste_de_nombres = list(map(int, entree_utilisateur.split()))

# Trouver les nombres palindromes dans la liste de l'utilisateur
palindromes = trouver_palindromes(liste_de_nombres)

# Afficher les nombres palindromes trouvés
print("Les nombres palindromes sont :", palindromes)