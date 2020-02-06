
from controllers.Controller import Controller
from views.view import View
from models.Model import Model
import datetime
model=Model()
view=View(model)
#model.creation_count_user('emira','emira','emira')
#model.add_role_user('emira','emira','USER')
controller=Controller(model,view)
view.display_all_informations_events()
controller.update_event()
view.display_all_informations_events()