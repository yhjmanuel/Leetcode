# Uses python3
import sys

def gcd_naive(a, b):
    if b < a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    

    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
