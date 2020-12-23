import prog5Functions
low = None
hi = None
numTraps = None
cont = None
another = None
valCorrect = None
askAgain = None
while cont != 0:
    askAgain = 1
    while askAgain != 0:
        low, hi = input("Enter endpoints of interval to be integrated (low hi): ").split()
        try:
            verifyLow = float(low)
            verifyHi = float(hi)
        except ValueError:
            print("Error: Improperly formatted input")
            continue
        if (hi < low):
            print("Error: low must be lower than high")
            continue
        numTraps = input("Enter number of trapezoids to be used: ")
        try:
            verifyTraps = int(numTraps)
        except ValueError:
            print("Error: not a number")
            continue
        askAgain = 0
    print(f'Using {numTraps} trapezoids, integral between {low} and {hi} is {prog5Functions.integrate(low, hi, numTraps)}')
    askAgain = 1
    while askAgain != 0:
        answer = input('Evaluate another integral (Y/N)?')
        if answer == "y" or answer == "Y":
            askAgain = 0
        elif answer == "n" or answer == "N":
            askAgain = 0
            cont = 0
        else:
            print("Error: must enter Y or N")
            continue
