from basical_logic import *
import math

def HA(a, b):
    return XOR(a, b), AND(a, b)

def FA(a, b, carry):
    return XOR(XOR(a, b), carry), OR(AND(carry, XOR(a, b)), AND(a, b))

def test_complex3(LOGIC):
    print(f"----- {str(LOGIC).split(' ')[1]} Test -----")
    print(f"{str(LOGIC).split(' ')[1]}(0, 0, 0) : {LOGIC(0, 0, 0)}")
    print(f"{str(LOGIC).split(' ')[1]}(0, 0, 1) : {LOGIC(0, 0, 1)}")
    print(f"{str(LOGIC).split(' ')[1]}(0, 1, 0) : {LOGIC(0, 1, 0)}")
    print(f"{str(LOGIC).split(' ')[1]}(0, 1, 1) : {LOGIC(0, 1, 1)}")
    print(f"{str(LOGIC).split(' ')[1]}(1, 0, 0) : {LOGIC(1, 0, 0)}")
    print(f"{str(LOGIC).split(' ')[1]}(1, 0, 1) : {LOGIC(1, 0, 1)}")
    print(f"{str(LOGIC).split(' ')[1]}(1, 1, 0) : {LOGIC(1, 1, 0)}")
    print(f"{str(LOGIC).split(' ')[1]}(1, 1, 1) : {LOGIC(1, 1, 1)}")
    print('---------------')

if __name__ == "__main__":
    print_Logical(HA)
    test_complex3(FA)