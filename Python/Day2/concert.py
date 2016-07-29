import musician #importing file i.e modues
#from musician import Musician #More specific
class Concert(object):
    '''This is class for concert.'''

    def __init__ (self, instruments,size,seats,celebrity):
        self.instruments = instruments
        self.size = size
        self.seats = seats
        self.celeb = celebrity

    def get_promotion_text(self):
        musician_text = ''
        for Musician in self.celeb:
            musician_text = musician_text + ' ' + musician.name
        text = 'Student discount alert! Shoreline {} Concert will have {} seats with capacity of {}, performing by {}'.format(' '.join(self.instruments),self.seats,self.size,musician_text)
        return text

instruments = ['Triangle', 'Guitar']
seats = ['VIP','Student']
ts = musician.Musician('Taylor Swift','female','pop', 'Singer')
bk = musician.Musician('Beyonce','female','R&B', 'Singer')
celebrity = [bk.name,ts.name]
s_concert = Concert(instruments, 300, [], [])
print s_concert.get_promotion_text()
