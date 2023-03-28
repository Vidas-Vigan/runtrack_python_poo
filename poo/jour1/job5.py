class Animal():
    def __init__(self,age=0,prenoms=0):
        self.age = age
        self.prenoms = prenoms
    # La méthode de l'âge de base
    def age_de_base(self):
        return f"L'age de l'animal {self.age} ans"
    # Plus 1 a son âge
    def viellir(self):
        return f"L'age de l'animal {self.age+1} ans"
    # Une méthode nommer qui prend en paramètre le nom de l'animal
    def nommer(self,):
        self.prenoms = 'Luna'
        
        return f"L'animal se nomme {self.prenoms}"
animal1 = Animal()
print(animal1.age_de_base())
animal2 = Animal()
print(animal2.viellir())
nom = Animal()
print(nom.nommer())



    
    