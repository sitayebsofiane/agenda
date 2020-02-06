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
        if auth[0]:
            try:
                mois = int(input('mois: '))
                day = int(input('jour: '))
                d1=datetime.datetime(datetime.date.today().year,mois,day,5,52,0)
                if self.model.role_name(auth[2]) == "ADMIN":
                    new_title=input('nouveau titre: ')
                    new_desc=input('nouvelle description:')
                    title=input('titre: ')
                    self.model.update_events_admin(new_title,d1,new_desc,title)
                elif self.model.role_name(auth[2] == "USER"):
                    new_title=input('nouveau titre: ')
                    new_desc=input('nouvelle description:')
                    title=input('titre: ')
                    self.model.update_events_user(new_title,d1,title)
            except ValueError:
                print('date incorrect !')

        
