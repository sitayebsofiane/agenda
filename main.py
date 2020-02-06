
from controllers.Controller import Controller
from views.view import View
from models.Model import Model
import datetime
model=Model()
view=View(model)
controller=Controller(model,view)
controller.dispatcher()
