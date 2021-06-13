import functools

@functools.lru_cache(maxsize=None)
def fib_recursive(n):
    if n <= 1:
        return n;
    return fib_recursive(n-1) + fib_recursive(n-2);

def fib_generator(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

#   F_20 correct result: 6765

result = fib_recursive(20)
print("result=(%s)" % result)

result = list(fib_generator(20))[-1]
print("result=(%s)" % result)

*_, result = fib_generator(20)
print("result=(%s)" % result)

first = next(fib_generator(20))
print("first=(%s)" % first)

first, *_ = fib_generator(20)
print("first=(%s)" % first)

