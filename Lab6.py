import random

def lehmann_primality_test(P, k=10):
    if P <= 2 or P % 2 == 0:
        return False  # Not valid input or even number
    
    for i in range(k):
        a = random.randint(2, P - 2)
        exp = (P - 1) // 2
        mod = pow(a, exp, P)

        if mod != 1 and mod != P - 1:
            print(f"Failed at iteration {i+1} with a = {a}")
            return False
    
    return True

# --- Example Usage ---
if __name__ == "__main__":
    P = int(input("Enter an odd integer P > 2: "))
    if lehmann_primality_test(P):
        print(f"{P} is probably prime.")
    else:
        print(f"{P} is composite.")
