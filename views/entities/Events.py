class Events:

    """ constructor of Events """
    def __init__(self,dicto):
        self.title=None
        self.date=None
        self.description=None
        self.hydrate(dicto)

    def hydrate(self, dicto):
        for key, value in dicto.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    """ description of event """ 
    def __repr__(self): 

        return "Event: title({}), date{}), description({})".format(self.title, self.date, self.description)
    
