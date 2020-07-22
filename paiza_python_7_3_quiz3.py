# ‹ã‹ã‚Ì•\‚ğì¬‚µ‚Ä‚İ‚æ‚¤

def multiply(x, y):
    return x * y

for num in range(1, 10):
    for num2 in range(1, 10):
        print(multiply(num, num2), end="")
        if num2 < 9:
            print(", ", end="")
    print()
