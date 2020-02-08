
from controllers.controller import Controller
from views.view import View
from models.model import Model
model=Model("ecole","postgres","as122014","localhost","5432")
view=View(model)
controller=Controller(model,view)

if __name__ == "__main__":
    
    controller.dispatcher()
