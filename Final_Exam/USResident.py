class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self,name)
        if status not in ["citizen","legal_resident","illegal_resident"]:
            raise ValueError("Errore")
        self.status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        return  self.status
