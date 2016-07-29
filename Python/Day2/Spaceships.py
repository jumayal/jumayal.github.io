
class spaceships:
    def __init__(ship,shape,fuel,speed,seats):
        ship.shape = shape
        ship.fuel = fuel
        ship.speed = speed
        ship.seats = seats
    def stats (ship):
        print 'With the shape of a {} and with {} gallons, you should travel {} km/s with your group of {}.'.format(ship.shape,ship.fuel,ship.speed,ship.seats)

al = spaceships("disk","10","10000000","10")
hum = spaceships("cylinder", "100","100", "4")
al.stats()
