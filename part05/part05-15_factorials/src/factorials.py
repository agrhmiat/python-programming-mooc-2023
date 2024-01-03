# Write your solution here

def factorials(n: int) -> dict:
    fact = {}
    res = 1
    for i in range(1, n+1):
        if n == 0:
            fact[i] = 1
        else:
            res *= i
            fact[i] = res
    return fact

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
