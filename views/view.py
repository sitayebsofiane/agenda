
import calendar
import datetime
import time
from views.entities.Events import *
from views.entities.User import *
from views.entities.Role import *

class View:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self,model):
        self.model=model
    """method for decorate display"""
    def decorate(self,func):
        print(View.OKBLUE + "-----------------------------------------------------------------------------------------" )
        return func


    """  The home page displays today's date and calendar for the current month """
    def display_today_month(self, month = datetime.date.today().month):
        year  = datetime.date.today().year
        jour = time.strftime("%A")
        if jour == "Monday":
            jour = "Le Lundi"
        if jour == "Tuesday":
            jour = "Le Mardi"
        if jour == "Wednesday":
            jour = "Le Mercredi"
        if jour == "Thursday":
            jour = "Le Jeudi"
        if jour == "Friday":
            jour = "Le Vendredi"
        if jour == "Saturday":
            jour = "Le Samedi"
        if jour == "Sunday":
            jour = "Le Dimanche"
        print(time.strftime("on est "+jour+" %d /%m /%Y elle est  %H :%I :%S"))
        print()
        # calendar of month
        print(calendar.month(year, month))

    """ User can see calendar for next month and previous month """
    def display_pre_or_next_month(self):
        respense=input('taper s pour mois suivant ou p pour le mois précédent: ')
        month=datetime.date.today().month
        if 1< month <12:
            if respense == "s":
                self.display_today_month(month+1)
            if respense == "p":
                self.display_today_month(month-1)
    
    """  Admin can see all events on a specific date - Admin can cancel (delete) an event """
    def display(self,user_or_admin):
        liste_of_dicto=list()
        if user_or_admin == 'ADMIN':
            liste_of_dicto = self.model.get_all_events_by_admin()
        if user_or_admin == 'USER':
            liste_of_dicto = self.model.get_all_events_by_user()
        print(" voici la liste des de tout evenements anisi que le role et le nom des utilisateurs: ")
        for dicto in liste_of_dicto:
            print(View.OKBLUE + """-------------------------------------------------""" )
            events = Events(dicto)
            role = Role(dicto)
            user = User(dicto)
            print(events,role,user)

