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
            #auth tuple of True if autified else False and id_user,id_role
            auth = self.model.authentification(name,first_name,password)
            testing-=1
        return auth
    """ add post after login """
    def post_event(self):
        auth=self.login()
        #auth tuple of True if autified else False and id_user,id_role
        if auth[0]:
            print (self.model.role_name(auth[2]))
            try:
                mois = int(input('mois: '))
                day = int(input('jour: '))
                title=input('titre: ')
                date=datetime.datetime(datetime.date.today().year,mois,day,5,52,0)
                if self.model.role_name(auth[2]) == "ADMIN":
                    description=input('description: ')
                    self.model.post_event(auth[1],title,date,description)
                elif self.model.role_name(auth[2]) == "USER":
                    self.model.post_event(auth[1],title,date,'')
            except ValueError:
                print('date incorrect !')

    """ update events user or admin """
    def update_event(self):
        auth=self.login()
        #auth tuple of True if autified else False and id_user,id_role
        if auth[0]:
            try:
                mois = int(input('mois: '))
                day = int(input('jour: '))
                new_title=input('nouveau titre: ')
                title=input('titre: ')
                date=datetime.datetime(datetime.date.today().year,mois,day,5,52,0)
                if self.model.role_name(auth[2]) == "ADMIN":
                    new_desc=input('nouvelle description: ')
                    self.model.update_event_admin(new_title,date,new_desc,title)
                elif self.model.role_name(auth[2]) == "USER":
                    self.model.update_event_user(new_title,date,title,auth[1])
            except ValueError:
                print('date incorrect !')
    """ delete event """
    def delete_event(self):
        auth=self.login()
        #auth tuple of True if autified else False and id_user,id_role
        if auth[0]:
            try:
                title=input('titre: ')
                if self.model.role_name(auth[2]) == "ADMIN":
                    self.model.delete_event_admin(title)
                elif self.model.role_name(auth[2]) == "USER":
                    self.model.delete_event_user(title,auth[1])
            except ValueError:
                print('date incorrect !')

    """ answer """
    def menu(self):
        response=input(""" taper: [ add' pour ajouter evenement,
        'update' pour metter ajour evenement,'delete' pour suprimer evenement ,
         'create' pour creation du compte 
         
         ]: """)
        return chose

    """ method main of application """
    def dispatcher(self):
        self.view.display_today_month()
        auth=self.login()
        if auth[0]:

            chose = self.menu()
            if
            



