class Personne():
    # Construteur
    def __init__(self,age=14):
        self.age = age
    # Méthode afficher âge
    def afficherAge(self):
        print("L'âge de la personne est", self.age)
    # Méthode bonjour
    def bonjour(self):
        print("Hello")
    # Méthode pour modifier l'âge de la personne
    def modifierAge(self,age=15):
        self.age = age
        return print("L'âge de la personne a changer de", self.age)
# Créer une classe Eleve qui va hériter de la classe Personne
class Eleve(Personne):
    # Constructeur
    def __init__(self,):
    # Une méthode publique allerEncours
    def allerEncours(self):
        print("Je vais en cours")

    

# Affiche dans le terminal je vais en cours
affich_cours = Personne()
print()


# Afficher l'âge dans le terminal
affich_nom = Personne()
print(affich_nom.afficherAge())
# Afficher hello dans le terminal
affich_salut = Personne()
print(affich_salut.bonjour())
# Afficher modifer âge dans le terminal
change_age = Personne()
print(change_age.modifierAge())

