from getpass import getpass
import datetime
class Controller:

    def __init__(self,model,view):
        self.model = model
        self.view = view
    """ login with role """
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
    """ add post after login """
    def add_event(self):

        auth=self.login()

        if auth[0]:
            self.model.post_event(auth[1],auth[2],input('title: '),datetime.datetime.today(),input('description: '))

    """ update events user or admin """
    def update_events(self):

        auth=self.login()
        print(auth)
        if auth[0]:
            if self.model.role_name(auth[2]) == "ADMIN":
                self.model.update_events_admin(input('nouveau titre: ')
                ,input('nouvelle date: '),input('nouvelle description:'),input('titre: '))
            elif self.model.role_name(auth[2] == "USER"):
                self.model.update_events_user(input('nouveau titre: ')
                ,input('nouvelle date: '),input('titre: '))

        
