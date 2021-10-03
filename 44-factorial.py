# n = 4
# product = 1
# for i in range(4):
#     product = product * (i+1)

# print(product)

'''
def factorail_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

f = factorail_iter(5)
print(f)

'''


def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5)
print(f)
