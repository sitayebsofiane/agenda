class User:

    """ constructor of User i initialise id_user to 0 """
    def __init__(self,name,firstName,password):
        self.id_user=0
        self.name=name
        self.firstName=firstName
        self.email=email
        self.password=password


    """ description of user """ 
    def __repr__(self): 

        return "Personne: nom({}), prénom({}), âge({})".format(self.name, self.firstName, self.email)

