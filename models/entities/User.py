class User:

    """ constructor of User i initialise id_user to 0 """
    def __init__(self,dicto):
        self.name=None
        self.firstName=None
        self.hydrate(dicto)

    def hydrate(self, dicto):
        for key, value in dicto.items():
            if hasattr(self, key):
                setattr(self, key, value)


    """ description of user """ 
    def __repr__(self): 

        return "Personne: nom({}), prénom({})".format(self.name, self.firstName))

