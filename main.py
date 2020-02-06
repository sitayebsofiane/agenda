
from controllers.Controller import Controller
from views.view import View
from models.Model import Model
model=Model()
view=View(model)
controller=Controller(model,view)
while __name__ == "__main__" and input("taper q pour quité , ENTER si vous vouler continuer").lower() != 'q':
    
    controller.dispatcher()
