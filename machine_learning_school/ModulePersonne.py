import csv
#creation du module personne
class Personne:
    """Classe Personne"""

    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.age = ""
        self.salaire = ""

    def saisie(self):
        self.nom = input('quel est votre nom :')
        self.prenom = input('quel est votre prenom :')
        self.age = int(input('quel est votre age:'))
        self.salaire = float(input('quel est votre salaire:'))

    def affichage(self):
         print(self.nom,",",self.prenom,",",self.age,",",self.salaire,"$")


    def retraite(self , limite):
        if self.age > limite :
            print("vous etes a la retraite")
        else :
            gap = limite - self.age
            print("il vous reste " +str(gap)+ " avant la retraite")



    def sauvegard_csv(self):
        with open('dictionnaire.csv', 'w') as csvfile:
             nom_champs = ['nom', 'prenom', 'age', 'salaire']
             writer = csv.DictWriter(csvfile, fieldnames=nom_champs, delimiter = ";" , lineterminator = "\n")

             writer.writeheader()
             for (k,v) in self.items():
                 writer.writerow(v)


    def dict_personne(self):
        dico = {}
        self.saisie()

        dico['nom'] = self.nom
        dico['prenom'] = self.prenom
        dico['age'] = self.age
        dico['salaire'] = self.salaire

class Employe:
    """Classe Employe"""

    def __init__(self):
        Personne.__init__(self)
        self.prime = 0.0

    def saisie(self):
        Personne.saisie(self)
        self.prime = float(input("Prime : "))
    #fin saisie

    #affichage
    def affichage(self):
        Personne.affichage(self)
        print("Sa prime : ", self.prime)
    #fin affichage
#fin classe Employé








