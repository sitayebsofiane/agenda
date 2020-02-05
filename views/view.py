
import calendar
import datetime
import time

class View:

    def __init__(self,model,controller):

        self.model=model
        self.controller=controller


    """  The home page displays today's date and calendar for the current month """
    def display_today(self, month = datetime.date.today().month):
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
    def display_month(self):
       pass
