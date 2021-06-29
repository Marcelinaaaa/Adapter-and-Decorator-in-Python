cache_fib = {0: 0, 1: 1}


def fibonacci(n):
    """Returns the suite of Fibonacci numbers"""
    assert (n >= 0), 'n must be >= 0'

    if n in cache_fib:
        return cache_fib[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    cache_fib[n] = res
    return res


if __name__ == '__main__':
    from timeit import Timer

    t = Timer('fibonacci(300)', 'from __main__ import fibonacci')
    print('Time: ', t.timeit())