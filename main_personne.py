import ModulePersonne as mp

p = mp.Personne()

#affichage des membre s de p
print(dir(p))

#affectations
p.nom = input('quel est votre nom :')
p.prenom = input('quel est votre prenom :')
p.age = input('quel est votre age:')
p.salaire = input('quel est votre salaire')

