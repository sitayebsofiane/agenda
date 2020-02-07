class User:

    """ constructor of User i initialise id_user to 0 """
    def __init__(self,dicto):
        self.name=name
        self.firstName=firstName
        self.email=email
        self.password=password
        self.hydrate(dicto)

    def hydrate(self, dicto):
        for key, value in dicto.items():
            if hassttr(self, key):
                setattr(self, key, value)


    """ description of user """ 
    def __repr__(self): 

        return "Personne: nom({}), prénom({}), âge({})".format(self.name, self.firstName, self.email)

