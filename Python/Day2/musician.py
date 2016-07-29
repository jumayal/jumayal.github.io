class Musician:
    '''This is a class for Musician.Yeaaaahhh'''
    #Constructor - THE method to create an instance from a class
    # _ _ init _ _ <-- Two Underscores
    #Part of Class
    def __init__(self,name,gender,genre,mtype):
        #The Name of the Musician
        #property of the class
        self.name = name
        #Gender of Musician
        #property of the class
        self.gender = gender
        #Genre of Musician
        #property of the class
        self.genre = genre
        # The type of the Musician
        #property of the class
        self.mtype = mtype
    def print_description(self):
        print '{} is a {} {} {}.'.format(self.name,self.gender,self.genre,self.mtype)

ts = Musician('Taylor Swift','female','pop', 'Singer')
bk = Musician('Beyonce','female','R&B', 'Singer')

#ts.print_description()
#bk.print_description()

#classroom = 'Ajohlo'
#print type(classroom)
#print dir(classroom)
