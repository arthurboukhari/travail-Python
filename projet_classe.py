marque = ["audi","bmw","mercedes"]
model = [ "R8" , "S5" , "RS4" , "Q8" , "G63" , "C63" , "SLS" , "M3" , "M4" , "M5" , "X6"]
couleur = ["rouge" , "bleu" , "vert" , "jaune" , "noir" , "gris" , "blanc" ]


class voiture:
    def __init__(self, marque, model, couleur, nb_porte, boite, carburant):
        self.model = model
        self.couleur = couleur        
        self.nb_porte = nb_porte
        self.boite = boite
        self.carburant=carburant

print("quel est le marque souhaité ?")
a_marque = input()
print("quel est le model souhaité ?")
a_model = input()
print("quel est la couleur souhaité ?")
a_couleur = input()
print("quel est le nombre de porte souhaité ?")
a_nb_porte = input()
print("quel est le type de boite souhaité ?")
a_boite = input()
print("quel est le type de carburant souhaité ?")
a_carburant = input()

if __name__ == "__main__":
    v = voiture (a_marque, a_model, a_couleur, a_nb_porte, a_boite, a_carburant)

    for i in range (1,3):
        if marque[i] == a_marque:
            print("la marque est disponible ! ")
    
    for i in range (1,11):
        if model[i] == a_model:
            print("le model est disponible ! ")
    for i in range (1,7):
        if couleur[i] == a_couleur:
            print("le couleur est disponible ! ")

# print(v.marque)
# print(v.model)
# print(v.couleur)
# print(v.nb_porte)
# print(v.boite)
# print(v.carburant)





# if m == "audi":
#     print("quel est le modele souhaité ?")
#     a_modele = input()
#     print("quel est la couleur souhaité ?")
#     a_couleur = input()
#     print("quel est le nombre de porte souhaité ?")
#     a_nb_porte = input()
#     print("quel est le type de boite souhaité ?")
#     a_boite = input()
#     print("quel est le type de carburant souhaité ?")
#     a_carburant = input()

# if m == "bmw":
#     print("quel est le modele souhaité ?")
#     b_modele = input()
#     print("quel est la couleur souhaité ?")
#     b_couleur = input()
#     print("quel est le nombre de porte souhaité ?")
#     b_nb_porte = input()
#     print("quel est le type de boite souhaité ?")
#     b_boite = input()
#     print("quel est le type de carburant souhaité ?")
#     b_carburant = input()

# if m == "mercedes":
#     print("quel est le modele souhaité ?")
#     m_modele = input()
#     print("quel est la couleur souhaité ?")
#     m_couleur = input()
#     print("quel est le nombre de porte souhaité ?")
#     m_nb_porte = input()
#     print("quel est le type de boite souhaité ?")
#     m_boite = input()
#     print("quel est le type de carburant souhaité ?")
#     m_carburant = input()