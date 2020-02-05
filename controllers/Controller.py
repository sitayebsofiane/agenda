from getpass import getpass
import datetime
class Controller:

    def __init__(self,model,view):
        self.model = model
        self.view = view

    def login(self):
        testing = 3
        auth = self.model.authentification('','','')
        while not auth[0] and testing>0:
            name = input("entrez votre nom: ")
            first_name = input("entrez votre prenom: ")
            password = getpass("entrez votre mot de passe: ")
            #auth tuple of True if autified else False ,id_user,id_role
            auth = self.model.authentification(name,first_name,password)
            testing-=1
        return auth

    def add_event(self):

        auth=self.login()
        if auth[0]:
            self.model.post_event(auth[1],auth[2],input('title: '),datetime.datetime.today(),input('description: '))
