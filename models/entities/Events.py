class Events:

    """ constructor of Events """
    def __init__(self,title,date,description):
        self.id_event=0
        self.title=title
        self.date=date
        self.description=description

    """ method to return houre """
    def houre(self,date):

        pass

    
    """ description of event """ 
    def __repr__(self): 

        return "Event: title({}), date{}), description({})".format(self.title, self.date, self.description)
    
