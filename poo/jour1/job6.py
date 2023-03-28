class Rectangle():
    # Créaction des atributs privées
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur 
    # Le getter du longueur
    def get__longueur(self):
        return self.__longueur
    # Le setter de longueur
    def set__longueur(self,longueur):
        self.__longueur = longueur
    # Getter de largeur
    def get_largeur(self):
        return self.__largeur
    # setter de largeur
    def set__largeur(self,largeur):
        self.__largeur = largeur
# Créaction du rectangle
rectangle = Rectangle(10,5)
# Afficher les valeurs initiales
print("longueur:",rectangle.get__longueur())
print("largeur:",rectangle.get_largeur())
    
    
    
