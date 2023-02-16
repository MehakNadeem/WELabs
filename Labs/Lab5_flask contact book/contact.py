class contact:
    def __init__(self,name='',mobileno='',city='',profession=''):
        self.id=None
        self.name=name
        self.mobileno=mobileno
        self.city=city
        self.profession=profession

    def print(self):
        print( 'Name:' + self.name + '\n' + 'Mobile no: ' + self.mobileno + '\n' + 'City: ' + self.city + '\n' + 'Profession: ' + self.profession)


