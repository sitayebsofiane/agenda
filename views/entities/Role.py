class Role:


    """ class to define the roles and i init id_role to 0"""
    def __init__(self,dicto):
        self.role = None
        self.role_description = None
        self.hydrate(dicto)

    def hydrate(self, dicto):
        for key, value in dicto.items():
            if hasattr(self, key):
                setattr(self, key, value)

    """ description of role """ 
    def __repr__(self):
        return "Role: role({}), description({})".format(self.role, self.role_description)
