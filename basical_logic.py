def AND(a, b):
    return a and b

def OR(a,b):
    return a or b

def NOT(a):
    return int(not a)

def XOR(*args):
    c = 0
    for k in args:
        c += k
    if c % 2 == 0:
        return 0
    else:
        return 1
    
def XNOR(*args):
    return NOT(XOR(*args))

def NAND(a, b):
    return NOT(AND(a, b))

def NOR(a, b):
    return NOT(OR(a, b))

def print_Logical(LOGIC):
    print(f"----- {str(LOGIC).split(' ')[1]} -----")
    print(f"{str(LOGIC).split(' ')[1]}(0, 0) : {LOGIC(0, 0)}")
    print(f"{str(LOGIC).split(' ')[1]}(0, 1) : {LOGIC(0, 1)}")
    print(f"{str(LOGIC).split(' ')[1]}(1, 0) : {LOGIC(1, 0)}")
    print(f"{str(LOGIC).split(' ')[1]}(1, 1) : {LOGIC(1, 1)}")
    print('---------------')

if __name__ == "__main__":
    print_Logical(AND)
    print_Logical(OR)
    print_Logical(XOR)
    print_Logical(XNOR)
    print_Logical(NAND)
    print_Logical(NOR)