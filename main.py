
from controllers.controller import Controller
from views.view import View
from models.model import Model
model=Model()
view=View(model)
controller=Controller(model,view)

while __name__ == "__main__" and input("taper q pour quiter , ENTER si vous vouler continuer: ").lower() != 'q':
    
    controller.dispatcher()
