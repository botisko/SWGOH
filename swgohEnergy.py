"""SWGOH Energy Calculation Script"""

import sys, datetime

# Energy limit constant for both types
energyLimit = 144
# Weekdays list
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday', 'Saturday')
# Refils
reffils = ([11, 00], [17, 00], [20, 00], [23, 00])

def tempEnergy():
    """Sketch for automatic energy calculation based on weekday"""
    actualWeekday = days[datetime.date.today().weekday()]
    actualTime = datetime.datetime.now().strftime('%H:%M')

    print("Today is", days[datetime.date.today().weekday()], "now is", actualTime)

    b = actualTime.split(':')

    actualTimeNow = datetime.timedelta(hours=int(b[0]), minutes=int(b[1]))

def main(cantina, actualEnergy, timeToRefill):
    """Function countEnergy counts the actual energy value to use"""
    # Determine what type of energy will be used based on input arguments
    if cantina == 'c':
        energyIncr = 6
        energyType = 'cantina energy.'
    elif cantina == 'e':
        energyIncr = 10
        energyType = 'energy.'
    else:
        raise ValueError('Unknown energy type. Use \'e\' for normal energy and \'c\' for cantina energy.')

    # Count the extra energy
    try:
        energyToWaste = actualEnergy + (timeToRefill * energyIncr) - energyLimit
    except ValueError:
        print('Input value must be integer.')

    # No energy to spend before refill
    if energyToWaste < 0:
        energyToWaste = 0

    print("You can spend",energyToWaste,energyType)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
