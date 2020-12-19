boolA, boolOperate, boolB = input('Enter Boolean expression: ').split()
boolSol = None
try:
    valA = int(boolA)
    valB = int(boolB)
except ValueError:
    print('Error: Inputs entered incorrectly')
    boolA, boolOperate, boolB = input('Try again: ').split()
finally:
    if (valA > 1) or (valB > 1):
        print(f'Error: the operands require > 1 bit')
    if boolOperate == '|':
        boolSol = valA | valB
    elif boolOperate == '&':
        boolSol = valA & valB
    elif boolOperate == '^':
        boolSol = valA ^ valB
    else:
        print(f'{boolOperate} is an invalid operator')
print(f'{boolA} {boolOperate} {boolB} = {boolSol}')