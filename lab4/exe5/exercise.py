base = float(input("Base: "))
exp = int(input("Exponent (non-negative integer): "))
result = 1
for _ in range(exp):
    result *= base
print(result)   # same as base ** exp