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
    def add_events(self):

        auth=self.login()

        if auth[0]:
            try:
                mois = int(input('mois: '))
                day = int(input('jour: '))
                new_title=input('titre: ')
                title=input('titre: ')
                date=datetime.datetime(datetime.date.today().year,mois,day,5,52,0)
                if self.model.role_name(auth[2]) == "ADMIN":
                    description=input('description:')
                    self.post_event_admin(auth[1],title,date,description):
                elif self.model.role_name(auth[2] == "USER"):
                    self.model.post_event_user(auth[0],title,date)
            except ValueError:
                print('date incorrect !')

    """ update events user or admin """
    def update_events(self):

        auth=self.login()

        if auth[0]:
            try:
                mois = int(input('mois: '))
                day = int(input('jour: '))
                new_title=input('nouveau titre: ')
                title=input('titre: ')
                date=datetime.datetime(datetime.date.today().year,mois,day,5,52,0)
                if self.model.role_name(auth[2]) == "ADMIN":
                    new_desc=input('nouvelle description:')
                    self.model.update_events_admin(new_title,date,new_desc,title)
                elif self.model.role_name(auth[2] == "USER"):
                    new_title=input('nouveau titre: ')
                    title=input('titre: ')
                    self.model.update_events_user(new_title,d1,title)
            except ValueError:
                print('date incorrect !')

        
