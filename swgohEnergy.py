"""SWGOH Energy Calculation Script"""

import sys

# Energy limit constant for both types
energyLimit = 144

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
        raise ValueError('Unknown energy type.')

    # Count the extra energy
    energyToWaste =  actualEnergy + (timeToRefill * energyIncr) - energyLimit

    print("You can spend",energyToWaste,energyType)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
