

from views.view import View
from models.Model import Model

model=Model()
v=View(model)
v.display_all_informations_events()
"""
#-----------------------------

import hashlib
from getpass import getpass
print(hashlib.algorithms_guaranteed)
chaine_mot_de_passe = b"azerty"
mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()
print(mot_de_passe_chiffre)
verrouille = True
while verrouille:
    entre = getpass("Tapez le mot de passe : ") # azerty
    # On encode la saisie pour avoir un type bytes
    entre = entre.encode()
    
    entre_chiffre = hashlib.sha1(entre).hexdigest()
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté...")
"""