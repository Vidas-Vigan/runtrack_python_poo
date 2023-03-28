class Livre():
    def __init__(self,titre,auteur,nbr_page):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbr_page = nbr_page
    # getter de titre
    def get__titre(self):
        return self.__titre
    # setter de titre
    def set__titre(self,tous_a_bord_de_nos_messermitch_bf109):
        self.__titre = tous_a_bord_de_nos_messermitch_bf109
    # getter de l'auteur
    def get__auteur(self):
        return self.__auteur
    # setter de l'auteur
    def set__auteur(self,adolph_galland):
        self.__auteur = adolph_galland
    # getter nombre de page
    def get__nbr_page(self):
        return self.__nbr_page
    # set nombre de page
    def set__nbr_page(self,nombre_positif):
        self.__nbr_page = nombre_positif
# Créaction charactère string
positive ="1,2,3,4,6,7,8,9,10"
negative ="-1,-2,-3,-4,-5,-6,-7,-8,-9,-10"
if Livre in positive:
    if positive == Livre:
        print("La valeur est changer")
    else:
        print("La valeur n'est pas changer")





