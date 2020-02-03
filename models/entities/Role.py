class Role:


    """ class to define the roles and i init id_role to 0"""
    def __init__(self,role,role_description):
        self.id_role=0
        self.role=role
        self.role_description=role_description

         """ description of role """ 
    def __repr__(self): 

        return "Role: role({}), description({})".format(self.role, self.role_description)
