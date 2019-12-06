import timeit


def memoize(function):
    def wrapper(*args):
        cache = dict()

        if args in cache:
            return cache[args]
        result = function(*args)
        cache[args] = result
        return result
    return wrapper


def factorial(n):
    if n==1 or n == 0:
        return 1
    else:
        return n * (n-1)


memoize_factorial  = memoize(factorial)

print(factorial(100))
print(memoize_factorial(100))

timeit.timeit(factorial(100), number=10000)
timeit.timeit(memoize_factorial(100), number=10000)
