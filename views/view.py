
import calendar
import datetime
import time

class View:

    def __init__(self,model,controller):

        self.model=model
        self.controller=controller


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
    
    """  User can see all events on a specific date - User can cancel (delete) an event """
    def display_all_events(self):
        pass

