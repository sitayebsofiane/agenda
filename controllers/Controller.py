from getpass import getpass
import datetime
class Controller:

    def __init__(self,model,view):
        self.model = model
        self.view = view

    """ method to check if events is abble """
    def check_title_date(self):
        title = input('titre: ')
        minute = int(input('nouvelle minute: '))
        houre = int(input('nouvelle houre: '))
        month = int(input('nouveu mois: '))
        day = int(input('nouveu jour: '))
        date_enter = datetime.datetime(datetime.date.today().year,month,day,houre,minute,0)
       
        return title,date_enter


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
    def post_event(self,auth):
        #auth tuple of True if autified else False and id_user,id_role
        if auth[0]:
            print ('vous êtes: ',self.model.role_name(auth[2]),'si vous êtes USER vous avez des droit restreint ')
            try:
                check = self.check_title_date()
                title = check[0]
                date = check[1]
                if self.model.role_name(auth[2]) == "ADMIN":
                    description=input('description: ')
                    self.model.post_event(auth[1],title,date,description)
                elif self.model.role_name(auth[2]) == "USER":
                    self.model.post_event(auth[1],title,date,'')
            except ValueError:
                print('date incorrect !')

    """ update events user or admin """
    def update_event(self,auth):
        #auth tuple of True if autified else False and id_user,id_role
        if auth[0]:
            print ('vous êtes: ',self.model.role_name(auth[2]),'si vous êtes USER vous avez des droit restreint ')
            try:
                check = self.check_title_date()
                title = check[0]
                date = check[1]
                new_title = input('nouveau titre: ')
                if self.model.role_name(auth[2]) == "ADMIN":
                    new_desc = input('nouvelle description: ')
                    self.model.update_event_admin(new_title,date,new_desc,title)
                elif self.model.role_name(auth[2]) == "USER":
                    self.model.update_event_user(new_title,date,title,auth[1])
            except ValueError:
                print('date incorrect !')

    """ delete event """
    def delete_event(self,auth):
        #auth tuple of True if autified else False and id_user,id_role
        if auth[0]:
            print ('vous êtes: ',self.model.role_name(auth[2]),' si vous êtes USER vous avez des droit restreint ')
            try:
                title=input('titre de ce que vous voulez supprimer: ')
                if self.model.role_name(auth[2]) == "ADMIN":
                    self.model.delete_event_admin(title)
                elif self.model.role_name(auth[2]) == "USER":
                    self.model.delete_event_user(title,auth[1])
            except ValueError:
                print('date incorrect !')

    """ answer """
    def menu(self):
        choose=input(""" taper: [ 'display' pour afficher ,add' pour ajouter evenement,
        'update' pour metter ajour evenement,'delete' pour suprimer evenement ,
         'create' pour creation du compte ,'addroleuser' pour ajouter un role
         
         ]: """)
        return choose

    """ method main of application """
    def dispatcher(self):
        auth=self.login()
        while auth[0] and input("taper q pour quiter , ENTER si vous voulez continuer: ").lower() != 'q':
            self.view.display_today_month()
            self.view.display_pre_or_next_month()
            choose = self.menu()

            if choose == 'add':
                self.post_event(auth)

            if choose == 'update':
                self.update_event(auth)

            if choose == 'delete':
                self.delete_event(auth)

            if choose == 'display':
                a=self.model.role_name(auth[2])
                self.view.display(a)

            if choose == 'create' and self.model.role_name(auth[2])== 'ADMIN':
                if self.model.creation_count_user(input('name: '),input('firstname'),input('password')):
                    print('count creer')
                else:
                    print('erreur')
                    
            if choose == 'addroleuser' and self.model.role_name(auth[2])== 'ADMIN':
                if self.add_role_user(input('name: '),input('firstname: '),input('role: ')):
                    print('role ajouter')
                else:
                    print('pas bien passer')


            



