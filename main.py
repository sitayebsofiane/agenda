
from controllers.Controller import Controller
from views.view import View
from models.Model import Model
import datetime
model=Model()
view=View(model)
controller=Controller(model,view)
view.display_all_events()
model.update_events_admin('bruno',datetime.datetime.today(),'no thing','mal partout')
